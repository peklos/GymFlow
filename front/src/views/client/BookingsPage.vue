<template>
  <MainLayout>
    <div class="container mx-auto px-4 py-12">
      <!-- Header -->
      <div class="mb-12">
        <h1 class="text-4xl font-bold gradient-text mb-2">Мои бронирования</h1>
        <p class="text-slate-600">Управляйте своими записями на занятия</p>
      </div>

      <LoadingSpinner v-if="isLoading" text="Загрузка бронирований..." />

      <!-- Bookings List -->
      <div v-else-if="bookings.length > 0" class="space-y-6">
        <div
          v-for="booking in sortedBookings"
          :key="booking.id"
          class="card"
        >
          <div class="flex items-start justify-between">
            <div class="flex-1">
              <div class="flex items-center gap-3 mb-3">
                <h3 class="text-xl font-bold text-slate-800">
                  {{ booking.section_name }}
                </h3>
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
              </div>

              <div class="space-y-2">
                <div class="flex items-center gap-2 text-slate-600">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  <span>Дата: <span class="font-semibold">{{ formatDate(booking.booking_date) }}</span></span>
                </div>

                <div class="flex items-center gap-2 text-slate-600">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span>{{ booking.day_of_week }}, {{ booking.time_start }} - {{ booking.time_end }}</span>
                </div>

                <div class="flex items-center gap-2 text-slate-600">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  <span>Тренер: <span class="font-semibold">{{ booking.trainer_name }}</span></span>
                </div>
              </div>
            </div>

            <button
              v-if="booking.status !== 'Отменено' && !isPast(booking.booking_date)"
              @click="confirmCancel(booking)"
              class="btn btn-danger ml-4"
            >
              Отменить
            </button>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-20">
        <div class="w-32 h-32 bg-gradient-to-br from-slate-200 to-slate-300 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-16 h-16 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-slate-800 mb-2">Нет бронирований</h3>
        <p class="text-slate-600 mb-6">Вы еще не записались ни на одно занятие</p>
        <router-link to="/schedule" class="btn btn-primary">
          Посмотреть расписание
        </router-link>
      </div>
    </div>

    <!-- Cancel Confirmation Modal -->
    <Modal v-model="showCancelModal" title="Отмена бронирования">
      <div v-if="bookingToCancel">
        <p class="text-slate-700 mb-4">
          Вы уверены, что хотите отменить бронирование?
        </p>
        <div class="p-4 bg-slate-50 rounded-lg">
          <p class="font-semibold text-slate-800">{{ bookingToCancel.section_name }}</p>
          <p class="text-slate-600">{{ formatDate(bookingToCancel.booking_date) }}, {{ bookingToCancel.time_start }}</p>
        </div>
      </div>

      <template #footer>
        <button @click="showCancelModal = false" class="btn btn-secondary">
          Нет, оставить
        </button>
        <button @click="cancelBooking" :disabled="isCancelling" class="btn btn-danger">
          {{ isCancelling ? 'Отмена...' : 'Да, отменить' }}
        </button>
      </template>
    </Modal>
  </MainLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import MainLayout from '@/components/layout/MainLayout.vue'
import Modal from '@/components/common/Modal.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useBookingsStore } from '@/stores/bookings'
import { useAuthStore } from '@/stores/auth'

const bookingsStore = useBookingsStore()
const authStore = useAuthStore()

const bookings = ref([])
const isLoading = ref(false)
const showCancelModal = ref(false)
const bookingToCancel = ref(null)
const isCancelling = ref(false)

const sortedBookings = computed(() => {
  return [...bookings.value].sort((a, b) => {
    return new Date(b.booking_date) - new Date(a.booking_date)
  })
})

onMounted(async () => {
  await loadBookings()
})

const loadBookings = async () => {
  try {
    isLoading.value = true
    await bookingsStore.fetchClientBookings(authStore.user.client_id)
    bookings.value = bookingsStore.bookings
  } catch (error) {
    console.error('Error loading bookings:', error)
  } finally {
    isLoading.value = false
  }
}

const confirmCancel = (booking) => {
  bookingToCancel.value = booking
  showCancelModal.value = true
}

const cancelBooking = async () => {
  try {
    isCancelling.value = true
    await bookingsStore.cancelBooking(bookingToCancel.value.id)
    bookings.value = bookings.value.filter(b => b.id !== bookingToCancel.value.id)
    showCancelModal.value = false
  } catch (error) {
    console.error('Error cancelling booking:', error)
    alert('Ошибка при отмене бронирования')
  } finally {
    isCancelling.value = false
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const isPast = (dateString) => {
  return new Date(dateString) < new Date()
}
</script>

<style scoped>
</style>
