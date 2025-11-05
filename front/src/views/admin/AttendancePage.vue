<template>
  <div>
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-slate-800 mb-2">Посещаемость</h1>
        <p class="text-slate-600">Отметка посещаемости клиентов</p>
      </div>
      <button @click="openMarkModal" class="btn btn-primary">
        <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        Отметить посещение
      </button>
    </div>

    <div class="mb-6 card">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Дата</label>
          <input v-model="filters.date" type="date" class="input" @change="loadAttendance" />
        </div>
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Секция</label>
          <select v-model="filters.section_id" class="input" @change="loadAttendance">
            <option value="">Все секции</option>
            <option v-for="section in sections" :key="section.id" :value="section.id">
              {{ section.name }}
            </option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Статус</label>
          <select v-model="filters.status" class="input" @change="loadAttendance">
            <option value="">Все</option>
            <option value="Присутствовал">Присутствовал</option>
            <option value="Отсутствовал">Отсутствовал</option>
            <option value="Опоздал">Опоздал</option>
          </select>
        </div>
      </div>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка данных..." />

    <div v-else-if="attendanceList.length > 0" class="card">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead>
            <tr class="border-b border-slate-200">
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Клиент</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Секция</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Дата</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Статус</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="att in attendanceList"
              :key="att.id"
              class="border-b border-slate-100 hover:bg-slate-50"
            >
              <td class="py-3 px-4 font-medium">{{ att.client_name }}</td>
              <td class="py-3 px-4">{{ att.section_name }}</td>
              <td class="py-3 px-4">{{ formatDate(att.attendance_date) }}</td>
              <td class="py-3 px-4">
                <span
                  class="badge"
                  :class="{
                    'badge-success': att.status === 'Присутствовал',
                    'badge-danger': att.status === 'Отсутствовал',
                    'badge-warning': att.status === 'Опоздал'
                  }"
                >
                  {{ att.status }}
                </span>
              </td>
              <td class="py-3 px-4">
                <select
                  @change="updateAttendance(att, $event.target.value)"
                  :value="att.status"
                  class="text-sm border border-slate-300 rounded px-2 py-1"
                >
                  <option value="Присутствовал">Присутствовал</option>
                  <option value="Отсутствовал">Отсутствовал</option>
                  <option value="Опоздал">Опоздал</option>
                </select>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600 mb-4">Записи не найдены</p>
      <button @click="openMarkModal" class="btn btn-primary">Отметить посещение</button>
    </div>

    <Modal v-model="showMarkModal" title="Отметить посещение">
      <form @submit.prevent="markAttendance" class="space-y-4">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Бронирование *</label>
          <select v-model.number="markForm.booking_id" required class="input">
            <option value="">Выберите бронирование</option>
            <option v-for="booking in activeBookings" :key="booking.id" :value="booking.id">
              {{ booking.client_name }} - {{ booking.section_name }} - {{ formatDate(booking.booking_date) }}
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Статус *</label>
          <select v-model="markForm.status" required class="input">
            <option value="Присутствовал">Присутствовал</option>
            <option value="Отсутствовал">Отсутствовал</option>
            <option value="Опоздал">Опоздал</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Дата посещения *</label>
          <input v-model="markForm.attendance_date" type="date" required class="input" />
        </div>

        <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {{ error }}
        </div>
      </form>

      <template #footer>
        <button @click="showMarkModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="markAttendance" :disabled="isMarking" class="btn btn-primary">
          {{ isMarking ? 'Сохранение...' : 'Сохранить' }}
        </button>
      </template>
    </Modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import Modal from '@/components/common/Modal.vue'
import { adminAttendanceService, adminBookingsService, adminSectionsService } from '@/api/services'

const attendanceList = ref([])
const sections = ref([])
const activeBookings = ref([])
const isLoading = ref(false)
const showMarkModal = ref(false)
const isMarking = ref(false)
const error = ref('')

const filters = ref({
  date: '',
  section_id: '',
  status: ''
})

const markForm = ref({
  booking_id: '',
  status: 'Присутствовал',
  attendance_date: new Date().toISOString().split('T')[0]
})

onMounted(async () => {
  await Promise.all([loadAttendance(), loadSections(), loadActiveBookings()])
})

const loadAttendance = async () => {
  try {
    isLoading.value = true
    const params = {}
    if (filters.value.date) params.date = filters.value.date
    if (filters.value.section_id) params.section_id = filters.value.section_id
    if (filters.value.status) params.status = filters.value.status
    
    const response = await adminAttendanceService.getAll(params)
    attendanceList.value = response.data
  } catch (err) {
    console.error('Error loading attendance:', err)
  } finally {
    isLoading.value = false
  }
}

const loadSections = async () => {
  try {
    const response = await adminSectionsService.getAll()
    sections.value = response.data
  } catch (err) {
    console.error('Error loading sections:', err)
  }
}

const loadActiveBookings = async () => {
  try {
    const response = await adminBookingsService.getAll({ status: 'Подтверждено' })
    activeBookings.value = response.data
  } catch (err) {
    console.error('Error loading bookings:', err)
  }
}

const openMarkModal = () => {
  markForm.value = {
    booking_id: '',
    status: 'Присутствовал',
    attendance_date: new Date().toISOString().split('T')[0]
  }
  error.value = ''
  showMarkModal.value = true
}

const markAttendance = async () => {
  try {
    isMarking.value = true
    error.value = ''
    await adminAttendanceService.mark(markForm.value)
    showMarkModal.value = false
    await loadAttendance()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка отметки посещения'
  } finally {
    isMarking.value = false
  }
}

const updateAttendance = async (attendance, newStatus) => {
  try {
    await adminAttendanceService.update(attendance.id, { status: newStatus })
    attendance.status = newStatus
  } catch (err) {
    console.error('Error updating attendance:', err)
    alert('Ошибка обновления')
    await loadAttendance()
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU')
}
</script>
