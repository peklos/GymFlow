<template>
  <MainLayout>
    <div class="min-h-[80vh] flex items-center justify-center px-4 py-12">
      <div class="max-w-md w-full">
        <!-- Header -->
        <div class="text-center mb-8">
          <div class="w-20 h-20 bg-gradient-to-br from-slate-700 to-slate-900 rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-xl">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
          </div>
          <h1 class="text-3xl font-bold text-slate-800 mb-2">Панель сотрудника</h1>
          <p class="text-slate-600">Вход для администраторов и менеджеров</p>
        </div>

        <!-- Login Form -->
        <div class="card border-2 border-slate-200">
          <form @submit.prevent="handleLogin" class="space-y-6">
            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">
                Логин сотрудника
              </label>
              <input
                v-model="form.login"
                type="text"
                required
                placeholder="admin@gym.ru"
                class="input"
                :class="{ 'input-error': error }"
              />
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">
                Пароль
              </label>
              <input
                v-model="form.password"
                type="password"
                required
                placeholder="••••••••"
                class="input"
                :class="{ 'input-error': error }"
              />
            </div>

            <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg">
              <p class="text-red-700 text-sm">{{ error }}</p>
            </div>

            <button
              type="submit"
              :disabled="isLoading"
              class="btn bg-gradient-to-r from-slate-700 to-slate-900 text-white hover:from-slate-800 hover:to-black w-full"
            >
              {{ isLoading ? 'Вход...' : 'Войти в систему' }}
            </button>
          </form>

          <div class="mt-6 pt-6 border-t border-slate-200 text-center">
            <router-link to="/login" class="text-sm text-slate-500 hover:text-slate-700">
              ← Вход для клиентов
            </router-link>
          </div>
        </div>

        <!-- Test Credentials -->
        <div class="mt-6 p-4 bg-slate-100 border border-slate-200 rounded-lg">
          <p class="text-sm font-semibold text-slate-800 mb-2">Тестовые данные:</p>
          <div class="space-y-1">
            <div class="text-sm">
              <span class="text-slate-600">Администратор:</span>
              <span class="ml-2 font-mono text-slate-800">admin@gym.ru / admin123</span>
            </div>
            <div class="text-sm">
              <span class="text-slate-600">Менеджер:</span>
              <span class="ml-2 font-mono text-slate-800">manager@gym.ru / manager123</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import MainLayout from '@/components/layout/MainLayout.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const form = ref({
  login: '',
  password: ''
})

const error = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  try {
    isLoading.value = true
    error.value = ''

    await authStore.adminLogin(form.value)

    // Redirect to admin dashboard
    const redirect = route.query.redirect || '/admin'
    router.push(redirect)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Неверный логин или пароль'
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
</style>
