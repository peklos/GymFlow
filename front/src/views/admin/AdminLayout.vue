<template>
  <div class="min-h-screen bg-slate-100">
    <!-- Top Bar -->
    <header class="bg-gradient-to-r from-slate-800 to-slate-900 text-white shadow-lg sticky top-0 z-40">
      <div class="flex items-center justify-between px-6 py-4">
        <div class="flex items-center space-x-4">
          <button
            @click="toggleSidebar"
            class="lg:hidden p-2 rounded-lg hover:bg-white/10"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>

          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <div>
              <h1 class="text-lg font-bold">Админ-панель GymFlow</h1>
              <p class="text-xs text-slate-300">Панель управления</p>
            </div>
          </div>
        </div>

        <div class="flex items-center space-x-4">
          <div class="text-right hidden sm:block">
            <p class="font-semibold">{{ authStore.employee?.name }}</p>
            <p class="text-xs text-slate-300">{{ authStore.employee?.role_name }}</p>
          </div>

          <button
            @click="handleLogout"
            class="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg transition-colors"
          >
            Выход
          </button>
        </div>
      </div>
    </header>

    <div class="flex">
      <!-- Sidebar -->
      <aside
        :class="[
          'fixed lg:sticky top-0 left-0 h-screen bg-white border-r border-slate-200 shadow-lg transition-transform duration-300 z-30',
          sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
        ]"
        style="top: 72px; height: calc(100vh - 72px);"
      >
        <nav class="p-4 space-y-2 w-64">
          <router-link
            v-for="item in menuItems"
            :key="item.path"
            :to="item.path"
            class="flex items-center space-x-3 px-4 py-3 rounded-xl transition-all duration-200 font-medium"
            :class="isActive(item.path)
              ? 'bg-gradient-to-r from-primary-600 to-accent-600 text-white shadow-lg'
              : 'hover:bg-slate-100'"
            :style="!isActive(item.path) ? 'color: #1e293b !important;' : ''"
            @click="closeSidebar"
          >
            <component :is="item.icon" class="w-5 h-5" />
            <span>{{ item.label }}</span>
          </router-link>
        </nav>
      </aside>

      <!-- Overlay for mobile -->
      <div
        v-if="sidebarOpen"
        @click="closeSidebar"
        class="fixed inset-0 bg-black/50 z-20 lg:hidden"
      ></div>

      <!-- Main Content -->
      <main class="flex-1 p-6">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const sidebarOpen = ref(false)

const menuItems = [
  {
    path: '/admin',
    label: 'Дашборд',
    icon: 'DashboardIcon'
  },
  {
    path: '/admin/clients',
    label: 'Клиенты',
    icon: 'UsersIcon'
  },
  {
    path: '/admin/trainers',
    label: 'Тренеры',
    icon: 'TrainersIcon'
  },
  {
    path: '/admin/sections',
    label: 'Секции',
    icon: 'SectionsIcon'
  },
  {
    path: '/admin/schedule',
    label: 'Расписание',
    icon: 'ScheduleIcon'
  },
  {
    path: '/admin/bookings',
    label: 'Бронирования',
    icon: 'BookingsIcon'
  },
  {
    path: '/admin/attendance',
    label: 'Посещаемость',
    icon: 'AttendanceIcon'
  },
  {
    path: '/admin/employees',
    label: 'Сотрудники',
    icon: 'EmployeesIcon'
  }
]

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value
}

const closeSidebar = () => {
  sidebarOpen.value = false
}

const isActive = (path) => {
  return route.path === path || (path !== '/admin' && route.path.startsWith(path))
}

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}
</script>

<script>
// Icon Components
export default {
  components: {
    DashboardIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
        </svg>
      `
    },
    UsersIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
      `
    },
    TrainersIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
        </svg>
      `
    },
    SectionsIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
        </svg>
      `
    },
    ScheduleIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
      `
    },
    BookingsIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
        </svg>
      `
    },
    AttendanceIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
      `
    },
    EmployeesIcon: {
      template: `
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
        </svg>
      `
    }
  }
}
</script>

<style scoped>
</style>
