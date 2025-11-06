<template>
  <Modal v-model="isOpen" title="📖 Справочник по использованию сайта">
    <div class="prose prose-slate max-w-none">
      <!-- Введение -->
      <div class="bg-gradient-to-br from-blue-50 to-purple-50 p-6 rounded-xl mb-6 border border-blue-100">
        <h3 class="text-2xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          👋 Добро пожаловать в GymFlow!
        </h3>
        <p class="text-slate-700 text-base leading-relaxed mb-0">
          Этот справочник поможет вам быстро освоиться с системой и начать тренировки.
          Здесь вы найдете пошаговые инструкции по всем основным функциям сайта.
        </p>
      </div>

      <!-- Навигация по сайту -->
      <div class="mb-6">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          🧭 Навигация по сайту
        </h4>
        <div class="bg-slate-50 p-5 rounded-lg border border-slate-200">
          <p class="text-slate-700 mb-3 text-base">
            В верхней части сайта расположено главное меню с разделами:
          </p>
          <ul class="space-y-2 text-slate-700 text-base">
            <li class="flex items-start gap-2">
              <span class="text-blue-500 font-bold">•</span>
              <span><strong>Главная</strong> — главная страница с популярными секциями</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-blue-500 font-bold">•</span>
              <span><strong>Секции</strong> — список всех доступных секций и программ</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-blue-500 font-bold">•</span>
              <span><strong>Расписание</strong> — расписание всех занятий</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-blue-500 font-bold">•</span>
              <span><strong>Профиль</strong> — ваши личные данные и настройки</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-blue-500 font-bold">•</span>
              <span><strong>Мои бронирования</strong> — список ваших забронированных занятий</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Как посмотреть секции -->
      <div class="mb-6">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          🏋️ Как посмотреть секции
        </h4>
        <div class="bg-green-50 p-5 rounded-lg border border-green-200">
          <ol class="space-y-3 text-slate-700 text-base list-none">
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-green-500 text-white rounded-full flex items-center justify-center text-sm font-bold">1</span>
              <span>Нажмите на кнопку <strong>"Секции"</strong> в верхнем меню или кнопку <strong>"Все секции"</strong> на главной странице</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-green-500 text-white rounded-full flex items-center justify-center text-sm font-bold">2</span>
              <span>Вы увидите список всех доступных секций с описаниями, ценами и фотографиями</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-green-500 text-white rounded-full flex items-center justify-center text-sm font-bold">3</span>
              <span>Нажмите на карточку секции, чтобы узнать подробнее о программе и тренерах</span>
            </li>
          </ol>
        </div>
      </div>

      <!-- Как посмотреть тренеров -->
      <div class="mb-6">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          👨‍🏫 Как посмотреть тренеров
        </h4>
        <div class="bg-purple-50 p-5 rounded-lg border border-purple-200">
          <ol class="space-y-3 text-slate-700 text-base list-none">
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-purple-500 text-white rounded-full flex items-center justify-center text-sm font-bold">1</span>
              <span>Перейдите в раздел <strong>"Секции"</strong> и выберите интересующую вас программу</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-purple-500 text-white rounded-full flex items-center justify-center text-sm font-bold">2</span>
              <span>На странице секции вы увидите список тренеров, работающих по этой программе</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-purple-500 text-white rounded-full flex items-center justify-center text-sm font-bold">3</span>
              <span>Для каждого тренера указаны его специализация, опыт работы и фотография</span>
            </li>
          </ol>
        </div>
      </div>

      <!-- Как посмотреть расписание -->
      <div class="mb-6">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          📅 Как посмотреть расписание
        </h4>
        <div class="bg-blue-50 p-5 rounded-lg border border-blue-200">
          <ol class="space-y-3 text-slate-700 text-base list-none">
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">1</span>
              <span>Нажмите на кнопку <strong>"Расписание"</strong> в верхнем меню</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">2</span>
              <span>Вы увидите таблицу с расписанием всех занятий на неделю</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">3</span>
              <span>Для каждого занятия указаны: время, секция, тренер, количество свободных мест и стоимость</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">4</span>
              <span>Используйте фильтры вверху страницы, чтобы найти занятия по дате или секции</span>
            </li>
          </ol>
        </div>
      </div>

      <!-- Как забронировать занятие -->
      <div class="mb-6">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          ✅ Как забронировать занятие
        </h4>
        <div class="bg-orange-50 p-5 rounded-lg border border-orange-200">
          <ol class="space-y-3 text-slate-700 text-base list-none">
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-orange-500 text-white rounded-full flex items-center justify-center text-sm font-bold">1</span>
              <span>Перейдите в раздел <strong>"Расписание"</strong> и найдите нужное занятие</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-orange-500 text-white rounded-full flex items-center justify-center text-sm font-bold">2</span>
              <span>Убедитесь, что есть свободные места (показано в колонке "Места")</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-orange-500 text-white rounded-full flex items-center justify-center text-sm font-bold">3</span>
              <span>Нажмите кнопку <strong>"Забронировать"</strong> напротив выбранного занятия</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-orange-500 text-white rounded-full flex items-center justify-center text-sm font-bold">4</span>
              <span>Подтвердите бронирование в появившемся окне</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-orange-500 text-white rounded-full flex items-center justify-center text-sm font-bold">5</span>
              <span>Готово! Ваше бронирование создано, и занятие появится в разделе <strong>"Мои бронирования"</strong></span>
            </li>
          </ol>
          <div class="mt-4 p-3 bg-white rounded-lg border-l-4 border-orange-400">
            <p class="text-sm text-slate-700 mb-0">
              <strong>💡 Совет:</strong> Вы можете отменить бронирование в разделе "Мои бронирования" не позднее чем за 2 часа до начала занятия.
            </p>
          </div>
        </div>
      </div>

      <!-- Мои бронирования -->
      <div class="mb-6">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          📋 Мои бронирования
        </h4>
        <div class="bg-indigo-50 p-5 rounded-lg border border-indigo-200">
          <ol class="space-y-3 text-slate-700 text-base list-none">
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-indigo-500 text-white rounded-full flex items-center justify-center text-sm font-bold">1</span>
              <span>Нажмите на <strong>"Мои бронирования"</strong> в верхнем меню</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-indigo-500 text-white rounded-full flex items-center justify-center text-sm font-bold">2</span>
              <span>Здесь вы увидите список всех ваших забронированных занятий</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-indigo-500 text-white rounded-full flex items-center justify-center text-sm font-bold">3</span>
              <span>Для каждого бронирования показана информация: дата, время, секция, тренер и статус</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="flex-shrink-0 w-6 h-6 bg-indigo-500 text-white rounded-full flex items-center justify-center text-sm font-bold">4</span>
              <span>Вы можете отменить бронирование, нажав на кнопку <strong>"Отменить"</strong></span>
            </li>
          </ol>
        </div>
      </div>

      <!-- Профиль -->
      <div class="mb-6">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          👤 Профиль
        </h4>
        <div class="bg-teal-50 p-5 rounded-lg border border-teal-200">
          <p class="text-slate-700 mb-3 text-base">
            В разделе <strong>"Профиль"</strong> вы можете:
          </p>
          <ul class="space-y-2 text-slate-700 text-base">
            <li class="flex items-start gap-2">
              <span class="text-teal-500 font-bold">•</span>
              <span>Просмотреть и изменить свои личные данные (имя, email, телефон)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-teal-500 font-bold">•</span>
              <span>Изменить пароль для входа в систему</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-teal-500 font-bold">•</span>
              <span>Посмотреть статистику ваших тренировок</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-teal-500 font-bold">•</span>
              <span>Выйти из системы</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Дополнительные советы -->
      <div class="bg-gradient-to-br from-amber-50 to-yellow-50 p-6 rounded-xl border border-amber-200">
        <h4 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
          💡 Полезные советы
        </h4>
        <ul class="space-y-2 text-slate-700 text-base">
          <li class="flex items-start gap-2">
            <span class="text-amber-500 font-bold">•</span>
            <span>Бронируйте занятия заранее, чтобы гарантировать себе место</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-amber-500 font-bold">•</span>
            <span>Приходите на занятия за 10-15 минут до начала</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-amber-500 font-bold">•</span>
            <span>Если не можете прийти, обязательно отмените бронирование заранее</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-amber-500 font-bold">•</span>
            <span>Регулярно проверяйте расписание - оно может меняться</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-amber-500 font-bold">•</span>
            <span>При возникновении вопросов обращайтесь к администратору зала</span>
          </li>
        </ul>
      </div>

      <!-- Контакты -->
      <div class="mt-6 text-center p-4 bg-slate-100 rounded-lg">
        <p class="text-slate-700 text-base mb-0">
          Если у вас остались вопросы, вы всегда можете обратиться к администратору зала или написать нам на почту.
          <br>
          <strong>Хороших тренировок! 💪</strong>
        </p>
      </div>
    </div>
  </Modal>
</template>

<script setup>
import { computed } from 'vue'
import Modal from './Modal.vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['update:modelValue'])

const isOpen = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})
</script>

<style scoped>
/* Убираем стандартные стили prose для более точного контроля */
.prose {
  max-width: none;
}

.prose h3,
.prose h4 {
  margin-top: 0;
}

.prose p {
  margin-bottom: 0.75rem;
}

.prose ul,
.prose ol {
  margin-top: 0;
  margin-bottom: 0;
}
</style>
