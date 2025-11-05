# 🎨 Гайд для разработки Frontend

## ✅ Бекенд готов на 100%!

Backend API полностью протестирован и готов к интеграции с фронтендом.

---

## 🔗 Подключение к API

### Локальная разработка
```javascript
const API_URL = 'http://localhost:8000';
```

### После деплоя на Render
```javascript
const API_URL = 'https://your-app-name.onrender.com';
```

---

## 📋 Основные эндпоинты для фронтенда

### 1. Регистрация пользователя
```javascript
async function register(userData, clientData) {
  const response = await fetch(`${API_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      user_data: userData,    // { login, password }
      client_data: clientData // { full_name, phone, email, address, date_of_birth }
    })
  });
  return await response.json();
  // Вернет: { message, user_id, client_id }
}
```

### 2. Вход пользователя
```javascript
async function login(login, password) {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ login, password })
  });
  return await response.json();
  // Вернет: { message, user_id, client_id, full_name, email }
}
```

### 3. Получить список секций
```javascript
async function getSections(filters = {}) {
  // Фильтры: sport_type, is_free, age
  const params = new URLSearchParams(filters);
  const response = await fetch(`${API_URL}/sections/?${params}`);
  return await response.json();
  // Вернет массив секций
}
```

### 4. Получить расписание
```javascript
async function getSchedule(filters = {}) {
  // Фильтры: section_id, trainer_id, day_of_week
  const params = new URLSearchParams(filters);
  const response = await fetch(`${API_URL}/schedule/?${params}`);
  return await response.json();
  // Вернет массив занятий
}
```

### 5. Создать бронирование
```javascript
async function createBooking(clientId, sectionId, childData = null) {
  const response = await fetch(`${API_URL}/bookings/?client_id=${clientId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      section_id: sectionId,
      child_full_name: childData?.name || null,
      child_age: childData?.age || null
    })
  });
  return await response.json();
  // Вернет: { id, client_id, section_id, booking_date, status, ... }
}
```

### 6. Мои бронирования
```javascript
async function getMyBookings(clientId) {
  const response = await fetch(`${API_URL}/bookings/client/${clientId}/`);
  return await response.json();
  // Вернет массив бронирований
}
```

### 7. Получить профиль
```javascript
async function getProfile(clientId) {
  const response = await fetch(`${API_URL}/profile/${clientId}/`);
  return await response.json();
}
```

### 8. Обновить профиль
```javascript
async function updateProfile(clientId, updates) {
  const response = await fetch(`${API_URL}/profile/${clientId}/`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(updates)
  });
  return await response.json();
}
```

---

## 🔧 Админская часть

### 1. Вход администратора
```javascript
async function adminLogin(login, password) {
  const response = await fetch(`${API_URL}/admin/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ login, password })
  });
  return await response.json();
  // Вернет: { message, employee: { id, login, role, role_id } }
}
```

### 2. Получить статистику
```javascript
async function getDashboardStats() {
  const response = await fetch(`${API_URL}/admin/stats/dashboard`);
  return await response.json();
  // Вернет: { overview, bookings, attendance, popular_sections, active_clients }
}
```

### 3. Управление клиентами
```javascript
async function getClients() {
  const response = await fetch(`${API_URL}/admin/clients/`);
  return await response.json();
}
```

### 4. Управление тренерами
```javascript
async function getTrainers() {
  const response = await fetch(`${API_URL}/admin/trainers/`);
  return await response.json();
}

async function createTrainer(trainerData) {
  const response = await fetch(`${API_URL}/admin/trainers/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(trainerData)
  });
  return await response.json();
}
```

---

## 🎯 Структура приложения (рекомендации)

### Страницы для клиентов:
1. **Главная** - список секций с фильтрами
2. **Секция** - детальная информация + расписание
3. **Регистрация** - форма регистрации
4. **Вход** - форма входа
5. **Профиль** - данные пользователя + мои бронирования
6. **Расписание** - общее расписание с фильтрами

### Страницы для админа:
1. **Дашборд** - статистика
2. **Клиенты** - список + CRUD
3. **Тренеры** - список + CRUD
4. **Секции** - список + CRUD
5. **Расписание** - управление расписанием
6. **Бронирования** - все бронирования + управление статусами

---

## 💾 Хранение состояния

### Рекомендуемый стек:
- **React** + **React Router** + **Context API** или **Redux**
- **Vue** + **Vue Router** + **Pinia**
- **Next.js** (для SSR)

### Что хранить в localStorage:
```javascript
// После успешного входа
localStorage.setItem('user', JSON.stringify({
  user_id: response.user_id,
  client_id: response.client_id,
  full_name: response.full_name,
  email: response.email
}));

// Для админа
localStorage.setItem('employee', JSON.stringify({
  employee_id: response.employee.id,
  login: response.employee.login,
  role: response.employee.role,
  role_id: response.employee.role_id
}));
```

---

## ⚠️ Важные замечания

### 1. Trailing Slash
Все GET эндпоинты требуют `/` в конце:
- ✅ `fetch('/sections/')`
- ❌ `fetch('/sections')` - вернет 307 redirect

### 2. CORS
CORS уже настроен на бекенде - все origins разрешены.

### 3. Авторизация
API **НЕ использует JWT токены** (упрощенная версия для учебного проекта).
Авторизация через передачу `user_id`, `client_id` или `employee_id`.

### 4. Валидация
Бекенд валидирует все входные данные через Pydantic.
Ошибки возвращаются в формате:
```json
{
  "detail": "Email уже зарегистрирован"
}
```

---

## 🚀 Деплой фронтенда

### На Netlify (рекомендуется):

1. **Build settings:**
   - Build command: `npm run build` (или `yarn build`)
   - Publish directory: `dist` (или `build`)

2. **Environment variables:**
   ```
   VITE_API_URL=https://your-backend.onrender.com
   # или для Next.js:
   NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
   ```

3. **Редиректы для SPA** (`public/_redirects`):
   ```
   /* /index.html 200
   ```

---

## 📚 Полная документация API

После запуска бекенда локально:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🧪 Тестовые данные

### Клиенты для тестирования:
- `ivanov@mail.ru` / `user123`
- `petrova@gmail.com` / `user123`

### Админы:
- `admin@gym.ru` / `admin123` (Администратор)
- `manager@gym.ru` / `manager123` (Менеджер)

---

## ✅ Чеклист интеграции

- [ ] Настроить API_URL в конфиге
- [ ] Реализовать регистрацию/вход
- [ ] Показать список секций
- [ ] Реализовать фильтрацию секций
- [ ] Показать расписание
- [ ] Реализовать создание бронирований
- [ ] Показать "Мои бронирования"
- [ ] Реализовать админ-панель (если нужно)
- [ ] Добавить обработку ошибок
- [ ] Тестирование всех форм

---

**Бекенд готов! Начинай разработку фронтенда! 🚀**
