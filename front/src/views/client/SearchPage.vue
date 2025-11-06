<template>
  <MainLayout>
    <div class="container mx-auto px-4 py-12">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="gradient-text">🔍 Поиск</span>
        </h1>
        <p class="text-slate-600 text-lg">
          Найдите нужный раздел или функцию быстро и легко
        </p>
      </div>

      <!-- Search Input -->
      <div class="max-w-2xl mx-auto mb-12">
        <div class="relative">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Введите что ищете... (например, 'записаться', 'расписание', 'профиль')"
            class="w-full px-6 py-4 pr-12 text-lg rounded-2xl border-2 border-slate-300 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
          />
          <svg
            class="absolute right-5 top-1/2 -translate-y-1/2 w-6 h-6 text-slate-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </div>
      </div>

      <!-- Results Count -->
      <div v-if="searchQuery" class="max-w-6xl mx-auto mb-6">
        <p class="text-slate-600">
          Найдено результатов: <strong class="text-primary-600">{{ filteredActions.length }}</strong>
        </p>
      </div>

      <!-- Action Cards Grid -->
      <div class="max-w-6xl mx-auto">
        <div v-if="filteredActions.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="action in filteredActions"
            :key="action.id"
            class="card group hover:shadow-xl transition-all duration-300 cursor-pointer"
            @click="handleActionClick(action)"
          >
            <!-- Icon -->
            <div
              class="w-16 h-16 rounded-2xl flex items-center justify-center mx-auto mb-4 text-3xl transition-transform group-hover:scale-110"
              :class="action.colorClass"
            >
              {{ action.icon }}
            </div>

            <!-- Title -->
            <h3 class="text-xl font-bold text-center mb-3 text-black">
              {{ action.title }}
            </h3>

            <!-- Description -->
            <p class="text-slate-600 text-center mb-4">
              {{ action.description }}
            </p>

            <!-- Tags -->
            <div class="flex flex-wrap gap-2 justify-center">
              <span
                v-for="tag in action.tags"
                :key="tag"
                class="px-3 py-1 bg-slate-100 text-slate-600 rounded-full text-xs font-medium"
              >
                {{ tag }}
              </span>
            </div>

            <!-- Arrow Icon -->
            <div class="mt-4 text-center">
              <svg
                class="w-6 h-6 mx-auto text-primary-500 transform group-hover:translate-x-1 transition-transform"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 7l5 5m0 0l-5 5m5-5H6"
                />
              </svg>
            </div>
          </div>
        </div>

        <!-- No Results -->
        <div v-else class="text-center py-16">
          <div class="w-24 h-24 bg-slate-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-12 h-12 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-slate-800 mb-3">Ничего не найдено</h3>
          <p class="text-slate-600 text-lg">
            Попробуйте изменить поисковый запрос или очистите поле для просмотра всех разделов
          </p>
        </div>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import MainLayout from '@/components/layout/MainLayout.vue'

const router = useRouter()
const authStore = useAuthStore()
const searchQuery = ref('')

