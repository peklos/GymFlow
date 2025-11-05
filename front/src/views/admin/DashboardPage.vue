<template>
  <div>
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-slate-800 mb-2">Дашборд</h1>
      <p class="text-slate-600">Обзор системы управления спортзалом</p>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка статистики..." />

    <div v-else-if="stats" class="space-y-8">
      <!-- Stats Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Total Clients -->
        <div class="card bg-gradient-to-br from-blue-500 to-blue-600 text-white">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-blue-100 text-sm mb-1">Всего клиентов</p>
              <p class="text-3xl font-bold">{{ stats.total_clients }}</p>
            </div>
            <div class="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Total Trainers -->
        <div class="card bg-gradient-to-br from-purple-500 to-purple-600 text-white">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-purple-100 text-sm mb-1">Всего тренеров</p>
              <p class="text-3xl font-bold">{{ stats.total_trainers }}</p>
            </div>
            <div class="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Total Sections -->
        <div class="card bg-gradient-to-br from-green-500 to-green-600 text-white">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-green-100 text-sm mb-1">Всего секций</p>
              <p class="text-3xl font-bold">{{ stats.total_sections }}</p>
            </div>
            <div class="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Total Bookings -->
        <div class="card bg-gradient-to-br from-orange-500 to-orange-600 text-white">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-orange-100 text-sm mb-1">Всего бронирований</p>
              <p class="text-3xl font-bold">{{ stats.total_bookings }}</p>
            </div>
            <div class="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Additional Info -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Recent Activity -->
        <div class="card">
          <h2 class="text-xl font-bold mb-4" style="color: #1e293b !important;">Быстрый доступ</h2>
          <div class="space-y-3">
            <router-link to="/admin/clients" class="flex items-center justify-between p-3 rounded-lg hover:bg-blue-50 transition-colors group">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                  </svg>
                </div>
                <span class="font-medium" style="color: #1e293b !important;">Управление клиентами</span>
              </div>
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>

            <router-link to="/admin/sections" class="flex items-center justify-between p-3 rounded-lg hover:bg-green-50 transition-colors group">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                  </svg>
                </div>
                <span class="font-medium" style="color: #1e293b !important;">Управление секциями</span>
              </div>
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>

            <router-link to="/admin/schedule" class="flex items-center justify-between p-3 rounded-lg hover:bg-purple-50 transition-colors group">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
                <span class="font-medium" style="color: #1e293b !important;">Управление расписанием</span>
              </div>
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>

            <router-link to="/admin/bookings" class="flex items-center justify-between p-3 rounded-lg hover:bg-orange-50 transition-colors group">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                  </svg>
                </div>
                <span class="font-medium" style="color: #1e293b !important;">Управление бронированиями</span>
              </div>
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>
          </div>
        </div>

        <!-- System Info -->
        <div class="card">
          <h2 class="text-xl font-bold mb-4" style="color: #1e293b !important;">Информация о системе</h2>
          <div class="space-y-4">
            <div>
              <p class="text-sm mb-1" style="color: #64748b !important;">Текущий пользователь</p>
              <p class="text-lg font-semibold" style="color: #1e293b !important;">{{ authStore.user?.login || 'Не указан' }}</p>
            </div>

            <div>
              <p class="text-sm mb-1" style="color: #64748b !important;">Роль</p>
              <p class="text-lg font-semibold" style="color: #1e293b !important;">{{ authStore.user?.role_name || 'Не указана' }}</p>
            </div>

            <div>
              <p class="text-sm mb-1" style="color: #64748b !important;">Версия системы</p>
              <p class="text-lg font-semibold" style="color: #1e293b !important;">GymFlow v1.0.0</p>
            </div>

            <div class="pt-4 border-t border-slate-200">
              <router-link to="/" class="text-primary-600 hover:text-primary-700 font-medium">
                Перейти на главную страницу →
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { adminStatsService } from '@/api/services'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const stats = ref(null)
const isLoading = ref(false)

onMounted(async () => {
  await loadStats()
})

const loadStats = async () => {
  try {
    isLoading.value = true
    const response = await adminStatsService.getDashboard()
    stats.value = response.data
  } catch (error) {
    console.error('Error loading stats:', error)
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
</style>
