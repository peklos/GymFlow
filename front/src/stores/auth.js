import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authService, adminAuthService } from '@/api/services'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const employee = ref(null)
  const isLoading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => !!user.value)
  const isAdmin = computed(() => !!employee.value)
  const currentUser = computed(() => user.value || employee.value)

  // Load from localStorage
  const loadFromStorage = () => {
    const savedUser = localStorage.getItem('user')
    const savedEmployee = localStorage.getItem('employee')

    if (savedUser) {
      user.value = JSON.parse(savedUser)
    }
    if (savedEmployee) {
      employee.value = JSON.parse(savedEmployee)
    }
  }

  // Client Auth
  const login = async (credentials) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await authService.login(credentials)
      user.value = response.data
      localStorage.setItem('user', JSON.stringify(response.data))
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка входа'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const register = async (userData) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await authService.register(userData)
      user.value = response.data
      localStorage.setItem('user', JSON.stringify(response.data))
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка регистрации'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  // Admin Auth
  const adminLogin = async (credentials) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await adminAuthService.login(credentials)
      employee.value = response.data
      localStorage.setItem('employee', JSON.stringify(response.data))
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка входа администратора'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const logout = () => {
    user.value = null
    employee.value = null
    localStorage.removeItem('user')
    localStorage.removeItem('employee')
  }

  // Initialize
  loadFromStorage()

  return {
    user,
    employee,
    isLoading,
    error,
    isAuthenticated,
    isAdmin,
    currentUser,
    login,
    register,
    adminLogin,
    logout,
  }
})
