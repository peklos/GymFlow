import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/client/HomePage.vue'),
      meta: { title: 'Главная' }
    },
    {
      path: '/sections',
      name: 'sections',
      component: () => import('@/views/client/SectionsPage.vue'),
      meta: { title: 'Секции' }
    },
    {
      path: '/sections/:id',
      name: 'section-detail',
      component: () => import('@/views/client/SectionDetailPage.vue'),
      meta: { title: 'Секция' }
    },
    {
      path: '/schedule',
      name: 'schedule',
      component: () => import('@/views/client/SchedulePage.vue'),
      meta: { title: 'Расписание' }
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/client/ProfilePage.vue'),
      meta: { requiresAuth: true, title: 'Профиль' }
    },
    {
      path: '/bookings',
      name: 'bookings',
      component: () => import('@/views/client/BookingsPage.vue'),
      meta: { requiresAuth: true, title: 'Мои бронирования' }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/auth/LoginPage.vue'),
      meta: { title: 'Вход' }
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/auth/RegisterPage.vue'),
      meta: { title: 'Регистрация' }
    },
    {
      path: '/admin/login',
      name: 'admin-login',
      component: () => import('@/views/auth/AdminLoginPage.vue'),
      meta: { title: 'Вход для сотрудников' }
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('@/views/admin/AdminLayout.vue'),
      meta: { requiresAdmin: true },
      children: [
        {
          path: '',
          name: 'admin-dashboard',
          component: () => import('@/views/admin/DashboardPage.vue'),
          meta: { title: 'Админ-панель' }
        },
        {
          path: 'clients',
          name: 'admin-clients',
          component: () => import('@/views/admin/ClientsPage.vue'),
          meta: { title: 'Управление клиентами' }
        },
        {
          path: 'trainers',
          name: 'admin-trainers',
          component: () => import('@/views/admin/TrainersPage.vue'),
          meta: { title: 'Управление тренерами' }
        },
        {
          path: 'sections',
          name: 'admin-sections',
          component: () => import('@/views/admin/SectionsManagePage.vue'),
          meta: { title: 'Управление секциями' }
        },
        {
          path: 'schedule',
          name: 'admin-schedule',
          component: () => import('@/views/admin/ScheduleManagePage.vue'),
          meta: { title: 'Управление расписанием' }
        },
        {
          path: 'bookings',
          name: 'admin-bookings',
          component: () => import('@/views/admin/BookingsManagePage.vue'),
          meta: { title: 'Управление бронированиями' }
        },
        {
          path: 'attendance',
          name: 'admin-attendance',
          component: () => import('@/views/admin/AttendancePage.vue'),
          meta: { title: 'Посещаемость' }
        },
        {
          path: 'employees',
          name: 'admin-employees',
          component: () => import('@/views/admin/EmployeesPage.vue'),
          meta: { title: 'Управление сотрудниками' }
        },
      ]
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// Navigation guards
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  // Set page title
  document.title = to.meta.title
    ? `${to.meta.title} - GymFlow`
    : 'GymFlow - Система управления спортзалом'

  // Check auth requirements
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'login', query: { redirect: to.fullPath } })
  } else if (to.meta.requiresAdmin && !authStore.isAdmin) {
    next({ name: 'admin-login', query: { redirect: to.fullPath } })
  } else {
    next()
  }
})

export default router
