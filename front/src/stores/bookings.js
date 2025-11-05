import { defineStore } from 'pinia'
import { ref } from 'vue'
import { bookingsService } from '@/api/services'

export const useBookingsStore = defineStore('bookings', () => {
  const bookings = ref([])
  const isLoading = ref(false)
  const error = ref(null)

  const fetchClientBookings = async (clientId) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await bookingsService.getByClient(clientId)
      bookings.value = response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка загрузки бронирований'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const createBooking = async (bookingData) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await bookingsService.create(bookingData)
      bookings.value.push(response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка создания бронирования'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const cancelBooking = async (bookingId) => {
    isLoading.value = true
    error.value = null
    try {
      await bookingsService.cancel(bookingId)
      bookings.value = bookings.value.filter(b => b.id !== bookingId)
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка отмены бронирования'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  return {
    bookings,
    isLoading,
    error,
    fetchClientBookings,
    createBooking,
    cancelBooking,
  }
})
