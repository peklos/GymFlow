<template>
  <header class="glass border-b border-white/20 sticky top-0 z-50 shadow-lg">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-20">
        <!-- Logo -->
        <router-link to="/" class="flex items-center space-x-3 group">
          <div class="w-12 h-12 bg-gradient-to-br from-primary-500 to-accent-500 rounded-2xl flex items-center justify-center transform group-hover:scale-110 transition-transform duration-300 shadow-glow">
            <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <span class="text-2xl font-bold gradient-text hidden md:block">GymFlow</span>
        </router-link>

        <!-- Desktop Navigation -->
        <nav class="hidden lg:flex items-center space-x-8">
          <router-link
            v-for="link in navLinks"
            :key="link.path"
            :to="link.path"
            class="text-slate-700 hover:text-primary-600 font-medium transition-colors duration-200 relative group"
          >
            {{ link.label }}
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-primary-600 to-accent-600 group-hover:w-full transition-all duration-300"></span>
          </router-link>
        </nav>

        <!-- User Actions -->
        <div class="flex items-center space-x-4">
          <template v-if="authStore.isAuthenticated || authStore.isAdmin">
            <div class="hidden md:flex items-center space-x-3">
              <div class="text-right">
                <p class="text-sm font-semibold text-slate-800">
                  {{ authStore.currentUser?.full_name || authStore.currentUser?.name }}
                </p>
                <p class="text-xs text-slate-500">
                  {{ authStore.isAdmin ? 'Сотрудник' : 'Клиент' }}
                </p>
              </div>
              <div class="w-10 h-10 bg-gradient-to-br from-primary-400 to-accent-400 rounded-full flex items-center justify-center text-white font-bold shadow-lg">
                {{ getUserInitial() }}
              </div>
            </div>
            <button
              @click="handleLogout"
              class="btn btn-secondary text-sm py-2 px-4"
            >
              Выход
            </button>
          </template>
          <template v-else>
            <router-link to="/login" class="btn btn-secondary text-sm py-2 px-4">
              Вход
            </router-link>
            <router-link to="/register" class="btn btn-primary text-sm py-2 px-4 hidden md:inline-block">
              Регистрация
            </router-link>
          </template>

          <!-- Mobile Menu Button -->
          <button
            @click="toggleMobileMenu"
            class="lg:hidden p-2 rounded-lg hover:bg-slate-100 transition-colors"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                v-if="!mobileMenuOpen"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
              <path
                v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition name="slide">
      <div v-if="mobileMenuOpen" class="lg:hidden border-t border-white/20 bg-white/95 backdrop-blur-md">
        <nav class="container mx-auto px-4 py-4 space-y-2">
          <router-link
            v-for="link in navLinks"
            :key="link.path"
            :to="link.path"
            @click="closeMobileMenu"
            class="block px-4 py-3 rounded-lg text-slate-700 hover:bg-primary-50 hover:text-primary-600 font-medium transition-colors"
          >
            {{ link.label }}
          </router-link>
        </nav>
      </div>
    </transition>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const mobileMenuOpen = ref(false)

const navLinks = computed(() => {
  const links = [
    { path: '/', label: 'Главная' },
    { path: '/sections', label: 'Секции' },
    { path: '/schedule', label: 'Расписание' },
    { path: '/search', label: 'Поиск' },
  ]

  if (authStore.isAuthenticated) {
    links.push(
      { path: '/profile', label: 'Профиль' },
      { path: '/bookings', label: 'Бронирования' }
    )
  }

  if (authStore.isAdmin) {
    links.push({ path: '/admin', label: 'Админ-панель' })
  }

  return links
})

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobileMenu = () => {
  mobileMenuOpen.value = false
}

const getUserInitial = () => {
  const name = authStore.currentUser?.full_name || authStore.currentUser?.name || 'U'
  return name.charAt(0).toUpperCase()
}

const handleLogout = () => {
  authStore.logout()
  router.push('/')
  closeMobileMenu()
}
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from {
  transform: translateY(-100%);
  opacity: 0;
}

.slide-leave-to {
  transform: translateY(-100%);
  opacity: 0;
}
</style>
