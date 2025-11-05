<template>
  <div>
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-slate-800 mb-2">Управление сотрудниками</h1>
        <p class="text-slate-600">Управление персоналом системы</p>
      </div>
      <button @click="openCreateModal" class="btn btn-primary">
        <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Добавить сотрудника
      </button>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка сотрудников..." />

    <div v-else-if="employees.length > 0" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div v-for="employee in employees" :key="employee.id" class="card">
        <div class="flex items-start justify-between mb-4">
          <div class="flex-1">
            <h3 class="text-xl font-bold mb-2" style="color: #1e293b !important;">{{ employee.login }}</h3>
            <span
              class="badge"
              :class="{
                'badge-danger': employee.role_name === 'Администратор',
                'badge-info': employee.role_name === 'Менеджер'
              }"
            >
              {{ employee.role_name || 'Не указано' }}
            </span>
          </div>
          <div class="w-16 h-16 bg-gradient-to-br from-slate-700 to-slate-900 rounded-xl flex items-center justify-center">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
          </div>
        </div>

        <div class="space-y-2 mb-4 text-sm">
          <div class="flex items-center gap-2" style="color: #475569 !important;">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2" />
            </svg>
            <span>ID: {{ employee.id }}</span>
          </div>
        </div>

        <div class="flex gap-2">
          <button @click="openEditModal(employee)" class="btn btn-secondary flex-1">
            Редактировать
          </button>
          <button @click="confirmDelete(employee)" class="btn btn-danger flex-1">
            Удалить
          </button>
        </div>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600 mb-4">Сотрудники не найдены</p>
      <button @click="openCreateModal" class="btn btn-primary">Добавить первого сотрудника</button>
    </div>

    <Modal v-model="showModal" :title="editingEmployee ? 'Редактировать сотрудника' : 'Добавить сотрудника'">
      <form @submit.prevent="saveEmployee" class="space-y-4">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Имя *</label>
          <input v-model="form.name" type="text" required class="input" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Логин *</label>
          <input
            v-model="form.login"
            type="text"
            required
            :disabled="!!editingEmployee"
            class="input"
            placeholder="user@gym.ru"
          />
        </div>

        <div v-if="!editingEmployee">
          <label class="block text-sm font-semibold text-slate-700 mb-2">Пароль *</label>
          <input v-model="form.password" type="password" required class="input" minlength="6" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Роль *</label>
          <select v-model.number="form.role_id" required class="input">
            <option value="">Выберите роль</option>
            <option v-for="role in roles" :key="role.id" :value="role.id">
              {{ role.name }}
            </option>
          </select>
        </div>

        <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {{ error }}
        </div>
      </form>

      <template #footer>
        <button @click="showModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="saveEmployee" :disabled="isSaving" class="btn btn-primary">
          {{ isSaving ? 'Сохранение...' : 'Сохранить' }}
        </button>
      </template>
    </Modal>

    <Modal v-model="showDeleteModal" title="Удаление сотрудника">
      <div v-if="employeeToDelete">
        <p class="text-slate-700 mb-4">Вы уверены, что хотите удалить сотрудника?</p>
        <div class="p-4 bg-slate-50 rounded-lg">
          <p class="font-semibold text-slate-800">{{ employeeToDelete.name }}</p>
          <p class="text-slate-600">{{ employeeToDelete.role_name }}</p>
        </div>
      </div>

      <template #footer>
        <button @click="showDeleteModal = false" class="btn btn-secondary">Отмена</button>
        <button @click="deleteEmployee" :disabled="isDeleting" class="btn btn-danger">
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
import { adminEmployeesService, adminRolesService } from '@/api/services'

const employees = ref([])
const roles = ref([])
const isLoading = ref(false)
const showModal = ref(false)
const showDeleteModal = ref(false)
const editingEmployee = ref(null)
const employeeToDelete = ref(null)
const isSaving = ref(false)
const isDeleting = ref(false)
const error = ref('')

const form = ref({
  name: '',
  login: '',
  password: '',
  role_id: ''
})

onMounted(async () => {
  await Promise.all([loadEmployees(), loadRoles()])
})

const loadEmployees = async () => {
  try {
    isLoading.value = true
    const response = await adminEmployeesService.getAll()
    employees.value = response.data
  } catch (err) {
    console.error('Error loading employees:', err)
  } finally {
    isLoading.value = false
  }
}

const loadRoles = async () => {
  try {
    const response = await adminRolesService.getAll()
    roles.value = response.data
  } catch (err) {
    console.error('Error loading roles:', err)
  }
}

const openCreateModal = () => {
  editingEmployee.value = null
  form.value = {
    name: '',
    login: '',
    password: '',
    role_id: ''
  }
  error.value = ''
  showModal.value = true
}

const openEditModal = (employee) => {
  editingEmployee.value = employee
  form.value = {
    name: employee.name,
    login: employee.login,
    password: '',
    role_id: employee.role_id
  }
  error.value = ''
  showModal.value = true
}

const saveEmployee = async () => {
  try {
    isSaving.value = true
    error.value = ''

    const data = editingEmployee.value
      ? { name: form.value.name, role_id: form.value.role_id }
      : form.value

    if (editingEmployee.value) {
      await adminEmployeesService.update(editingEmployee.value.id, data)
    } else {
      await adminEmployeesService.create(data)
    }

    showModal.value = false
    await loadEmployees()
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка сохранения'
  } finally {
    isSaving.value = false
  }
}

const confirmDelete = (employee) => {
  employeeToDelete.value = employee
  showDeleteModal.value = true
}

const deleteEmployee = async () => {
  try {
    isDeleting.value = true
    await adminEmployeesService.delete(employeeToDelete.value.id)
    showDeleteModal.value = false
    await loadEmployees()
  } catch (err) {
    console.error('Error deleting employee:', err)
    alert('Ошибка удаления сотрудника')
  } finally {
    isDeleting.value = false
  }
}
</script>
