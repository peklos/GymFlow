<template>
  <div>
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-slate-800 mb-2">Управление секциями</h1>
        <p class="text-slate-600" style="color: #0f172a !important;">Создание и редактирование секций</p>
      </div>
      <button @click="openCreateModal" class="btn btn-primary">
        <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Добавить секцию
      </button>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка секций..." />

    <div v-else-if="sections.length > 0" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div v-for="section in sections" :key="section.id" class="card">
        <div class="flex items-start justify-between mb-4">
          <div class="flex-1">
            <h3 class="text-xl font-bold text-slate-800 mb-2">{{ section.name }}</h3>
            <div class="flex gap-2 mb-2">
              <span class="badge badge-info">{{ section.sport_type }}</span>
              <span v-if="section.is_free" class="badge badge-success">Бесплатно</span>
            </div>
          </div>
        </div>

        <p class="text-slate-600 text-sm mb-4">{{ section.description }}</p>

        <div class="space-y-2 mb-4 text-sm">
          <div class="flex items-center gap-2 text-slate-600">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
            <span>Возраст: {{ section.age_from }}-{{ section.age_to }} лет</span>
          </div>
        </div>

        <div class="flex gap-2">
          <button @click="openEditModal(section)" class="btn btn-secondary flex-1">Редактировать</button>
          <button @click="confirmDelete(section)" class="btn btn-danger flex-1">Удалить</button>
        </div>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600 mb-4">Секции не найдены</p>
      <button @click="openCreateModal" class="btn btn-primary">Добавить первую секцию</button>
    </div>

    <Modal v-model="showModal" :title="editingSection ? 'Редактировать секцию' : 'Добавить секцию'">
      <form @submit.prevent="saveSection" class="space-y-4">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Название *</label>
          <input v-model="form.name" type="text" required class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Вид спорта *</label>
          <select v-model="form.sport_type" required class="input">
            <option value="">Выберите вид</option>
            <option value="Фитнес">Фитнес</option>
            <option value="Йога">Йога</option>
            <option value="Бокс">Бокс</option>
            <option value="Плавание">Плавание</option>
            <option value="Танцы">Танцы</option>
            <option value="Единоборства">Единоборства</option>
          </select>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Возраст от *</label>
            <input v-model.number="form.age_from" type="number" required min="0" class="input" />
          </div>
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Возраст до *</label>
            <input v-model.number="form.age_to" type="number" required min="0" class="input" />
          </div>
        </div>

        <div>
          <label class="flex items-center space-x-2 cursor-pointer">
            <input v-model="form.is_free" type="checkbox" class="w-5 h-5 rounded" />
            <span class="text-slate-700 font-medium">Бесплатная секция</span>
          </label>
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Описание</label>
          <textarea v-model="form.description" rows="3" class="input"></textarea>
        </div>

        <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {{ error }}
        </div>
      </form>

      <template #footer>
        <button @click="showModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="saveSection" :disabled="isSaving" class="btn btn-primary">
          {{ isSaving ? 'Сохранение...' : 'Сохранить' }}
        </button>
      </template>
    </Modal>

    <Modal v-model="showDeleteModal" title="Удаление секции">
      <div v-if="sectionToDelete">
        <p class="text-slate-700 mb-4">Вы уверены, что хотите удалить секцию?</p>
        <div class="p-4 bg-slate-50 rounded-lg">
          <p class="font-semibold text-slate-800">{{ sectionToDelete.name }}</p>
          <p class="text-slate-600">{{ sectionToDelete.sport_type }}</p>
        </div>
      </div>

      <template #footer>
        <button @click="showDeleteModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="deleteSection" :disabled="isDeleting" class="btn btn-danger">
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
import { adminSectionsService } from '@/api/services'

const sections = ref([])
const isLoading = ref(false)
const showModal = ref(false)
const showDeleteModal = ref(false)
const editingSection = ref(null)
const sectionToDelete = ref(null)
const isSaving = ref(false)
const isDeleting = ref(false)
const error = ref('')

const form = ref({
  name: '',
  sport_type: '',
  age_from: 18,
  age_to: 65,
  is_free: false,
  description: ''
})

onMounted(async () => {
  await loadSections()
})

const loadSections = async () => {
  try {
    isLoading.value = true
    const response = await adminSectionsService.getAll()
    sections.value = response.data
  } catch (err) {
    console.error('Error loading sections:', err)
  } finally {
    isLoading.value = false
  }
}

const openCreateModal = () => {
  editingSection.value = null
  form.value = {
    name: '',
    sport_type: '',
    age_from: 18,
    age_to: 65,
    is_free: false,
    description: ''
  }
  error.value = ''
  showModal.value = true
}

const openEditModal = (section) => {
  editingSection.value = section
  form.value = { ...section }
  error.value = ''
  showModal.value = true
}

const saveSection = async () => {
  try {
    isSaving.value = true
    error.value = ''

    if (editingSection.value) {
      await adminSectionsService.update(editingSection.value.id, form.value)
    } else {
      await adminSectionsService.create(form.value)
    }

    showModal.value = false
    await loadSections()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка сохранения'
  } finally {
    isSaving.value = false
  }
}

const confirmDelete = (section) => {
  sectionToDelete.value = section
  showDeleteModal.value = true
}

const deleteSection = async () => {
  try {
    isDeleting.value = true
    await adminSectionsService.delete(sectionToDelete.value.id)
    showDeleteModal.value = false
    await loadSections()
  } catch (err) {
    console.error('Error deleting section:', err)
    alert('Ошибка удаления секции')
  } finally {
    isDeleting.value = false
  }
}
</script>
