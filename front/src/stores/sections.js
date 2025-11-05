import { defineStore } from 'pinia'
import { ref } from 'vue'
import { sectionsService } from '@/api/services'

export const useSectionsStore = defineStore('sections', () => {
  const sections = ref([])
  const currentSection = ref(null)
  const isLoading = ref(false)
  const error = ref(null)

  const fetchSections = async (filters = {}) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await sectionsService.getAll(filters)
      sections.value = response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка загрузки секций'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const fetchSectionById = async (id) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await sectionsService.getById(id)
      currentSection.value = response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка загрузки секции'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  return {
    sections,
    currentSection,
    isLoading,
    error,
    fetchSections,
    fetchSectionById,
  }
})
