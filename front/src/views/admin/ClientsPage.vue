<template>
  <div>
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-slate-800 mb-2">Управление клиентами</h1>
      <p class="text-slate-600">Просмотр и редактирование информации о клиентах</p>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка клиентов..." />

    <div v-else-if="clients.length > 0" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div
        v-for="client in clients"
        :key="client.id"
        class="card"
      >
        <div class="flex items-start justify-between mb-4">
          <div class="flex-1">
            <h3 class="text-xl font-bold text-slate-800 mb-2">{{ client.full_name }}</h3>
            <p class="text-slate-600 text-sm mb-1">{{ client.email }}</p>
          </div>
          <div class="w-16 h-16 bg-gradient-to-br from-blue-100 to-blue-200 rounded-xl flex items-center justify-center">
            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </div>
        </div>

        <div class="space-y-2 mb-4">
          <div class="flex items-center gap-2 text-sm text-slate-600">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            <span>{{ client.phone }}</span>
          </div>
          <div v-if="client.address" class="flex items-center gap-2 text-sm text-slate-600">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>{{ client.address }}</span>
          </div>
          <div v-if="client.date_of_birth" class="flex items-center gap-2 text-sm text-slate-600">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            <span>Дата рождения: {{ formatDate(client.date_of_birth) }}</span>
          </div>
          <div class="flex items-center gap-2 text-sm text-slate-600">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <span>Регистрация: {{ formatDate(client.registration_date) }}</span>
          </div>
        </div>

        <div class="flex gap-2">
          <button @click="openEditModal(client)" class="btn btn-secondary flex-1">
            Редактировать
          </button>
          <button @click="confirmDelete(client)" class="btn btn-danger flex-1">
            Удалить
          </button>
        </div>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600">Клиенты не найдены</p>
    </div>

    <!-- Edit Modal -->
    <Modal v-model="showModal" title="Редактировать клиента">
      <form @submit.prevent="saveClient" class="space-y-4">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">ФИО *</label>
          <input v-model="form.full_name" type="text" required class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Телефон *</label>
          <input v-model="form.phone" type="tel" required placeholder="+7 (999) 123-45-67" class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Email *</label>
          <input v-model="form.email" type="email" required class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Адрес</label>
          <input v-model="form.address" type="text" class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Дата рождения</label>
          <input v-model="form.date_of_birth" type="date" class="input" />
        </div>

        <div v-if="error" class="text-red-600 text-sm">{{ error }}</div>

        <div class="flex gap-3 pt-4">
          <button type="submit" :disabled="isSaving" class="btn btn-primary flex-1">
            <span v-if="isSaving">Сохранение...</span>
            <span v-else>Сохранить</span>
          </button>
          <button type="button" @click="showModal = false" class="btn btn-secondary flex-1">
            Отмена
          </button>
        </div>
      </form>
    </Modal>

    <!-- Delete Confirmation Modal -->
    <Modal v-model="showDeleteModal" title="Подтверждение удаления">
      <div class="space-y-4">
        <p class="text-slate-700">
          Вы уверены, что хотите удалить клиента <strong>{{ deletingClient?.full_name }}</strong>?
        </p>
        <p class="text-sm text-slate-600">
          Это действие нельзя отменить. Все бронирования клиента также будут удалены.
        </p>

        <div v-if="error" class="text-red-600 text-sm">{{ error }}</div>

        <div class="flex gap-3 pt-4">
          <button @click="deleteClient" :disabled="isDeleting" class="btn btn-danger flex-1">
            <span v-if="isDeleting">Удаление...</span>
            <span v-else>Удалить</span>
          </button>
          <button @click="showDeleteModal = false" class="btn btn-secondary flex-1">
            Отмена
          </button>
        </div>
      </div>
    </Modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import Modal from '@/components/common/Modal.vue'
import { adminClientsService } from '@/api/services'

const clients = ref([])
const isLoading = ref(false)
const showModal = ref(false)
const showDeleteModal = ref(false)
const editingClient = ref(null)
const deletingClient = ref(null)
const isSaving = ref(false)
const isDeleting = ref(false)
const error = ref('')

const form = ref({
  full_name: '',
  phone: '',
  email: '',
  address: '',
  date_of_birth: ''
})

onMounted(async () => {
  await loadClients()
})

const loadClients = async () => {
  try {
    isLoading.value = true
    const response = await adminClientsService.getAll()
    clients.value = response.data
  } catch (err) {
    console.error('Error loading clients:', err)
    error.value = 'Ошибка загрузки клиентов'
  } finally {
    isLoading.value = false
  }
}

const openEditModal = async (client) => {
  editingClient.value = client
  // Load full client details
  try {
    const response = await adminClientsService.getById(client.id)
    const clientData = response.data

    form.value = {
      full_name: clientData.full_name || '',
      phone: clientData.phone || '',
      email: clientData.email || '',
      address: clientData.address || '',
      date_of_birth: clientData.date_of_birth || ''
    }
    showModal.value = true
    error.value = ''
  } catch (err) {
    console.error('Error loading client details:', err)
    error.value = 'Ошибка загрузки данных клиента'
  }
}

const saveClient = async () => {
  try {
    isSaving.value = true
    error.value = ''

    // Prepare data - remove empty fields
    const updateData = {}
    if (form.value.full_name) updateData.full_name = form.value.full_name
    if (form.value.phone) updateData.phone = form.value.phone
    if (form.value.email) updateData.email = form.value.email
    if (form.value.address) updateData.address = form.value.address
    if (form.value.date_of_birth) updateData.date_of_birth = form.value.date_of_birth

    await adminClientsService.update(editingClient.value.id, updateData)
    showModal.value = false
    await loadClients()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка сохранения клиента'
  } finally {
    isSaving.value = false
  }
}

const confirmDelete = (client) => {
  deletingClient.value = client
  showDeleteModal.value = true
  error.value = ''
}

const deleteClient = async () => {
  try {
    isDeleting.value = true
    error.value = ''
    await adminClientsService.delete(deletingClient.value.id)
    showDeleteModal.value = false
    await loadClients()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка удаления клиента'
  } finally {
    isDeleting.value = false
  }
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU')
}
</script>

<style scoped>
</style>