// Define all available actions
const actions = ref([
  {
    id: 1,
    title: 'Посмотреть секции',
    description: 'Просмотр всех доступных секций и программ тренировок',
    icon: '🏋️',
    colorClass: 'bg-gradient-to-br from-blue-500 to-blue-600 text-white',
    route: { name: 'sections' },
    tags: ['секции', 'тренировки', 'программы', 'фитнес'],
    keywords: ['секции', 'секция', 'программы', 'программа', 'тренировки', 'тренировка', 'занятия', 'занятие', 'фитнес', 'спорт']
  },
  {
    id: 2,
    title: 'Посмотреть расписание',
    description: 'Расписание всех занятий на неделю с временем и тренерами',
    icon: '📅',
    colorClass: 'bg-gradient-to-br from-purple-500 to-purple-600 text-white',
    route: { name: 'schedule' },
    tags: ['расписание', 'время', 'занятия', 'тренеры'],
    keywords: ['расписание', 'график', 'время', 'когда', 'занятия', 'занятие', 'тренеры', 'тренер']
  },
  {
    id: 3,
    title: 'Записаться на занятие',
    description: 'Забронировать место на тренировку в удобное время',
    icon: '✅',
    colorClass: 'bg-gradient-to-br from-green-500 to-green-600 text-white',
    route: { name: 'schedule' },
    tags: ['бронирование', 'запись', 'занятия'],
    keywords: ['записаться', 'забронировать', 'бронирование', 'запись', 'запи', 'записать', 'занятие', 'занятия', 'тренировка', 'тренировки']
  },
  {
    id: 4,
    title: 'Мои бронирования',
    description: 'Просмотр и управление вашими забронированными занятиями',
    icon: '📋',
    colorClass: 'bg-gradient-to-br from-indigo-500 to-indigo-600 text-white',
    route: { name: 'bookings' },
    tags: ['бронирования', 'мои занятия', 'записи'],
    keywords: ['бронирования', 'бронирование', 'мои', 'записи', 'запись', 'занятия', 'мои занятия', 'забронированные']
  },
  {
    id: 5,
    title: 'Мой профиль',
    description: 'Просмотр и редактирование личных данных и настроек',
    icon: '👤',
    colorClass: 'bg-gradient-to-br from-teal-500 to-teal-600 text-white',
    route: { name: 'profile' },
    tags: ['профиль', 'настройки', 'данные', 'личный кабинет'],
    keywords: ['профиль', 'личные данные', 'настройки', 'кабинет', 'личный', 'данные', 'информация', 'аккаунт']
  },
  {
    id: 6,
    title: 'Выйти из аккаунта',
    description: 'Безопасный выход из вашего личного кабинета',
    icon: '🚪',
    colorClass: 'bg-gradient-to-br from-red-500 to-red-600 text-white',
    action: 'logout',
    tags: ['выход', 'выйти', 'безопасность'],
    keywords: ['выйти', 'выход', 'logout', 'разлогиниться', 'выход из системы']
  },
  {
    id: 7,
    title: 'Посмотреть тренеров',
    description: 'Информация о всех тренерах и их специализациях',
    icon: '👨‍🏫',
    colorClass: 'bg-gradient-to-br from-orange-500 to-orange-600 text-white',
    route: { name: 'sections' },
    tags: ['тренеры', 'инструкторы', 'специалисты'],
    keywords: ['тренеры', 'тренер', 'инструкторы', 'инструктор', 'специалисты', 'кто ведет', 'преподаватели']
  },
  {
    id: 8,
    title: 'Главная страница',
    description: 'Вернуться на главную страницу сайта',
    icon: '🏠',
    colorClass: 'bg-gradient-to-br from-pink-500 to-pink-600 text-white',
    route: { name: 'home' },
    tags: ['главная', 'домой', 'начало'],
    keywords: ['главная', 'домой', 'начало', 'home', 'главная страница', 'стартовая']
  },
  {
    id: 9,
    title: 'Справочник',
    description: 'Подробная инструкция по использованию сайта',
    icon: '📖',
    colorClass: 'bg-gradient-to-br from-amber-500 to-amber-600 text-white',
    action: 'handbook',
    tags: ['справочник', 'помощь', 'инструкция', 'гид'],
    keywords: ['справочник', 'помощь', 'инструкция', 'как пользоваться', 'руководство', 'гид', 'help']
  }
])

// Filter actions based on search query
const filteredActions = computed(() => {
  if (!searchQuery.value.trim()) {
    return actions.value
  }

  const query = searchQuery.value.toLowerCase().trim()

  return actions.value.filter(action => {
    // Search in title
    if (action.title.toLowerCase().includes(query)) {
      return true
    }

    // Search in description
    if (action.description.toLowerCase().includes(query)) {
      return true
    }

    // Search in tags
    if (action.tags.some(tag => tag.toLowerCase().includes(query))) {
      return true
    }

    // Search in keywords
    if (action.keywords.some(keyword => keyword.toLowerCase().includes(query))) {
      return true
    }

    return false
  })
})

// Handle action click
const handleActionClick = (action) => {
  if (action.route) {
    router.push(action.route)
  } else if (action.action === 'logout') {
    handleLogout()
  } else if (action.action === 'handbook') {
    // Navigate to home and open handbook
    router.push({ name: 'home', query: { showHandbook: 'true' } })
  }
}

// Handle logout
const handleLogout = async () => {
  try {
    await authStore.logout()
    router.push({ name: 'login' })
  } catch (error) {
    console.error('Logout error:', error)
  }
}
</script>

<style scoped>
.gradient-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
</style>
