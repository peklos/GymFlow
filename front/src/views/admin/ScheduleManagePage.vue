<template>
  <div>
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-slate-800 mb-2">Управление расписанием</h1>
        <p class="text-slate-600">Создание и редактирование расписания занятий</p>
      </div>
      <button @click="openCreateModal" class="btn btn-primary">
        <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Добавить занятие
      </button>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка расписания..." />

    <div v-else-if="scheduleItems.length > 0" class="space-y-6">
      <div v-for="item in scheduleItems" :key="item.id" class="card">
        <div class="flex items-start justify-between">
          <div class="flex-1">
            <div class="flex items-center gap-3 mb-3">
              <h3 class="text-xl font-bold text-slate-800">{{ item.section_name }}</h3>
              <span class="badge badge-info">{{ item.day_of_week }}</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
              <div class="flex items-center gap-2 text-slate-600">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span>{{ item.time_start }} - {{ item.time_end }}</span>
              </div>

              <div class="flex items-center gap-2 text-slate-600">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                <span>Тренер: {{ item.trainer_name }}</span>
              </div>

              <div v-if="item.location" class="flex items-center gap-2 text-slate-600">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                <span>Место: {{ item.location }}</span>
              </div>
            </div>
          </div>

          <div class="flex gap-2 ml-4">
            <button @click="openEditModal(item)" class="btn btn-secondary">Редактировать</button>
            <button @click="confirmDelete(item)" class="btn btn-danger">Удалить</button>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600 mb-4">Расписание пусто</p>
      <button @click="openCreateModal" class="btn btn-primary">Добавить первое занятие</button>
    </div>

    <Modal v-model="showModal" :title="editingItem ? 'Редактировать занятие' : 'Добавить занятие'">
      <form @submit.prevent="saveItem" class="space-y-4">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Секция *</label>
          <select v-model.number="form.section_id" required class="input" @change="loadTrainers">
            <option value="">Выберите секцию</option>
            <option v-for="section in sections" :key="section.id" :value="section.id">
              {{ section.name }}
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Тренер *</label>
          <select v-model.number="form.trainer_id" required class="input">
            <option value="">Выберите тренера</option>
            <option v-for="trainer in trainers" :key="trainer.id" :value="trainer.id">
              {{ trainer.full_name }}
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">День недели *</label>
          <select v-model="form.day_of_week" required class="input">
            <option value="">Выберите день</option>
            <option value="Понедельник">Понедельник</option>
            <option value="Вторник">Вторник</option>
            <option value="Среда">Среда</option>
            <option value="Четверг">Четверг</option>
            <option value="Пятница">Пятница</option>
            <option value="Суббота">Суббота</option>
            <option value="Воскресенье">Воскресенье</option>
          </select>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Время начала *</label>
            <input v-model="form.start_time" type="time" required class="input" />
          </div>
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Время окончания *</label>
            <input v-model="form.end_time" type="time" required class="input" />
          </div>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Место проведения</label>
          <input v-model="form.location" type="text" class="input" placeholder="Зал №1, Спортзал и т.д." />
        </div>

        <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {{ error }}
        </div>
      </form>

      <template #footer>
        <button @click="showModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="saveItem" :disabled="isSaving" class="btn btn-primary">
          {{ isSaving ? 'Сохранение...' : 'Сохранить' }}
        </button>
      </template>
    </Modal>

    <Modal v-model="showDeleteModal" title="Удаление занятия">
      <div v-if="itemToDelete">
        <p class="text-slate-700 mb-4">Вы уверены, что хотите удалить это занятие из расписания?</p>
        <div class="p-4 bg-slate-50 rounded-lg">
          <p class="font-semibold text-slate-800">{{ itemToDelete.section_name }}</p>
          <p class="text-slate-600">{{ itemToDelete.day_of_week }}, {{ itemToDelete.time_start }}</p>
        </div>
      </div>

      <template #footer>
        <button @click="showDeleteModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="deleteItem" :disabled="isDeleting" class="btn btn-danger">
          {{ isDeleting ? 'Удаление...' : 'Удалить' }}
        </button>
      </template>
    </Modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import Modal from '@/components/common/Modal.vue'
import { adminScheduleService, adminSectionsService, adminTrainersService } from '@/api/services'

const scheduleItems = ref([])
const sections = ref([])
const trainers = ref([])
const isLoading = ref(false)
const showModal = ref(false)
const showDeleteModal = ref(false)
const editingItem = ref(null)
const itemToDelete = ref(null)
const isSaving = ref(false)
const isDeleting = ref(false)
const error = ref('')

const form = ref({
  section_id: '',
  trainer_id: '',
  day_of_week: '',
  time_start: '09:00',
  time_end: '10:00',
  max_participants: 10
})

onMounted(async () => {
  await Promise.all([loadSchedule(), loadSections(), loadTrainers()])
})

const loadSchedule = async () => {
  try {
    isLoading.value = true
    const response = await adminScheduleService.getAll()
    scheduleItems.value = response.data
  } catch (err) {
    console.error('Error loading schedule:', err)
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

const loadTrainers = async () => {
  try {
    const response = await adminTrainersService.getAll()
    trainers.value = response.data
  } catch (err) {
    console.error('Error loading trainers:', err)
  }
}

const openCreateModal = () => {
  editingItem.value = null
  form.value = {
    section_id: '',
    trainer_id: '',
    day_of_week: '',
    time_start: '09:00',
    time_end: '10:00',
    max_participants: 10
  }
  error.value = ''
  showModal.value = true
}

const openEditModal = (item) => {
  editingItem.value = item
  form.value = {
    section_id: item.section_id,
    trainer_id: item.trainer_id,
    day_of_week: item.day_of_week,
    time_start: item.time_start,
    time_end: item.time_end,
    max_participants: item.max_participants
  }
  error.value = ''
  showModal.value = true
}

const saveItem = async () => {
  try {
    isSaving.value = true
    error.value = ''

    if (editingItem.value) {
      await adminScheduleService.update(editingItem.value.id, form.value)
    } else {
      await adminScheduleService.create(form.value)
    }

    showModal.value = false
    await loadSchedule()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка сохранения'
  } finally {
    isSaving.value = false
  }
}

const confirmDelete = (item) => {
  itemToDelete.value = item
  showDeleteModal.value = true
}

const deleteItem = async () => {
  try {
    isDeleting.value = true
    await adminScheduleService.delete(itemToDelete.value.id)
    showDeleteModal.value = false
    await loadSchedule()
  } catch (err) {
    console.error('Error deleting schedule item:', err)
    alert('Ошибка удаления')
  } finally {
    isDeleting.value = false
  }
}
</script>
