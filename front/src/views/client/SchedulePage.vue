<template>
  <MainLayout>
    <div class="container mx-auto px-4 py-12">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl lg:text-5xl font-bold mb-4">
          <span class="gradient-text">Расписание занятий</span>
        </h1>
        <p class="text-xl text-slate-600">
          Выбери удобное время и забронируй тренировку
        </p>
      </div>

      <!-- Filters -->
      <div class="card mb-8 max-w-4xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Секция
            </label>
            <select v-model="filters.section_id" class="input" @change="loadSchedule">
              <option value="">Все секции</option>
              <option v-for="section in sections" :key="section.id" :value="section.id">
                {{ section.name }}
              </option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">
              День недели
            </label>
            <select v-model="filters.day_of_week" class="input" @change="loadSchedule">
              <option value="">Все дни</option>
              <option value="Понедельник">Понедельник</option>
              <option value="Вторник">Вторник</option>
              <option value="Среда">Среда</option>
              <option value="Четверг">Четверг</option>
              <option value="Пятница">Пятница</option>
              <option value="Суббота">Суббота</option>
              <option value="Воскресенье">Воскресенье</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Время
            </label>
            <input
              v-model="filters.time_start"
              type="time"
              class="input"
              @change="loadSchedule"
            />
          </div>
        </div>
      </div>

      <!-- Loading -->
      <LoadingSpinner v-if="isLoading" text="Загрузка расписания..." />

      <!-- Schedule List -->
      <div v-else-if="scheduleItems.length > 0" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div
          v-for="item in scheduleItems"
          :key="item.id"
          class="card card-hover"
        >
          <div class="flex items-start justify-between mb-4">
            <div class="flex-1">
              <h3 class="text-xl font-bold text-slate-800 mb-2">
                {{ item.section_name }}
              </h3>
              <p class="text-slate-600 mb-2">
                Тренер: <span class="font-semibold">{{ item.trainer_name }}</span>
              </p>
            </div>
            <span class="badge badge-info">{{ item.day_of_week }}</span>
          </div>

          <div class="space-y-3 mb-4">
            <div class="flex items-center gap-2 text-slate-600">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>{{ item.time_start.substring(0, 5) }} - {{ item.time_end.substring(0, 5) }}</span>
            </div>

            <div class="flex items-center gap-2 text-slate-600">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
              <span>Макс. участников: {{ item.max_participants }}</span>
            </div>
          </div>

          <button
            v-if="authStore.isAuthenticated"
            @click="openBookingModal(item)"
            class="btn btn-primary w-full"
          >
            Забронировать
          </button>
          <router-link
            v-else
            to="/login"
            class="btn btn-primary w-full"
          >
            Войти для бронирования
          </router-link>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-20">
        <div class="w-32 h-32 bg-gradient-to-br from-slate-200 to-slate-300 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-16 h-16 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-slate-800 mb-2">Расписание не найдено</h3>
        <p class="text-slate-600 mb-6">Попробуйте изменить параметры поиска</p>
      </div>
    </div>

    <!-- Booking Modal -->
    <Modal v-model="showBookingModal" title="Забронировать занятие">
      <div v-if="selectedSchedule" class="space-y-4">
        <div>
          <h4 class="font-semibold text-slate-800 mb-2">{{ selectedSchedule.section_name }}</h4>
          <p class="text-slate-600">Тренер: {{ selectedSchedule.trainer_name }}</p>
          <p class="text-slate-600">{{ selectedSchedule.day_of_week }}, {{ selectedSchedule.time_start.substring(0, 5) }}</p>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Дата занятия
          </label>
          <input
            v-model="bookingDate"
            type="date"
            :min="minDate"
            class="input"
          />
        </div>

        <div v-if="bookingError" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
          {{ bookingError }}
        </div>
      </div>

      <template #footer>
        <button @click="showBookingModal = false" class="btn btn-secondary">
          Отмена
        </button>
        <button @click="createBooking" :disabled="isBooking" class="btn btn-primary">
          {{ isBooking ? 'Бронирование...' : 'Забронировать' }}
        </button>
      </template>
    </Modal>
  </MainLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import MainLayout from '@/components/layout/MainLayout.vue'
import Modal from '@/components/common/Modal.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { scheduleService } from '@/api/services'
import { useSectionsStore } from '@/stores/sections'
import { useBookingsStore } from '@/stores/bookings'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const sectionsStore = useSectionsStore()
const bookingsStore = useBookingsStore()
const authStore = useAuthStore()

const scheduleItems = ref([])
const sections = ref([])
const isLoading = ref(false)
const showBookingModal = ref(false)
const selectedSchedule = ref(null)
const bookingDate = ref('')
const bookingError = ref('')
const isBooking = ref(false)

const filters = ref({
  section_id: route.query.section_id || '',
  day_of_week: '',
  time_start: ''
})

const minDate = computed(() => {
  const today = new Date()
  return today.toISOString().split('T')[0]
})

onMounted(async () => {
  await loadSections()
  await loadSchedule()
})

const loadSections = async () => {
  try {
    await sectionsStore.fetchSections()
    sections.value = sectionsStore.sections
  } catch (error) {
    console.error('Error loading sections:', error)
  }
}

const loadSchedule = async () => {
  try {
    isLoading.value = true
    const params = {}
    if (filters.value.section_id) params.section_id = filters.value.section_id
    if (filters.value.day_of_week) params.day_of_week = filters.value.day_of_week
    if (filters.value.time_start) params.time_start = filters.value.time_start

    const response = await scheduleService.getAll(params)
    scheduleItems.value = response.data
  } catch (error) {
    console.error('Error loading schedule:', error)
  } finally {
    isLoading.value = false
  }
}

const openBookingModal = (schedule) => {
  selectedSchedule.value = schedule
  bookingDate.value = minDate.value
  bookingError.value = ''
  showBookingModal.value = true
}

const createBooking = async () => {
  if (!bookingDate.value) {
    bookingError.value = 'Выберите дату занятия'
    return
  }

  try {
    isBooking.value = true
    bookingError.value = ''

    await bookingsStore.createBooking({
      client_id: authStore.user.client_id,
      schedule_id: selectedSchedule.value.id,
      booking_date: bookingDate.value
    })

    showBookingModal.value = false
    alert('Бронирование создано успешно!')
  } catch (error) {
    bookingError.value = error.response?.data?.detail || 'Ошибка при создании бронирования'
  } finally {
    isBooking.value = false
  }
}
</script>

<style scoped>
</style>
