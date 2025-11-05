# 📡 GymSystem API - Примеры запросов

## 🔗 Base URL
```
Локально: http://localhost:8000
Продакшн: https://your-app.onrender.com
```

---

## 👤 КЛИЕНТСКАЯ ЧАСТЬ

### 1. Регистрация нового клиента

**Endpoint:** `POST /auth/register`

**Request:**
```json
{
  "user_data": {
    "login": "newuser@gmail.com",
    "password": "password123"
  },
  "client_data": {
    "full_name": "Иванов Иван Иванович",
    "phone": "+79991234567",
    "email": "newuser@gmail.com",
    "address": "Москва, ул. Ленина, 10",
    "date_of_birth": "1995-05-15"
  }
}
```

**Response (200):**
```json
{
  "message": "Регистрация успешна",
  "user_id": 6,
  "client_id": 6
}
```

---

### 2. Вход клиента

**Endpoint:** `POST /auth/login`

**Request:**
```json
{
  "login": "ivanov@mail.ru",
  "password": "user123"
}
```

**Response (200):**
```json
{
  "message": "Вход выполнен успешно",
  "user_id": 1,
  "client_id": 1,
  "full_name": "Иванов Иван Иванович",
  "email": "ivanov@mail.ru"
}
```

---

### 3. Получить профиль клиента

**Endpoint:** `GET /profile/{client_id}`

**Example:** `GET /profile/1`

**Response (200):**
```json
{
  "id": 1,
  "user_id": 1,
  "full_name": "Иванов Иван Иванович",
  "phone": "+79161234501",
  "email": "ivanov@mail.ru",
  "address": "Москва, ул. Ленина, 10",
  "date_of_birth": "1990-05-15",
  "registration_date": "2024-01-10"
}
```

---

### 4. Обновить профиль

**Endpoint:** `PATCH /profile/{client_id}`

**Example:** `PATCH /profile/1`

**Request:**
```json
{
  "phone": "+79999999999",
  "address": "Москва, ул. Новая, 20"
}
```

**Response (200):**
```json
{
  "id": 1,
  "user_id": 1,
  "full_name": "Иванов Иван Иванович",
  "phone": "+79999999999",
  "email": "ivanov@mail.ru",
  "address": "Москва, ул. Новая, 20",
  "date_of_birth": "1990-05-15",
  "registration_date": "2024-01-10"
}
```

---

### 5. Получить список секций

**Endpoint:** `GET /sections`

**Query параметры:**
- `sport_type` - фильтр по виду спорта (Фитнес, Йога, Бокс и т.д.)
- `is_free` - только бесплатные (true/false)
- `age` - фильтр по возрасту

**Example 1:** `GET /sections` (все секции)

**Example 2:** `GET /sections?sport_type=Йога` (только йога)

**Example 3:** `GET /sections?is_free=true` (только бесплатные)

**Example 4:** `GET /sections?age=10` (для 10-летних)

**Response (200):**
```json
[
  {
    "id": 1,
    "name": "Общий фитнес",
    "sport_type": "Фитнес",
    "age_from": 18,
    "age_to": 65,
    "is_free": false,
    "description": "Общие занятия фитнесом для поддержания формы"
  },
  {
    "id": 2,
    "name": "Йога для начинающих",
    "sport_type": "Йога",
    "age_from": 16,
    "age_to": 70,
    "is_free": false,
    "description": "Занятия йогой для новичков"
  }
]
```

---

### 6. Получить расписание

**Endpoint:** `GET /schedule`

**Query параметры:**
- `section_id` - фильтр по секции
- `trainer_id` - фильтр по тренеру
- `day_of_week` - день недели

**Example 1:** `GET /schedule` (все расписание)

**Example 2:** `GET /schedule?section_id=1` (расписание секции)

**Example 3:** `GET /schedule?day_of_week=Понедельник` (на понедельник)

**Response (200):**
```json
[
  {
    "id": 1,
    "section_id": 1,
    "trainer_id": 1,
    "day_of_week": "Понедельник",
    "start_time": "10:00:00",
    "end_time": "11:30:00",
    "location": "Зал №1"
  },
  {
    "id": 2,
    "section_id": 1,
    "trainer_id": 1,
    "day_of_week": "Среда",
    "start_time": "10:00:00",
    "end_time": "11:30:00",
    "location": "Зал №1"
  }
]
```

---

### 7. Создать бронирование

**Endpoint:** `POST /bookings?client_id={client_id}`

**Example:** `POST /bookings?client_id=1`

**Request (для взрослого):**
```json
{
  "section_id": 1,
  "child_full_name": null,
  "child_age": null
}
```

