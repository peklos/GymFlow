<template>
  <MainLayout>
    <!-- Hero Section -->
    <section class="relative overflow-hidden py-20 lg:py-32">
      <div class="absolute inset-0 bg-gradient-to-br from-primary-500/10 via-accent-500/10 to-purple-500/10"></div>

      <div class="container mx-auto px-4 relative z-10">
        <div class="grid lg:grid-cols-2 gap-12 items-center max-w-7xl mx-auto">
          <!-- Text Content -->
          <div class="text-center lg:text-left">
            <h1 class="text-5xl lg:text-7xl font-black mb-6 animate-float">
              <span class="gradient-text">GymFlow</span>
            </h1>
            <p class="text-xl lg:text-2xl text-slate-700 mb-8 font-medium">
              Твой путь к идеальной форме начинается здесь
            </p>
            <p class="text-lg text-slate-600 mb-12">
              Современная система управления тренировками. Выбирай секции, бронируй занятия и достигай своих целей!
            </p>

            <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <router-link to="/sections" class="btn btn-primary text-lg px-8 py-4">
                Выбрать секцию
              </router-link>
              <router-link to="/schedule" class="btn btn-secondary text-lg px-8 py-4">
                Смотреть расписание
              </router-link>
            </div>
          </div>

          <!-- Hero Illustration -->
          <div class="hidden lg:block relative">
            <svg viewBox="0 0 500 500" class="w-full h-auto animate-float" style="animation-duration: 4s;">
              <!-- Yoga Person -->
              <g>
                <circle cx="150" cy="80" r="25" fill="#6366F1" opacity="0.2"/>
                <circle cx="150" cy="80" r="18" fill="#6366F1"/>
                <rect x="135" y="100" width="30" height="45" rx="8" fill="#818CF8"/>
                <rect x="125" y="110" width="15" height="35" rx="6" fill="#A5B4FC"/>
                <rect x="160" y="110" width="15" height="35" rx="6" fill="#A5B4FC"/>
                <rect x="142" y="145" width="16" height="40" rx="6" fill="#C7D2FE"/>
                <rect x="142" y="185" width="16" height="35" rx="6" fill="#DDD6FE"/>
              </g>

              <!-- Fitness Person -->
              <g transform="translate(250, 50)">
                <circle cx="50" cy="40" r="25" fill="#8B5CF6" opacity="0.2"/>
                <circle cx="50" cy="40" r="18" fill="#8B5CF6"/>
                <rect x="35" y="60" width="30" height="50" rx="8" fill="#A78BFA"/>
                <rect x="20" y="65" width="15" height="40" rx="6" fill="#C4B5FD" transform="rotate(-45 27.5 85)"/>
                <rect x="65" y="65" width="15" height="40" rx="6" fill="#C4B5FD" transform="rotate(45 72.5 85)"/>
                <rect x="42" y="110" width="16" height="45" rx="6" fill="#DDD6FE"/>
              </g>

              <!-- Dumbbell Left -->
              <g transform="translate(80, 300)">
                <rect x="0" y="20" width="50" height="8" rx="4" fill="#4F46E5"/>
                <circle cx="0" cy="24" r="14" fill="#6366F1"/>
                <circle cx="50" cy="24" r="14" fill="#6366F1"/>
              </g>

              <!-- Dumbbell Right -->
              <g transform="translate(370, 350)">
                <rect x="0" y="20" width="50" height="8" rx="4" fill="#7C3AED"/>
                <circle cx="0" cy="24" r="14" fill="#8B5CF6"/>
                <circle cx="50" cy="24" r="14" fill="#8B5CF6"/>
              </g>

              <!-- Yoga Mat -->
              <rect x="100" y="420" width="120" height="15" rx="7" fill="#A5B4FC" opacity="0.6"/>

              <!-- Energy Circles -->
              <circle cx="400" cy="100" r="30" fill="#F472B6" opacity="0.3"/>
              <circle cx="420" cy="120" r="20" fill="#EC4899" opacity="0.4"/>

              <circle cx="50" cy="200" r="25" fill="#60A5FA" opacity="0.3"/>
              <circle cx="70" cy="180" r="15" fill="#3B82F6" opacity="0.4"/>

              <!-- Trophy Icon -->
              <g transform="translate(350, 380)">
                <path d="M30 10 L40 10 L38 25 L32 25 Z" fill="#FBBF24" stroke="#F59E0B" stroke-width="2"/>
                <rect x="33" y="25" width="4" height="8" fill="#F59E0B"/>
                <ellipse cx="35" cy="35" rx="10" ry="3" fill="#F59E0B"/>
                <circle cx="35" cy="5" r="4" fill="#FCD34D"/>
              </g>

              <!-- Stars -->
              <path d="M 200 120 L 204 128 L 212 128 L 206 134 L 208 142 L 200 137 L 192 142 L 194 134 L 188 128 L 196 128 Z" fill="#FDE047"/>
              <path d="M 450 250 L 454 258 L 462 258 L 456 264 L 458 272 L 450 267 L 442 272 L 444 264 L 438 258 L 446 258 Z" fill="#FDE047" opacity="0.7"/>
              <path d="M 50 420 L 54 428 L 62 428 L 56 434 L 58 442 L 50 437 L 42 442 L 44 434 L 38 428 L 46 428 Z" fill="#FDE047" opacity="0.5"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Decorative Elements -->
      <div class="absolute top-20 left-10 w-72 h-72 bg-primary-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float"></div>
      <div class="absolute bottom-20 right-10 w-72 h-72 bg-accent-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float" style="animation-delay: 1s;"></div>
      <div class="absolute top-1/2 left-1/2 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-float" style="animation-delay: 0.5s;"></div>
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
    <section class="py-20 bg-gradient-to-br from-slate-50 to-blue-50 relative overflow-hidden">
      <!-- Background Pattern -->
      <div class="absolute inset-0 opacity-5">
        <svg class="w-full h-full" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern id="fitness-pattern" x="0" y="0" width="100" height="100" patternUnits="userSpaceOnUse">
              <circle cx="50" cy="50" r="30" stroke="#6366F1" stroke-width="2" fill="none"/>
              <path d="M30 50 L70 50 M50 30 L50 70" stroke="#8B5CF6" stroke-width="2"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#fitness-pattern)"/>
        </svg>
      </div>

      <div class="container mx-auto px-4 relative z-10">
        <h2 class="text-4xl font-bold text-center mb-4">
          <span class="gradient-text">Популярные секции</span>
        </h2>
        <p class="text-center mb-12" style="color: #475569 !important;">
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

    <!-- CTA Section - Only show for non-authenticated users -->
    <section v-if="!authStore.isAuthenticated" class="py-20 relative overflow-hidden">
      <div class="container mx-auto px-4">
        <div class="card bg-gradient-to-br from-primary-500 to-accent-500 text-white text-center max-w-5xl mx-auto relative overflow-hidden">
          <!-- Background Pattern -->
          <div class="absolute inset-0 opacity-10">
            <svg class="w-full h-full" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="dots" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
                  <circle cx="20" cy="20" r="2" fill="white"/>
                </pattern>
              </defs>
              <rect width="100%" height="100%" fill="url(#dots)"/>
            </svg>
          </div>

          <!-- Decorative Icons -->
          <div class="absolute top-10 left-10 opacity-20">
            <svg width="80" height="80" viewBox="0 0 80 80" fill="none">
              <circle cx="40" cy="40" r="35" stroke="white" stroke-width="3"/>
              <path d="M40 20 L40 60 M50 30 L40 20 L30 30" stroke="white" stroke-width="3" stroke-linecap="round"/>
            </svg>
          </div>

          <div class="absolute bottom-10 right-10 opacity-20">
            <svg width="70" height="70" viewBox="0 0 70 70" fill="none">
              <polygon points="35,10 50,30 60,25 50,45 60,60 35,50 10,60 20,45 10,25 20,30" fill="white"/>
            </svg>
          </div>

          <!-- Content -->
          <div class="relative z-10">
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
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const sectionsStore = useSectionsStore()
const authStore = useAuthStore()

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
