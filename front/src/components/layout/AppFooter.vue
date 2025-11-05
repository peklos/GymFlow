<template>
  <footer class="glass border-t border-white/20 mt-20">
    <div class="container mx-auto px-4 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- About -->
        <div class="space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-primary-500 to-accent-500 rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <span class="text-xl font-bold gradient-text">GymFlow</span>
          </div>
          <p class="text-slate-600 text-sm">
            Современная система управления спортзалом для вашего удобства
          </p>
        </div>

        <!-- Quick Links -->
        <div>
          <h3 class="font-bold text-slate-800 mb-4">Быстрые ссылки</h3>
          <ul class="space-y-2">
            <li>
              <router-link to="/" class="text-slate-600 hover:text-primary-600 text-sm transition-colors">
                Главная
              </router-link>
            </li>
            <li>
              <router-link to="/sections" class="text-slate-600 hover:text-primary-600 text-sm transition-colors">
                Секции
              </router-link>
            </li>
            <li>
              <router-link to="/schedule" class="text-slate-600 hover:text-primary-600 text-sm transition-colors">
                Расписание
              </router-link>
            </li>
          </ul>
        </div>

        <!-- For Clients -->
        <div>
          <h3 class="font-bold text-slate-800 mb-4">Для клиентов</h3>
          <ul class="space-y-2">
            <li>
              <router-link to="/register" class="text-slate-600 hover:text-primary-600 text-sm transition-colors">
                Регистрация
              </router-link>
            </li>
            <li>
              <router-link to="/login" class="text-slate-600 hover:text-primary-600 text-sm transition-colors">
                Вход
              </router-link>
            </li>
            <li>
              <router-link to="/profile" class="text-slate-600 hover:text-primary-600 text-sm transition-colors">
                Профиль
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Contact -->
        <div>
          <h3 class="font-bold text-slate-800 mb-4">Контакты</h3>
          <ul class="space-y-2 text-sm text-slate-600">
            <li class="flex items-center space-x-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              <span>+7 (999) 123-45-67</span>
            </li>
            <li class="flex items-center space-x-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <span>info@gymflow.ru</span>
            </li>
            <li class="flex items-center space-x-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              <span>Москва, ул. Спортивная 1</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="border-t border-slate-200 mt-8 pt-8 flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
        <p class="text-slate-500 text-sm">
          © 2024 GymFlow. Все права защищены.
        </p>
        <div class="flex items-center space-x-6">
          <router-link to="/admin/login" class="text-slate-500 hover:text-primary-600 text-sm transition-colors">
            Вход для сотрудников
          </router-link>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
</style>
