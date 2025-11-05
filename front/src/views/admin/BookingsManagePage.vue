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
              class="border-b border-slate-100 hover:bg-blue-50"
            >
              <td class="py-3 px-4">{{ booking.id }}</td>
              <td class="py-3 px-4 font-medium">{{ booking.client_name }}</td>
              <td class="py-3 px-4">{{ booking.section_name }}</td>
              <td class="py-3 px-4">{{ formatDate(booking.booking_date) }}</td>
              <td class="py-3 px-4">-</td>
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
                <div class="flex gap-2">
                  <button
                    @click="viewDetails(booking)"
                    class="text-sm text-blue-600 hover:text-blue-800 font-medium"
                  >
                    Подробнее
                  </button>
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
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600">Бронирования не найдены</p>
    </div>

    <!-- Booking Details Modal -->
    <Modal v-model="showDetailsModal" title="Детали бронирования">
      <LoadingSpinner v-if="isLoadingDetails" text="Загрузка..." />

      <div v-else-if="selectedBooking" class="space-y-4">
        <!-- Booking Info -->
        <div class="border-b border-slate-200 pb-4">
          <h3 class="text-lg font-bold text-slate-800 mb-3">Информация о бронировании</h3>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-sm text-slate-500">ID бронирования</p>
              <p class="font-semibold text-slate-800">{{ selectedBooking.id }}</p>
            </div>
            <div>
              <p class="text-sm text-slate-500">Статус</p>
              <p>
                <span
                  class="badge"
                  :class="{
                    'badge-success': selectedBooking.status === 'Подтверждено',
                    'badge-warning': selectedBooking.status === 'Ожидание',
                    'badge-danger': selectedBooking.status === 'Отменено'
                  }"
                >
                  {{ selectedBooking.status }}
                </span>
              </p>
            </div>
            <div>
              <p class="text-sm text-slate-500">Дата занятия</p>
              <p class="font-semibold text-slate-800">{{ formatDate(selectedBooking.booking_date) }}</p>
            </div>
          </div>
        </div>

        <!-- Client Info -->
        <div class="border-b border-slate-200 pb-4">
          <h3 class="text-lg font-bold text-slate-800 mb-3">Клиент</h3>
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 bg-gradient-to-br from-blue-100 to-blue-200 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <div>
              <p class="font-bold text-slate-800">{{ selectedBooking.client_name || 'Не указано' }}</p>
              <p class="text-sm text-slate-600">ID клиента: {{ selectedBooking.client_id }}</p>
            </div>
          </div>
        </div>

        <!-- Section Info -->
        <div class="border-b border-slate-200 pb-4">
          <h3 class="text-lg font-bold text-slate-800 mb-3">Секция</h3>
          <div class="bg-slate-50 rounded-lg p-4">
            <div class="grid grid-cols-2 gap-3">
              <div>
                <p class="text-sm text-slate-500">Название секции</p>
                <p class="font-semibold text-slate-800">{{ selectedBooking.section_name || 'Не указано' }}</p>
              </div>
              <div>
                <p class="text-sm text-slate-500">ID секции</p>
                <p class="font-semibold text-slate-800">{{ selectedBooking.section_id }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Actions -->
        <div class="pt-4">
          <button @click="showDetailsModal = false" class="btn btn-secondary w-full">
            Закрыть
          </button>
        </div>
      </div>
    </Modal>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import Modal from '@/components/common/Modal.vue'
import { adminBookingsService } from '@/api/services'

const bookings = ref([])
const isLoading = ref(false)
const showDetailsModal = ref(false)
const isLoadingDetails = ref(false)
const selectedBooking = ref(null)

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

const viewDetails = async (booking) => {
  try {
    isLoadingDetails.value = true
    showDetailsModal.value = true
    const response = await adminBookingsService.getById(booking.id)
    selectedBooking.value = response.data
  } catch (err) {
    console.error('Error loading booking details:', err)
    alert('Ошибка загрузки деталей бронирования')
    showDetailsModal.value = false
  } finally {
    isLoadingDetails.value = false
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
  if (!dateString) return 'Не указано'
  const date = new Date(dateString)
  if (isNaN(date.getTime())) return 'Не указано'
  return date.toLocaleDateString('ru-RU')
}
</script>
