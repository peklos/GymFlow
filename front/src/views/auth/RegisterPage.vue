<template>
  <MainLayout>
    <div class="min-h-[80vh] flex items-center justify-center px-4 py-12">
      <div class="max-w-2xl w-full">
        <!-- Header -->
        <div class="text-center mb-8">
          <div class="w-20 h-20 bg-gradient-to-br from-accent-500 to-primary-500 rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-glow-accent">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
            </svg>
          </div>
          <h1 class="text-3xl font-bold gradient-text mb-2">Регистрация</h1>
          <p class="text-slate-600">Создайте аккаунт и начните тренироваться</p>
        </div>

        <!-- Register Form -->
        <div class="card">
          <form @submit.prevent="handleRegister" class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <!-- User Info -->
              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">
                  Email *
                </label>
                <input
                  v-model="form.email"
                  type="email"
                  required
                  placeholder="your@email.com"
                  class="input"
                />
              </div>

              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">
                  Пароль *
                </label>
                <input
                  v-model="form.password"
                  type="password"
                  required
                  minlength="6"
                  placeholder="Минимум 6 символов"
                  class="input"
                />
              </div>
            </div>

            <!-- Client Info -->
            <div class="border-t border-slate-200 pt-6">
              <h3 class="font-bold text-slate-800 mb-4">Персональные данные</h3>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                  <label class="block text-sm font-semibold text-slate-700 mb-2">
                    Фамилия *
                  </label>
                  <input
                    v-model="form.last_name"
                    type="text"
                    required
                    placeholder="Иванов"
                    class="input"
                  />
                </div>

                <div>
                  <label class="block text-sm font-semibold text-slate-700 mb-2">
                    Имя *
                  </label>
                  <input
                    v-model="form.first_name"
                    type="text"
                    required
                    placeholder="Иван"
                    class="input"
                  />
                </div>

                <div>
                  <label class="block text-sm font-semibold text-slate-700 mb-2">
                    Отчество
                  </label>
                  <input
                    v-model="form.patronymic"
                    type="text"
                    placeholder="Иванович"
                    class="input"
                  />
                </div>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">
                  Дата рождения *
                </label>
                <input
                  v-model="form.birth_date"
                  type="date"
                  required
                  class="input"
                />
              </div>

              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">
                  Телефон *
                </label>
                <input
                  v-model="form.phone_number"
                  type="tel"
                  required
                  placeholder="+7 (999) 123-45-67"
                  class="input"
                />
              </div>
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">
                Пол *
              </label>
              <select v-model="form.gender" required class="input">
                <option value="">Выберите пол</option>
                <option value="Мужской">Мужской</option>
                <option value="Женский">Женский</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">
                Адрес
              </label>
              <input
                v-model="form.address"
                type="text"
                placeholder="Город, улица, дом"
                class="input"
              />
            </div>

            <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg">
              <p class="text-red-700 text-sm">{{ error }}</p>
            </div>

            <button
              type="submit"
              :disabled="isLoading"
              class="btn btn-primary w-full text-lg py-4"
            >
              {{ isLoading ? 'Регистрация...' : 'Зарегистрироваться' }}
            </button>
          </form>

          <div class="mt-6 text-center">
            <p class="text-slate-600">
              Уже есть аккаунт?
              <router-link to="/login" class="text-primary-600 hover:text-primary-700 font-semibold">
                Войти
              </router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import MainLayout from '@/components/layout/MainLayout.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const form = ref({
  email: '',
  password: '',
  first_name: '',
  last_name: '',
  patronymic: '',
  birth_date: '',
  phone_number: '',
  gender: '',
  address: ''
})

const error = ref('')
const isLoading = ref(false)

const handleRegister = async () => {
  try {
    isLoading.value = true
    error.value = ''

    await authStore.register(form.value)

    router.push('/')
  } catch (err) {
    error.value = err.response?.data?.detail || 'Ошибка регистрации. Попробуйте снова.'
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
</style>
