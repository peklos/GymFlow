<template>
  <div>
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-slate-800 mb-2">Управление бронированиями</h1>
      <p class="text-slate-600">Просмотр и управление бронированиями клиентов</p>
    </div>

    <div class="mb-6 grid grid-cols-1 md:grid-cols-4 gap-4">
      <div class="card bg-gradient-to-br from-blue-500 to-blue-600 text-white">
        <p class="text-blue-100 text-sm mb-1">Всего бронирований</p>
        <p class="text-3xl font-bold">{{ stats.total }}</p>
      </div>
      <div class="card bg-gradient-to-br from-green-500 to-green-600 text-white">
        <p class="text-green-100 text-sm mb-1">Подтверждено</p>
        <p class="text-3xl font-bold">{{ stats.confirmed }}</p>
      </div>
      <div class="card bg-gradient-to-br from-yellow-500 to-yellow-600 text-white">
        <p class="text-yellow-100 text-sm mb-1">Ожидание</p>
        <p class="text-3xl font-bold">{{ stats.pending }}</p>
      </div>
      <div class="card bg-gradient-to-br from-red-500 to-red-600 text-white">
        <p class="text-red-100 text-sm mb-1">Отменено</p>
        <p class="text-3xl font-bold">{{ stats.cancelled }}</p>
      </div>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка бронирований..." />

    <div v-else-if="bookings.length > 0" class="card">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead>
            <tr class="border-b border-slate-200">
              <th class="text-left py-3 px-4 font-semibold text-slate-700">ID</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Клиент</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Секция</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Дата</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Время</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Статус</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="booking in bookings"
              :key="booking.id"
              class="border-b border-slate-100 hover:bg-slate-50"
            >
              <td class="py-3 px-4">{{ booking.id }}</td>
              <td class="py-3 px-4 font-medium">{{ booking.client_name }}</td>
              <td class="py-3 px-4">{{ booking.section_name }}</td>
              <td class="py-3 px-4">{{ formatDate(booking.booking_date) }}</td>
              <td class="py-3 px-4">{{ booking.time_start }}</td>
              <td class="py-3 px-4">
                <span
                  class="badge"
                  :class="{
                    'badge-success': booking.status === 'Подтверждено',
                    'badge-warning': booking.status === 'Ожидание',
                    'badge-danger': booking.status === 'Отменено'
                  }"
                >
                  {{ booking.status }}
                </span>
              </td>
              <td class="py-3 px-4">
                <select
                  v-if="booking.status !== 'Отменено'"
                  @change="updateStatus(booking, $event.target.value)"
                  :value="booking.status"
                  class="text-sm border border-slate-300 rounded px-2 py-1"
                >
                  <option value="Ожидание">Ожидание</option>
                  <option value="Подтверждено">Подтверждено</option>
                  <option value="Отменено">Отменено</option>
                </select>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600">Бронирования не найдены</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { adminBookingsService } from '@/api/services'

const bookings = ref([])
const isLoading = ref(false)

const stats = computed(() => {
  const total = bookings.value.length
  const confirmed = bookings.value.filter(b => b.status === 'Подтверждено').length
  const pending = bookings.value.filter(b => b.status === 'Ожидание').length
  const cancelled = bookings.value.filter(b => b.status === 'Отменено').length
  return { total, confirmed, pending, cancelled }
})

onMounted(async () => {
  await loadBookings()
})

const loadBookings = async () => {
  try {
    isLoading.value = true
    const response = await adminBookingsService.getAll()
    bookings.value = response.data
  } catch (err) {
    console.error('Error loading bookings:', err)
  } finally {
    isLoading.value = false
  }
}

const updateStatus = async (booking, newStatus) => {
  try {
    await adminBookingsService.updateStatus(booking.id, { status: newStatus })
    booking.status = newStatus
  } catch (err) {
    console.error('Error updating status:', err)
    alert('Ошибка обновления статуса')
    await loadBookings()
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU')
}
</script>