**Request (для ребенка):**
```json
{
  "section_id": 4,
  "child_full_name": "Иванов Петр",
  "child_age": 10
}
```

**Response (200):**
```json
{
  "id": 9,
  "client_id": 1,
  "section_id": 1,
  "booking_date": "2024-03-10",
  "status": "pending",
  "child_full_name": null,
  "child_age": null
}
```

---

### 8. Получить свои бронирования

**Endpoint:** `GET /bookings/client/{client_id}`

**Example:** `GET /bookings/client/1`

**Response (200):**
```json
[
  {
    "id": 1,
    "client_id": 1,
    "section_id": 1,
    "booking_date": "2024-03-01",
    "status": "approved",
    "child_full_name": null,
    "child_age": null
  },
  {
    "id": 9,
    "client_id": 1,
    "section_id": 1,
    "booking_date": "2024-03-10",
    "status": "pending",
    "child_full_name": null,
    "child_age": null
  }
]
```

---

### 9. Отменить бронирование

**Endpoint:** `DELETE /bookings/{booking_id}`

**Example:** `DELETE /bookings/9`

**Response (200):**
```json
{
  "message": "Бронирование отменено",
  "booking_id": 9
}
```

---

## 🔧 АДМИНСКАЯ ЧАСТЬ

### 1. Вход сотрудника

**Endpoint:** `POST /admin/auth/login`

**Request:**
```json
{
  "login": "admin@gym.ru",
  "password": "admin123"
}
```

**Response (200):**
```json
{
  "message": "Вход выполнен успешно",
  "employee": {
    "id": 1,
    "login": "admin@gym.ru",
    "role": "Администратор",
    "role_id": 1
  }
}
```

---

### 2. Получить всех клиентов

**Endpoint:** `GET /admin/clients`

**Response (200):**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "full_name": "Иванов Иван Иванович",
    "phone": "+79161234501",
    "email": "ivanov@mail.ru",
    "address": "Москва, ул. Ленина, 10",
    "date_of_birth": "1990-05-15",
    "registration_date": "2024-01-10"
  }
]
```

---

### 3. Создать тренера

**Endpoint:** `POST /admin/trainers`

**Request:**
```json
{
  "full_name": "Новиков Алексей Петрович",
  "email": "novikov@gym.ru",
  "phone": "+79166666666",
  "address": "Москва, ул. Спортивная, 1",
  "specialization": "Кроссфит"
}
```

**Response (200):**
```json
{
  "id": 6,
  "full_name": "Новиков Алексей Петрович",
  "email": "novikov@gym.ru",
  "phone": "+79166666666",
  "address": "Москва, ул. Спортивная, 1",
  "specialization": "Кроссфит"
}
```

---

### 4. Создать секцию

**Endpoint:** `POST /admin/sections`

**Request:**
```json
{
  "name": "Бег для начинающих",
  "sport_type": "Легкая атлетика",
  "age_from": 16,
  "age_to": 60,
  "is_free": false,
  "description": "Тренировки по бегу для новичков"
}
```

**Response (200):**
```json
{
  "id": 9,
  "name": "Бег для начинающих",
  "sport_type": "Легкая атлетика",
  "age_from": 16,
  "age_to": 60,
  "is_free": false,
  "description": "Тренировки по бегу для новичков"
}
```

---

### 5. Добавить в расписание

**Endpoint:** `POST /admin/schedule`

**Request:**
```json
{
  "section_id": 1,
  "trainer_id": 1,
  "day_of_week": "Вторник",
  "start_time": "14:00:00",
  "end_time": "15:30:00",
  "location": "Зал №1"
}
```

**Response (200):**
```json
{
  "id": 23,
  "section_id": 1,
  "trainer_id": 1,
  "day_of_week": "Вторник",
  "start_time": "14:00:00",
  "end_time": "15:30:00",
  "location": "Зал №1"
}
```

---

### 6. Одобрить бронирование

**Endpoint:** `PATCH /admin/bookings/{booking_id}`

**Example:** `PATCH /admin/bookings/7`

**Request:**
```json
{
  "status": "approved"
}
```

**Response (200):**
```json
{
  "id": 7,
  "client_id": 2,
  "section_id": 8,
  "booking_date": "2024-03-06",
  "status": "approved",
  "child_full_name": null,
  "child_age": null
}
```

---

### 7. Отметить посещение

**Endpoint:** `POST /admin/attendance`

**Request:**
```json
{
  "booking_id": 1,
  "schedule_id": 1,
  "visit_date": "2024-03-11",
  "was_present": true
}
```

**Response (200):**
```json
{
  "id": 8,
  "booking_id": 1,
  "schedule_id": 1,
  "visit_date": "2024-03-11",
  "was_present": true
}
```

---

### 8. Получить статистику

**Endpoint:** `GET /admin/stats/dashboard`

**Response (200):**
```json
{
  "overview": {
    "total_clients": 5,
    "total_trainers": 5,
    "total_sections": 8,
    "total_bookings": 8
  },
  "bookings": {
    "pending": 2,
    "approved": 6
  },
  "attendance": {
    "total_visits": 7,
    "present_visits": 6,
    "attendance_rate": 85.71
  },
  "popular_sections": [
    {
      "id": 1,
      "name": "Общий фитнес",
      "sport_type": "Фитнес",
      "bookings_count": 3
    }
  ],
  "active_clients": [
    {
      "id": 1,
      "full_name": "Иванов Иван Иванович",
      "email": "ivanov@mail.ru",
      "bookings_count": 2
    }
  ]
}
```

---

### 9. Статистика бронирований

**Endpoint:** `GET /admin/bookings/stats/overview`

**Response (200):**
```json
{
  "total_bookings": 8,
  "pending_bookings": 2,
  "approved_bookings": 6,
  "rejected_bookings": 0,
  "cancelled_bookings": 0
}
```

---

### 10. Создать сотрудника (только Администратор)

**Endpoint:** `POST /admin/employees?admin_id=1`

**Request:**
```json
{
  "login": "support@gym.ru",
  "password": "support123",
  "role_id": 2
}
```

**Response (200):**
```json
{
  "id": 4,
  "login": "support@gym.ru",
  "role_id": 2
}
```

---

## 🔍 Фильтрация и поиск

### Примеры фильтрации секций:

```bash
# Все секции
GET /sections

