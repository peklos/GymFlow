<template>
  <div>
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-slate-800 mb-2">Управление тренерами</h1>
        <p class="text-slate-600">Добавление и редактирование тренеров</p>
      </div>
      <button @click="openCreateModal" class="btn btn-primary">
        <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Добавить тренера
      </button>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка тренеров..." />

    <div v-else-if="trainers.length > 0" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div
        v-for="trainer in trainers"
        :key="trainer.id"
        class="card"
      >
        <div class="flex items-start justify-between mb-4">
          <div class="flex-1">
            <h3 class="text-xl font-bold text-slate-800 mb-2">
              {{ trainer.last_name }} {{ trainer.first_name }} {{ trainer.patronymic }}
            </h3>
            <p class="text-slate-600 mb-2">{{ trainer.specialization }}</p>
          </div>
          <div class="w-16 h-16 bg-gradient-to-br from-purple-100 to-purple-200 rounded-xl flex items-center justify-center">
            <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </div>
        </div>

        <div class="space-y-2 mb-4">
          <div class="flex items-center gap-2 text-sm text-slate-600">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            <span>{{ trainer.phone_number }}</span>
          </div>
          <div class="flex items-center gap-2 text-sm text-slate-600">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <span>Стаж: {{ trainer.experience_years }} {{ pluralizeYears(trainer.experience_years) }}</span>
          </div>
        </div>

        <div class="flex gap-2">
          <button @click="openEditModal(trainer)" class="btn btn-secondary flex-1">
            Редактировать
          </button>
          <button @click="confirmDelete(trainer)" class="btn btn-danger flex-1">
            Удалить
          </button>
        </div>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600 mb-4">Тренеры не найдены</p>
      <button @click="openCreateModal" class="btn btn-primary">
        Добавить первого тренера
      </button>
    </div>

    <!-- Create/Edit Modal -->
    <Modal v-model="showModal" :title="editingTrainer ? 'Редактировать тренера' : 'Добавить тренера'">
      <form @submit.prevent="saveTrainer" class="space-y-4">
        <div class="grid grid-cols-3 gap-4">
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Фамилия *</label>
            <input v-model="form.last_name" type="text" required class="input" />
          </div>
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Имя *</label>
            <input v-model="form.first_name" type="text" required class="input" />
          </div>
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Отчество</label>
            <input v-model="form.patronymic" type="text" class="input" />
          </div>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Специализация *</label>
          <input v-model="form.specialization" type="text" required placeholder="Например: Фитнес, Йога, Бокс" class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Телефон *</label>
          <input v-model="form.phone_number" type="tel" required placeholder="+7 (999) 123-45-67" class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Стаж работы (лет) *</label>
          <input v-model.number="form.experience_years" type="number" required min="0" class="input" />
        </div>

        <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {{ error }}
        </div>
      </form>

      <template #footer>
        <button @click="showModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="saveTrainer" :disabled="isSaving" class="btn btn-primary">
          {{ isSaving ? 'Сохранение...' : 'Сохранить' }}
        </button>
      </template>
    </Modal>

    <!-- Delete Confirmation Modal -->
    <Modal v-model="showDeleteModal" title="Удаление тренера">
      <div v-if="trainerToDelete">
        <p class="text-slate-700 mb-4">Вы уверены, что хотите удалить тренера?</p>
        <div class="p-4 bg-slate-50 rounded-lg">
          <p class="font-semibold text-slate-800">
            {{ trainerToDelete.last_name }} {{ trainerToDelete.first_name }}
          </p>
          <p class="text-slate-600">{{ trainerToDelete.specialization }}</p>
        </div>
      </div>

      <template #footer>
        <button @click="showDeleteModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="deleteTrainer" :disabled="isDeleting" class="btn btn-danger">
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
import { adminTrainersService } from '@/api/services'

const trainers = ref([])
const isLoading = ref(false)
const showModal = ref(false)
const showDeleteModal = ref(false)
const editingTrainer = ref(null)
const trainerToDelete = ref(null)
const isSaving = ref(false)
const isDeleting = ref(false)
const error = ref('')

const form = ref({
  first_name: '',
  last_name: '',
  patronymic: '',
  specialization: '',
  phone_number: '',
  experience_years: 0
})

onMounted(async () => {
  await loadTrainers()
})

const loadTrainers = async () => {
  try {
    isLoading.value = true
    const response = await adminTrainersService.getAll()
    trainers.value = response.data
  } catch (err) {
    console.error('Error loading trainers:', err)
  } finally {
    isLoading.value = false
  }
}

const openCreateModal = () => {
  editingTrainer.value = null
  form.value = {
    first_name: '',
    last_name: '',
    patronymic: '',
    specialization: '',
    phone_number: '',
    experience_years: 0
  }
  error.value = ''
  showModal.value = true
}

const openEditModal = (trainer) => {
  editingTrainer.value = trainer
  form.value = { ...trainer }
  error.value = ''
  showModal.value = true
}

const saveTrainer = async () => {
  try {
    isSaving.value = true
    error.value = ''

    if (editingTrainer.value) {
      await adminTrainersService.update(editingTrainer.value.id, form.value)
    } else {
      await adminTrainersService.create(form.value)
    }

    showModal.value = false
    await loadTrainers()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка сохранения'
  } finally {
    isSaving.value = false
  }
}

const confirmDelete = (trainer) => {
  trainerToDelete.value = trainer
  showDeleteModal.value = true
}

const deleteTrainer = async () => {
  try {
    isDeleting.value = true
    await adminTrainersService.delete(trainerToDelete.value.id)
    showDeleteModal.value = false
    await loadTrainers()
  } catch (err) {
    console.error('Error deleting trainer:', err)
    alert('Ошибка удаления тренера')
  } finally {
    isDeleting.value = false
  }
}

const pluralizeYears = (years) => {
  const cases = [2, 0, 1, 1, 1, 2]
  const titles = ['год', 'года', 'лет']
  return titles[(years % 100 > 4 && years % 100 < 20) ? 2 : cases[Math.min(years % 10, 5)]]
}
</script>

<style scoped>
</style>
