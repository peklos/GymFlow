<template>
  <MainLayout>
    <div class="container mx-auto px-4 py-12">
      <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <div class="mb-8">
          <h1 class="text-4xl font-bold gradient-text mb-2">Мой профиль</h1>
          <p class="text-slate-600">Управляйте своими данными</p>
        </div>

        <LoadingSpinner v-if="isLoading" text="Загрузка профиля..." />

        <div v-else-if="profile" class="space-y-6">
          <!-- Profile Info Card -->
          <div class="card">
            <div class="flex items-center justify-between mb-6">
              <h2 class="text-2xl font-bold text-slate-800">Личная информация</h2>
              <button
                v-if="!isEditing"
                @click="startEditing"
                class="btn btn-primary"
              >
                Редактировать
              </button>
            </div>

            <form v-if="isEditing" @submit.prevent="saveProfile" class="space-y-6">
              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">
                  ФИО *
                </label>
                <input
                  v-model="editForm.full_name"
                  type="text"
                  required
                  class="input"
                  placeholder="Иванов Иван Иванович"
                />
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-semibold text-slate-700 mb-2">
                    Дата рождения
                  </label>
                  <input
                    v-model="editForm.date_of_birth"
                    type="date"
                    class="input"
                  />
                </div>

                <div>
                  <label class="block text-sm font-semibold text-slate-700 mb-2">
                    Телефон *
                  </label>
                  <input
                    v-model="editForm.phone"
                    type="tel"
                    required
                    class="input"
                  />
                </div>
              </div>

              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">
                  Email *
                </label>
                <input
                  v-model="editForm.email"
                  type="email"
                  required
                  class="input"
                />
              </div>

              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">
                  Адрес
                </label>
                <input
                  v-model="editForm.address"
                  type="text"
                  class="input"
                />
              </div>

              <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
                {{ error }}
              </div>

              <div class="flex gap-4">
                <button
                  type="submit"
                  :disabled="isSaving"
                  class="btn btn-primary"
                >
                  {{ isSaving ? 'Сохранение...' : 'Сохранить' }}
                </button>
                <button
                  type="button"
                  @click="cancelEditing"
                  class="btn btn-secondary"
                >
                  Отмена
                </button>
              </div>
            </form>

            <div v-else class="space-y-4">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <p class="text-sm text-slate-500 mb-1">ФИО</p>
                  <p class="text-lg font-semibold text-slate-800">
                    {{ profile.full_name || 'Не указано' }}
                  </p>
                </div>

                <div>
                  <p class="text-sm text-slate-500 mb-1">Дата рождения</p>
                  <p class="text-lg font-semibold text-slate-800">
                    {{ formatDate(profile.date_of_birth) }}
                  </p>
                </div>

                <div>
                  <p class="text-sm text-slate-500 mb-1">Телефон</p>
                  <p class="text-lg font-semibold text-slate-800">
                    {{ profile.phone || 'Не указано' }}
                  </p>
                </div>

                <div>
                  <p class="text-sm text-slate-500 mb-1">Email</p>
                  <p class="text-lg font-semibold text-slate-800">
                    {{ profile.email || 'Не указано' }}
                  </p>
                </div>

                <div v-if="profile.address" class="md:col-span-2">
                  <p class="text-sm text-slate-500 mb-1">Адрес</p>
                  <p class="text-lg font-semibold text-slate-800">
                    {{ profile.address }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Account Info Card -->
          <div class="card">
            <h2 class="text-2xl font-bold text-slate-800 mb-6">Данные аккаунта</h2>
            <div class="space-y-4">
              <div>
                <p class="text-sm text-slate-500 mb-1">Email</p>
                <p class="text-lg font-semibold text-slate-800">
                  {{ authStore.user?.email }}
                </p>
              </div>
              <div>
                <p class="text-sm text-slate-500 mb-1">ID клиента</p>
                <p class="text-lg font-semibold text-slate-800">
                  {{ profile.id }}
                </p>
              </div>
            </div>
          </div>

          <!-- Quick Actions -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <router-link to="/bookings" class="card card-hover text-center">
              <svg class="w-12 h-12 mx-auto mb-4 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              <h3 class="text-xl font-bold text-slate-800 mb-2">Мои бронирования</h3>
              <p class="text-slate-600">Просмотр и управление записями</p>
            </router-link>

            <router-link to="/schedule" class="card card-hover text-center">
              <svg class="w-12 h-12 mx-auto mb-4 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              <h3 class="text-xl font-bold text-slate-800 mb-2">Записаться</h3>
              <p class="text-slate-600">Забронировать новое занятие</p>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MainLayout from '@/components/layout/MainLayout.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { profileService } from '@/api/services'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const profile = ref(null)
const isLoading = ref(false)
const isEditing = ref(false)
const isSaving = ref(false)
const error = ref('')
const editForm = ref({})

onMounted(async () => {
  await loadProfile()
})

const loadProfile = async () => {
  try {
    isLoading.value = true
    const response = await profileService.getProfile(authStore.user.client_id)
    profile.value = response.data
  } catch (err) {
    console.error('Error loading profile:', err)
  } finally {
    isLoading.value = false
  }
}

const startEditing = () => {
  editForm.value = { ...profile.value }
  isEditing.value = true
  error.value = ''
}

const cancelEditing = () => {
  isEditing.value = false
  editForm.value = {}
  error.value = ''
}

const saveProfile = async () => {
  try {
    isSaving.value = true
    error.value = ''

    await profileService.updateProfile(profile.value.id, editForm.value)
    profile.value = { ...editForm.value }
    isEditing.value = false
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка сохранения профиля'
  } finally {
    isSaving.value = false
  }
}

const formatDate = (dateString) => {
  if (!dateString) return 'Не указано'
  const date = new Date(dateString)
  if (isNaN(date.getTime())) return 'Не указано'
  return date.toLocaleDateString('ru-RU')
}
</script>

<style scoped>
</style>
