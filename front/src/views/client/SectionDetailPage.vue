<template>
  <MainLayout>
    <div class="container mx-auto px-4 py-12">
      <LoadingSpinner v-if="isLoading" text="Загрузка информации о секции..." />

      <div v-else-if="section" class="max-w-4xl mx-auto">
        <!-- Back Button -->
        <button @click="$router.back()" class="btn btn-secondary mb-6">
          <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          Назад
        </button>

        <!-- Section Header -->
        <div class="card mb-8">
          <div class="flex items-start justify-between">
            <div class="flex-1">
              <h1 class="text-4xl font-bold gradient-text mb-4">
                {{ section.name }}
              </h1>
              <div class="flex flex-wrap gap-2 mb-4">
                <span class="badge badge-info text-base px-4 py-2">{{ section.sport_type }}</span>
                <span v-if="section.is_free" class="badge badge-success text-base px-4 py-2">Бесплатно</span>
              </div>
            </div>
            <div class="w-20 h-20 bg-gradient-to-br from-primary-100 to-accent-100 rounded-2xl flex items-center justify-center">
              <svg class="w-10 h-10 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
          </div>

          <div class="border-t border-slate-200 mt-6 pt-6">
            <h2 class="text-xl font-bold text-slate-800 mb-3">Описание</h2>
            <p class="text-slate-600 text-lg leading-relaxed">
              {{ section.description }}
            </p>
          </div>

          <div class="border-t border-slate-200 mt-6 pt-6">
            <h2 class="text-xl font-bold text-slate-800 mb-4">Информация</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                  <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                  </svg>
                </div>
                <div>
                  <p class="text-sm text-slate-500">Возрастная группа</p>
                  <p class="text-lg font-semibold text-slate-800">{{ section.age_from }}-{{ section.age_to }} лет</p>
                </div>
              </div>

              <div class="flex items-center gap-3">
                <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                  <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div>
                  <p class="text-sm text-slate-500">Стоимость</p>
                  <p class="text-lg font-semibold text-slate-800">
                    {{ section.is_free ? 'Бесплатно' : 'По абонементу' }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="card bg-gradient-to-br from-primary-50 to-accent-50 border-2 border-primary-200">
          <h2 class="text-2xl font-bold text-slate-800 mb-4">Готов записаться?</h2>
          <p class="text-slate-600 mb-6">
            Посмотри расписание занятий и выбери удобное время для тренировки
          </p>
          <div class="flex flex-col sm:flex-row gap-4">
            <router-link
              :to="{ name: 'schedule', query: { section_id: section.id } }"
              class="btn btn-primary"
            >
              Посмотреть расписание
            </router-link>
            <router-link to="/sections" class="btn btn-secondary">
              Другие секции
            </router-link>
          </div>
        </div>
      </div>

      <!-- Error State -->
      <div v-else class="text-center py-20">
        <div class="w-32 h-32 bg-gradient-to-br from-red-200 to-red-300 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-16 h-16 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-slate-800 mb-2">Секция не найдена</h3>
        <p class="text-slate-600 mb-6">Возможно, она была удалена или не существует</p>
        <router-link to="/sections" class="btn btn-primary">
          Все секции
        </router-link>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import MainLayout from '@/components/layout/MainLayout.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useSectionsStore } from '@/stores/sections'

const route = useRoute()
const sectionsStore = useSectionsStore()

const section = ref(null)
const isLoading = ref(false)

onMounted(async () => {
  try {
    isLoading.value = true
    const sectionId = parseInt(route.params.id)
    await sectionsStore.fetchSectionById(sectionId)
    section.value = sectionsStore.currentSection
  } catch (error) {
    console.error('Error loading section:', error)
  } finally {
    isLoading.value = false
  }
})
</script>

<style scoped>
</style>
