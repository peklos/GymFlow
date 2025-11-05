<template>
  <MainLayout>
    <div class="min-h-[80vh] flex items-center justify-center px-4 py-12">
      <div class="max-w-md w-full">
        <!-- Header -->
        <div class="text-center mb-8">
          <div class="w-20 h-20 bg-gradient-to-br from-primary-500 to-accent-500 rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-glow">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
            </svg>
          </div>
          <h1 class="text-3xl font-bold gradient-text mb-2">Вход в GymFlow</h1>
          <p class="text-slate-600">Войдите в свой аккаунт, чтобы продолжить</p>
        </div>

        <!-- Login Form -->
        <div class="card">
          <form @submit.prevent="handleLogin" class="space-y-6">
            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">
                Email
              </label>
              <input
                v-model="form.login"
                type="email"
                required
                placeholder="your@email.com"
                class="input"
                :class="{ 'input-error': error }"
              />
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">
                Пароль
              </label>
              <input
                v-model="form.password"
                type="password"
                required
                placeholder="••••••••"
                class="input"
                :class="{ 'input-error': error }"
              />
            </div>

            <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg">
              <p class="text-red-700 text-sm">{{ error }}</p>
            </div>

            <button
              type="submit"
              :disabled="isLoading"
              class="btn btn-primary w-full"
            >
              {{ isLoading ? 'Вход...' : 'Войти' }}
            </button>
          </form>

          <div class="mt-6 text-center">
            <p class="text-slate-600">
              Нет аккаунта?
              <router-link to="/register" class="text-primary-600 hover:text-primary-700 font-semibold">
                Зарегистрироваться
              </router-link>
            </p>
          </div>

          <div class="mt-6 pt-6 border-t border-slate-200 text-center">
            <router-link to="/admin/login" class="text-sm text-slate-500 hover:text-slate-700">
              Вход для сотрудников →
            </router-link>
          </div>
        </div>

        <!-- Test Credentials -->
        <div class="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <p class="text-sm font-semibold text-blue-800 mb-2">Тестовые данные:</p>
          <p class="text-sm text-blue-700">Email: ivanov@mail.ru</p>
          <p class="text-sm text-blue-700">Пароль: user123</p>
        </div>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import MainLayout from '@/components/layout/MainLayout.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const form = ref({
  login: '',
  password: ''
})

const error = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  try {
    isLoading.value = true
    error.value = ''

    await authStore.login(form.value)

    // Redirect to original page or home
    const redirect = route.query.redirect || '/'
    router.push(redirect)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Неверный email или пароль'
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
</style>