# Только фитнес
GET /sections?sport_type=Фитнес

# Только бесплатные
GET /sections?is_free=true

# Для детей 10 лет
GET /sections?age=10

# Бесплатный фитнес для детей 12 лет
GET /sections?sport_type=Фитнес&is_free=true&age=12
```

### Примеры фильтрации расписания:

```bash
# Все расписание
GET /schedule

# Расписание секции №1
GET /schedule?section_id=1

# Расписание тренера №2
GET /schedule?trainer_id=2

# Расписание на понедельник
GET /schedule?day_of_week=Понедельник

# Расписание секции №1 на понедельник
GET /schedule?section_id=1&day_of_week=Понедельник
```

---

## ❌ Обработка ошибок

### 400 Bad Request
```json
{
  "detail": "Email уже зарегистрирован"
}
```

### 401 Unauthorized
```json
{
  "detail": "Неверный email или пароль"
}
```

### 403 Forbidden
```json
{
  "detail": "Доступ запрещен. Требуется роль Администратора"
}
```

### 404 Not Found
```json
{
  "detail": "Клиент не найден"
}
```

---

## 📝 Тестирование через curl

### Регистрация:
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "user_data": {"login": "test@test.ru", "password": "test123"},
    "client_data": {
      "full_name": "Тест Тестов",
      "phone": "+79999999999",
      "email": "test@test.ru",
      "address": "Москва",
      "date_of_birth": "1995-01-01"
    }
  }'
```

### Логин:
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"login": "ivanov@mail.ru", "password": "user123"}'
```

### Получить секции:
```bash
curl "http://localhost:8000/sections"
```

### Создать бронирование:
```bash
curl -X POST "http://localhost:8000/bookings?client_id=1" \
  -H "Content-Type: application/json" \
  -d '{
    "section_id": 1,
    "child_full_name": null,
    "child_age": null
  }'
```

---

## 🧪 Тестирование через Python

```python
import requests

BASE_URL = "http://localhost:8000"

# Регистрация
response = requests.post(f"{BASE_URL}/auth/register", json={
    "user_data": {
        "login": "test@test.ru",
        "password": "test123"
    },
    "client_data": {
        "full_name": "Тест Тестов",
        "phone": "+79999999999",
        "email": "test@test.ru",
        "address": "Москва",
        "date_of_birth": "1995-01-01"
    }
})
print(response.json())

# Логин
response = requests.post(f"{BASE_URL}/auth/login", json={
    "login": "ivanov@mail.ru",
    "password": "user123"
})
user_data = response.json()
client_id = user_data["client_id"]

# Получить секции
response = requests.get(f"{BASE_URL}/sections")
sections = response.json()
print(f"Найдено секций: {len(sections)}")

# Создать бронирование
response = requests.post(
    f"{BASE_URL}/bookings?client_id={client_id}",
    json={
        "section_id": 1,
        "child_full_name": None,
        "child_age": None
    }
)
booking = response.json()
print(f"Создано бронирование: {booking['id']}")
```

---

**Готово! Все примеры готовы к использованию! 🚀**
