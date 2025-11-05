<template>
  <MainLayout>
    <div class="container mx-auto px-4 py-12">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl lg:text-5xl font-bold mb-4">
          <span class="gradient-text">Наши секции</span>
        </h1>
        <p class="text-xl text-slate-600 max-w-2xl mx-auto">
          Выбери направление, которое тебе по душе
        </p>
      </div>

      <!-- Filters -->
      <div class="card mb-8 max-w-4xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Вид спорта
            </label>
            <select v-model="filters.sport_type" class="input">
              <option value="">Все виды</option>
              <option value="Фитнес">Фитнес</option>
              <option value="Йога">Йога</option>
              <option value="Бокс">Бокс</option>
              <option value="Плавание">Плавание</option>
              <option value="Танцы">Танцы</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Возраст от
            </label>
            <input
              v-model.number="filters.age_from"
              type="number"
              placeholder="От"
              class="input"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Возраст до
            </label>
            <input
              v-model.number="filters.age_to"
              type="number"
              placeholder="До"
              class="input"
            />
          </div>
        </div>

        <div class="flex items-center gap-4 mt-4">
          <label class="flex items-center space-x-2 cursor-pointer">
            <input
              v-model="filters.is_free"
              type="checkbox"
              class="w-5 h-5 rounded border-slate-300 text-primary-600 focus:ring-primary-500"
            />
            <span class="text-slate-700 font-medium">Только бесплатные</span>
          </label>

          <button
            @click="applyFilters"
            class="btn btn-primary ml-auto"
          >
            Применить фильтры
          </button>

          <button
            @click="resetFilters"
            class="btn btn-secondary"
          >
            Сбросить
          </button>
        </div>
      </div>

      <!-- Loading -->
      <LoadingSpinner v-if="isLoading" text="Загрузка секций..." />

      <!-- Sections Grid -->
      <div v-else-if="filteredSections.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <SectionCard
          v-for="section in filteredSections"
          :key="section.id"
          :section="section"
          @view-details="goToSection"
        />
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-20">
        <div class="w-32 h-32 bg-gradient-to-br from-slate-200 to-slate-300 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-16 h-16 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M12 12h.01M12 12h.01M12 12h.01M12 12h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-slate-800 mb-2">Секции не найдены</h3>
        <p class="text-slate-600 mb-6">Попробуйте изменить параметры поиска</p>
        <button @click="resetFilters" class="btn btn-primary">
          Сбросить фильтры
        </button>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import MainLayout from '@/components/layout/MainLayout.vue'
import SectionCard from '@/components/sections/SectionCard.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useSectionsStore } from '@/stores/sections'

const router = useRouter()
const sectionsStore = useSectionsStore()

const isLoading = ref(false)
const filters = ref({
  sport_type: '',
  age_from: null,
  age_to: null,
  is_free: false
})

const filteredSections = computed(() => {
  let sections = sectionsStore.sections

  if (filters.value.sport_type) {
    sections = sections.filter(s => s.sport_type === filters.value.sport_type)
  }

  if (filters.value.age_from) {
    sections = sections.filter(s => s.age_to >= filters.value.age_from)
  }

  if (filters.value.age_to) {
    sections = sections.filter(s => s.age_from <= filters.value.age_to)
  }

  if (filters.value.is_free) {
    sections = sections.filter(s => s.is_free)
  }

  return sections
})

onMounted(async () => {
  await loadSections()
})

const loadSections = async () => {
  try {
    isLoading.value = true
    await sectionsStore.fetchSections()
  } catch (error) {
    console.error('Error loading sections:', error)
  } finally {
    isLoading.value = false
  }
}

const applyFilters = async () => {
  await loadSections()
}

const resetFilters = async () => {
  filters.value = {
    sport_type: '',
    age_from: null,
    age_to: null,
    is_free: false
  }
  await loadSections()
}

const goToSection = (sectionId) => {
  router.push({ name: 'section-detail', params: { id: sectionId } })
}
</script>

<style scoped>
</style>
