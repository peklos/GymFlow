<template>
  <MainLayout>
    <!-- Hero Section -->
    <section class="relative overflow-hidden py-20 lg:py-32">
      <div class="absolute inset-0 bg-gradient-to-br from-primary-500/10 via-accent-500/10 to-purple-500/10"></div>

      <div class="container mx-auto px-4 relative z-10">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-5xl lg:text-7xl font-black mb-6 animate-float">
            <span class="gradient-text">GymFlow</span>
          </h1>
          <p class="text-xl lg:text-2xl text-slate-700 mb-8 font-medium">
            Твой путь к идеальной форме начинается здесь
          </p>
          <p class="text-lg text-slate-600 mb-12 max-w-2xl mx-auto">
            Современная система управления тренировками. Выбирай секции, бронируй занятия и достигай своих целей!
          </p>

          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link to="/sections" class="btn btn-primary text-lg px-8 py-4">
              Выбрать секцию
            </router-link>
            <router-link to="/schedule" class="btn btn-secondary text-lg px-8 py-4">
              Смотреть расписание
            </router-link>
          </div>
        </div>
      </div>

      <!-- Decorative Elements -->
      <div class="absolute top-20 left-10 w-72 h-72 bg-primary-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float"></div>
      <div class="absolute bottom-20 right-10 w-72 h-72 bg-accent-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float" style="animation-delay: 1s;"></div>
    </section>

    <!-- Features Section -->
    <section class="py-20 container mx-auto px-4">
      <h2 class="text-4xl font-bold text-center mb-4">
        <span class="gradient-text">Почему GymFlow?</span>
      </h2>
      <p class="text-center text-slate-600 mb-12 max-w-2xl mx-auto">
        Мы предлагаем лучшие условия для ваших тренировок
      </p>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="card text-center group hover:shadow-glow">
          <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-3 text-slate-800">Разнообразие программ</h3>
          <p class="text-slate-600">
            Более 10 различных секций: от фитнеса до единоборств
          </p>
        </div>

        <div class="card text-center group hover:shadow-glow-accent">
          <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-3 text-slate-800">Удобное расписание</h3>
          <p class="text-slate-600">
            Гибкое расписание, подстраивающееся под ваш ритм жизни
          </p>
        </div>

        <div class="card text-center group hover:shadow-glow">
          <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-green-600 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-3 text-slate-800">Простое бронирование</h3>
          <p class="text-slate-600">
            Забронируй занятие в пару кликов через личный кабинет
          </p>
        </div>
      </div>
    </section>

    <!-- Popular Sections -->
    <section class="py-20 bg-gradient-to-br from-slate-50 to-blue-50">
      <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold text-center mb-4">
          <span class="gradient-text">Популярные секции</span>
        </h2>
        <p class="text-center text-slate-600 mb-12">
          Самые востребованные направления для тренировок
        </p>

        <div v-if="isLoading" class="flex justify-center py-12">
          <LoadingSpinner text="Загрузка секций..." />
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <SectionCard
            v-for="section in popularSections"
            :key="section.id"
            :section="section"
            @view-details="goToSection"
          />
        </div>

        <div class="text-center mt-12">
          <router-link to="/sections" class="btn btn-primary text-lg px-8 py-4">
            Все секции
          </router-link>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20">
      <div class="container mx-auto px-4">
        <div class="card bg-gradient-to-br from-primary-500 to-accent-500 text-white text-center max-w-4xl mx-auto">
          <h2 class="text-3xl lg:text-4xl font-bold mb-6">
            Готов начать свой путь?
          </h2>
          <p class="text-xl mb-8 text-white/90">
            Зарегистрируйся сейчас и получи первую тренировку бесплатно!
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link to="/register" class="btn bg-white text-primary-600 hover:bg-slate-100 text-lg px-8 py-4">
              Регистрация
            </router-link>
            <router-link to="/login" class="btn border-2 border-white text-white hover:bg-white/10 text-lg px-8 py-4">
              Войти
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import MainLayout from '@/components/layout/MainLayout.vue'
import SectionCard from '@/components/sections/SectionCard.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useSectionsStore } from '@/stores/sections'

const router = useRouter()
const sectionsStore = useSectionsStore()

const popularSections = ref([])
const isLoading = ref(false)

onMounted(async () => {
  try {
    isLoading.value = true
    await sectionsStore.fetchSections()
    // Show first 3 sections as popular
    popularSections.value = sectionsStore.sections.slice(0, 3)
  } catch (error) {
    console.error('Error loading sections:', error)
  } finally {
    isLoading.value = false
  }
})

const goToSection = (sectionId) => {
  router.push({ name: 'section-detail', params: { id: sectionId } })
}
</script>

<style scoped>
</style>
