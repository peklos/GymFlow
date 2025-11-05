# GymFlow - Система управления спортивным залом
## Описание проекта для защиты

---

## 📋 Содержание

1. [Введение](#введение)
2. [Технологический стек](#технологический-стек)
3. [Архитектура приложения](#архитектура-приложения)
4. [Структура базы данных](#структура-базы-данных)
5. [Типы связей между таблицами](#типы-связей-между-таблицами)
6. [Реализация backend](#реализация-backend)
7. [Реализация frontend](#реализация-frontend)
8. [API Endpoints](#api-endpoints)
9. [Функциональные возможности](#функциональные-возможности)
10. [Развертывание проекта](#развертывание-проекта)
11. [Заключение](#заключение)

---

## 1. Введение

**GymFlow** — это полнофункциональная веб-система для управления спортивным залом, разработанная с использованием современного технологического стека. Проект включает в себя backend API на FastAPI и frontend на Vue.js 3.

### Цель проекта
Создать удобную систему для управления:
- Клиентами и их записями
- Тренерами и расписанием
- Секциями и бронированиями
- Посещаемостью и статистикой

### Решаемые задачи
1. Автоматизация процесса записи клиентов на занятия
2. Управление расписанием тренировок
3. Контроль посещаемости
4. Административная панель для сотрудников
5. Личный кабинет для клиентов

---

## 2. Технологический стек

### Backend
- **FastAPI** (Python 3.11+)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (продакшн)
- **SQLite** (разработка)
- **Pydantic** (валидация)
- **Uvicorn** (ASGI сервер)

### Frontend
- **Vue.js 3** (Composition API)
- **Vite** (сборщик)
- **Vue Router** (маршрутизация)
- **Pinia** (state management)
- **Tailwind CSS** (стилизация)
- **Axios** (HTTP клиент)

### DevOps
- **Git/GitHub** (контроль версий)
- **Render** (backend хостинг)
- **Netlify** (frontend хостинг)
- **Neon** (PostgreSQL в облаке)

### Почему этот стек крутой?

#### FastAPI
✅ **Самый быстрый Python фреймворк** — производительность сравнима с Node.js и Go
✅ **Автоматическая генерация документации** — Swagger UI и ReDoc из коробки
✅ **Типизация** — использует Python type hints для валидации
✅ **Async/await** — поддержка асинхронности для высокой производительности
✅ **Современный стандарт** — используется в крупных компаниях (Uber, Netflix)

#### Vue.js 3
✅ **Composition API** — более гибкая и масштабируемая архитектура
✅ **Реактивность** — автоматическое обновление UI при изменении данных
✅ **Легкий вес** — меньше размер бандла, быстрее загрузка
✅ **Простота изучения** — проще React, но мощнее
✅ **Производительность** — Virtual DOM и оптимизация рендеринга

#### PostgreSQL
✅ **Самая продвинутая open-source БД** — ACID транзакции, JSON, индексы
✅ **Надежность** — используется в банках и крупных проектах
✅ **Масштабируемость** — горизонтальное и вертикальное масштабирование
✅ **Бесплатная** — полностью open-source без ограничений

#### Tailwind CSS
✅ **Utility-first** — быстрая разработка без написания CSS
✅ **Responsive** — адаптивный дизайн из коробки
✅ **Малый размер** — PurgeCSS удаляет неиспользуемые стили
✅ **Консистентность** — единая система дизайна

---

## 3. Архитектура приложения

### Общая архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Vue.js 3   │  │ Vue Router   │  │    Pinia     │      │
│  │  Components  │  │  Маршруты    │  │  Store       │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         │                 │                  │               │
│         └─────────────────┴──────────────────┘               │
│                          │                                   │
│                    ┌─────▼──────┐                           │
│                    │   Axios    │                           │
│                    │ HTTP Client│                           │
│                    └─────┬──────┘                           │
└──────────────────────────┼──────────────────────────────────┘
                           │ REST API
                           │ JSON
┌──────────────────────────▼──────────────────────────────────┐
│                        BACKEND                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   FastAPI    │  │  Pydantic    │  │ SQLAlchemy   │      │
│  │   Routers    │  │   Schemas    │  │    ORM       │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                  │               │
│         └─────────────────┴──────────────────┘               │
│                          │                                   │
│                    ┌─────▼──────┐                           │
│                    │  Database  │                           │
│                    │ PostgreSQL │                           │
│                    └────────────┘                           │
└─────────────────────────────────────────────────────────────┘
```

### Трехуровневая архитектура

1. **Presentation Layer (Frontend)**
   - Vue компоненты
   - Роутинг
   - Состояние приложения

2. **Business Logic Layer (Backend)**
   - API endpoints
   - Бизнес-логика
   - Валидация данных

3. **Data Access Layer (Database)**
   - ORM модели
   - SQL запросы
   - Транзакции

---

## 4. Структура базы данных

### ER-диаграмма

```
┌──────────────┐         ┌──────────────┐
│    Roles     │◄────────┤   Employees  │
│──────────────│ 1     ∞ │──────────────│
│ id (PK)      │         │ id (PK)      │
│ name         │         │ login        │
└──────────────┘         │ password     │
       ▲                 │ role_id (FK) │
       │                 └──────────────┘
       │ 1
       │
       │ ∞                ┌──────────────┐
┌──────┴───────┐         │   Clients    │
│ UserClients  │◄────────┤──────────────│
│──────────────│ 1     1 │ id (PK)      │
│ id (PK)      │         │ user_id (FK) │
│ login        │         │ full_name    │
│ password     │         │ phone        │
│ role_id (FK) │         │ email        │
└──────────────┘         │ address      │
                         │ date_of_birth│
                         └──────┬───────┘
                                │ 1
                                │
                                │ ∞
                         ┌──────▼───────┐
                    ┌────┤   Bookings   ├────┐
                    │    │──────────────│    │
                    │    │ id (PK)      │    │
                    │    │ client_id(FK)│    │
                    │    │ section_id(FK│    │
                    │    │ booking_date │    │
                    │    │ status       │    │
                    │    └──────┬───────┘    │
                    │           │ 1          │
                    │           │            │
                    │           │ ∞          │
                    │    ┌──────▼───────┐   │
                    │    │  Attendance  │   │
                    │    │──────────────│   │
                    │    │ id (PK)      │   │
                    │    │ booking_id(FK│   │
                    │    │ schedule_id  │   │
                    │    │ visit_date   │   │
                    │    │ was_present  │   │
                    │    └──────────────┘   │
                    │                        │
                    │                        │
            ┌───────▼────────┐       ┌──────▼──────┐
            │   Sections     │       │  Schedules  │
            │────────────────│       │─────────────│
            │ id (PK)        │       │ id (PK)     │
            │ name           │       │ section_id  │
            │ sport_type     │       │ trainer_id  │
            │ age_from       │       │ day_of_week │
            │ age_to         │       │ start_time  │
            │ is_free        │       │ end_time    │
            │ description    │◄──────┤ location    │
            └────────────────┘ 1   ∞ └──────┬──────┘
                                            │ ∞
                                            │
                                            │ 1
                                     ┌──────▼──────┐
                                     │  Trainers   │
                                     │─────────────│
                                     │ id (PK)     │
                                     │ full_name   │
                                     │ email       │
                                     │ phone       │
                                     │ address     │
                                     │specialization
                                     └─────────────┘
```

### Описание таблиц

#### 1. **roles** (Роли пользователей)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| name | String(50) | Название роли (Клиент, Администратор, Менеджер) |

**Назначение:** Система разграничения прав доступа

---

#### 2. **employees** (Сотрудники)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| login | String(100) | Логин сотрудника (уникальный) |
| password | String(100) | Пароль (хэшированный) |
| role_id | Integer (FK) | Внешний ключ на roles |

**Назначение:** Учетные записи администраторов и менеджеров

---

#### 3. **user_clients** (Учетные записи клиентов)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| login | String(100) | Логин клиента (email) |
| password | String(100) | Пароль (хэшированный) |
| role_id | Integer (FK) | Внешний ключ на roles |

**Назначение:** Авторизация клиентов в системе

---

#### 4. **clients** (Клиенты)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| user_id | Integer (FK) | Связь с user_clients |
| full_name | String(100) | ФИО клиента |
| phone | String(20) | Телефон (уникальный) |
| email | String(100) | Email (уникальный) |
| address | String(255) | Адрес |
| date_of_birth | Date | Дата рождения |
| registration_date | Date | Дата регистрации |

**Назначение:** Персональная информация о клиентах

---

#### 5. **trainers** (Тренеры)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| full_name | String(100) | ФИО тренера |
| email | String(100) | Email (уникальный) |
| phone | String(20) | Телефон (уникальный) |
| address | String(255) | Адрес |
| specialization | String(100) | Специализация |

**Назначение:** Информация о тренерах

---

#### 6. **sections** (Секции)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| name | String(100) | Название секции |
| sport_type | String(50) | Вид спорта |
| age_from | Integer | Возраст от |
| age_to | Integer | Возраст до |
| is_free | Boolean | Бесплатная секция |
| description | Text | Описание |

**Назначение:** Спортивные секции и направления

---

#### 7. **schedules** (Расписание)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| section_id | Integer (FK) | Внешний ключ на sections |
| trainer_id | Integer (FK) | Внешний ключ на trainers |
| day_of_week | String(20) | День недели |
| start_time | Time | Время начала |
| end_time | Time | Время окончания |
| location | String(100) | Место проведения |

**Назначение:** Расписание занятий

---

#### 8. **bookings** (Бронирования)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| client_id | Integer (FK) | Внешний ключ на clients |
| section_id | Integer (FK) | Внешний ключ на sections |
| booking_date | Date | Дата бронирования |
| status | String(30) | Статус (Ожидание, Подтверждено, Отменено) |
| child_full_name | String(100) | ФИО ребенка (если запись для ребенка) |
| child_age | Integer | Возраст ребенка |

**Назначение:** Заявки на запись в секции

---

#### 9. **attendance** (Посещаемость)
| Поле | Тип | Описание |
|------|-----|----------|
| id | Integer (PK) | Первичный ключ |
| booking_id | Integer (FK) | Внешний ключ на bookings |
| schedule_id | Integer (FK) | Внешний ключ на schedules |
| visit_date | Date | Дата посещения |
| was_present | Boolean | Присутствовал ли |

**Назначение:** Учет посещаемости занятий

---

## 5. Типы связей между таблицами

### 5.1. Один-ко-многим (One-to-Many) — 1:∞

#### **Roles → Employees**
```python
# models.py
class Role(Base):
    employees = relationship('Employee', back_populates='role')

class Employee(Base):
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role', back_populates='employees')
```
**Объяснение:** Одна роль может быть у многих сотрудников, но каждый сотрудник имеет только одну роль.

---

#### **Roles → UserClients**
```python
class Role(Base):
    user_clients = relationship('UserClient', back_populates='role')

class UserClient(Base):
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role', back_populates='user_clients')
```
**Объяснение:** Одна роль может быть у многих клиентов (все клиенты имеют роль "Клиент").

---

#### **Clients → Bookings**
```python
class Client(Base):
    bookings = relationship('Booking', back_populates='client')

class Booking(Base):
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Client', back_populates='bookings')
```
**Объяснение:** Один клиент может иметь много бронирований (записей на секции).

---

#### **Sections → Bookings**
```python
class Section(Base):
    bookings = relationship('Booking', back_populates='section')

class Booking(Base):
    section_id = Column(Integer, ForeignKey('sections.id'))
    section = relationship('Section', back_populates='bookings')
```
**Объяснение:** В одну секцию могут записаться много клиентов.

---

#### **Trainers → Schedules**
```python
class Trainer(Base):
    schedules = relationship('Schedule', back_populates='trainer')

class Schedule(Base):
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    trainer = relationship('Trainer', back_populates='schedules')
```
**Объяснение:** Один тренер ведет много занятий по расписанию.

---

#### **Sections → Schedules**
```python
class Section(Base):
    schedules = relationship('Schedule', back_populates='section')

class Schedule(Base):
    section_id = Column(Integer, ForeignKey('sections.id'))
    section = relationship('Section', back_populates='schedules')
```
**Объяснение:** Одна секция имеет много занятий в расписании.

---

### 5.2. Один-к-одному (One-to-One) — 1:1

#### **UserClients ↔ Clients**
```python
class UserClient(Base):
    client = relationship('Client', back_populates='user', uselist=False)

class Client(Base):
    user_id = Column(Integer, ForeignKey('user_clients.id'), unique=True)
    user = relationship('UserClient', back_populates='client')
```
**Объяснение:** Каждая учетная запись клиента связана ровно с одной записью в таблице clients. Параметр `uselist=False` указывает на связь 1:1.

---

### 5.3. Многие-ко-многим через промежуточную таблицу (Many-to-Many)

В нашем проекте **нет прямых связей многие-ко-многим**, но есть связи, реализованные через промежуточные таблицы:

#### **Clients ↔ Schedules через Bookings и Attendance**

```
Clients → Bookings → Attendance ← Schedules
```

**Объяснение:**
- Один клиент может посещать много занятий (через бронирования)
- Одно занятие могут посещать много клиентов
- Промежуточные таблицы `bookings` и `attendance` связывают клиентов и расписание

---

## 6. Реализация Backend

### 6.1. Структура Backend

```
back/
├── db/
│   ├── database.py      # Конфигурация БД
│   ├── models.py        # SQLAlchemy модели
│   └── init_data.py     # Начальные данные
├── schemas/
│   ├── role.py          # Pydantic схемы ролей
│   ├── employee.py      # Схемы сотрудников
│   ├── user.py          # Схемы пользователей
│   └── ...              # Остальные схемы
├── routers/
│   ├── auth.py          # Авторизация клиентов
│   ├── profile.py       # Профиль клиента
│   ├── sections.py      # API секций
│   ├── schedule.py      # API расписания
│   ├── bookings.py      # API бронирований
│   └── admin_*.py       # Админские роутеры
└── main.py              # Точка входа
```

### 6.2. Ключевые концепции

#### **Dependency Injection**
```python
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()
```
**Объяснение:** FastAPI автоматически создает и закрывает соединение с БД для каждого запроса.

---

#### **Pydantic валидация**
```python
from pydantic import BaseModel, EmailStr

class ClientCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
```
**Объяснение:** Pydantic автоматически валидирует входящие данные и возвращает понятные ошибки.

---

#### **ORM relationships**
```python
# Получение клиента с его бронированиями
client = db.query(Client).filter(Client.id == 1).first()
bookings = client.bookings  # Автоматически загружаются через relationship
```

---

#### **CORS middleware**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```
**Объяснение:** Разрешает кросс-доменные запросы от frontend к backend.

---

### 6.3. Примеры API endpoints

#### Регистрация клиента
```python
@router.post("/auth/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Проверка существующего пользователя
    existing = db.query(UserClient).filter(
        UserClient.login == user_data.login
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Пользователь существует")

    # Создание учетной записи
    user = UserClient(
        login=user_data.login,
        password=user_data.password,  # В реальности хэшируется
        role_id=1  # Роль "Клиент"
    )
    db.add(user)
    db.commit()

    # Создание профиля клиента
    client = Client(
        user_id=user.id,
        full_name=user_data.full_name,
        phone=user_data.phone,
        email=user_data.email
    )
    db.add(client)
    db.commit()

    return {"id": user.id, "login": user.login}
```

---

#### Получение расписания с фильтрами
```python
@router.get("/schedule/")
def get_schedule(
    section_id: Optional[int] = None,
    day_of_week: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Schedule)

    if section_id:
        query = query.filter(Schedule.section_id == section_id)
    if day_of_week:
        query = query.filter(Schedule.day_of_week == day_of_week)

    schedules = query.all()

    # Добавление computed полей
    result = []
    for schedule in schedules:
        result.append({
            "id": schedule.id,
            "section_name": schedule.section.name,
            "trainer_name": schedule.trainer.full_name,
            "day_of_week": schedule.day_of_week,
            "time_start": str(schedule.start_time),
            "time_end": str(schedule.end_time)
        })

    return result
```

---

#### Статистика для дашборда
```python
@router.get("/admin/stats/dashboard")
def get_stats(db: Session = Depends(get_db)):
    return {
        "total_clients": db.query(Client).count(),
        "total_trainers": db.query(Trainer).count(),
        "total_sections": db.query(Section).count(),
        "total_bookings": db.query(Booking).count()
    }
```

---

## 7. Реализация Frontend

### 7.1. Структура Frontend

```
front/src/
├── api/
│   ├── axios.js         # Настройка HTTP клиента
│   └── services.js      # API сервисы
├── components/
│   ├── common/          # Общие компоненты
│   └── layout/          # Компоненты разметки
├── views/
│   ├── client/          # Страницы клиента
│   │   ├── HomePage.vue
│   │   ├── ProfilePage.vue
│   │   ├── SchedulePage.vue
│   │   └── SectionsPage.vue
│   ├── admin/           # Админка
│   │   ├── DashboardPage.vue
│   │   ├── ClientsPage.vue
│   │   └── ...
│   └── auth/            # Авторизация
├── stores/
│   ├── auth.js          # Pinia store авторизации
│   └── sections.js      # Store секций
└── router/
    └── index.js         # Конфигурация маршрутов
```

### 7.2. Ключевые концепции

#### **Composition API**
```vue
<script setup>
import { ref, onMounted } from 'vue'

const clients = ref([])
const isLoading = ref(false)

onMounted(async () => {
  isLoading.value = true
  const response = await adminClientsService.getAll()
  clients.value = response.data
  isLoading.value = false
})
</script>
```
**Преимущества:**
- Более читаемый код
- Лучшая переиспользуемость логики
- TypeScript поддержка

---

#### **Pinia Store (State Management)**
```javascript
// stores/auth.js
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: null,
    isAuthenticated: false
  }),

  actions: {
    async login(credentials) {
      const response = await authService.login(credentials)
      this.user = response.data.user
      this.token = response.data.token
      this.isAuthenticated = true
      localStorage.setItem('token', this.token)
    },

    logout() {
      this.user = null
      this.token = null
      this.isAuthenticated = false
      localStorage.removeItem('token')
    }
  },

  getters: {
    isAdmin: (state) => state.user?.role_name === 'Администратор'
  }
})
```

---

#### **Vue Router Guards**
```javascript
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  // Редирект на логин если требуется авторизация
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'login' })
    return
  }

  // Редирект на админку если требуются права администратора
  if (to.meta.requiresAdmin && !authStore.isAdmin) {
    next({ name: 'home' })
    return
  }

  next()
})
```

---

#### **Axios Interceptors**
```javascript
// api/axios.js
import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
})

// Добавление токена ко всем запросам
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Обработка ошибок
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401) {
      // Редирект на логин
      router.push('/login')
    }
    return Promise.reject(error)
  }
)
```

---

#### **Reactive Forms**
```vue
<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="form.email" type="email" required />
    <input v-model="form.password" type="password" required />
    <button type="submit" :disabled="isLoading">
      {{ isLoading ? 'Загрузка...' : 'Войти' }}
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
  email: '',
  password: ''
})

const isLoading = ref(false)

const handleSubmit = async () => {
  isLoading.value = true
  try {
    await authStore.login(form.value)
    router.push('/profile')
  } catch (error) {
    alert('Ошибка входа')
  } finally {
    isLoading.value = false
  }
}
</script>
```

---

## 8. API Endpoints

### 8.1. Публичные endpoints (клиенты)

#### Авторизация
```
POST   /auth/register          - Регистрация клиента
POST   /auth/login             - Вход клиента
GET    /auth/me/{user_id}      - Получить данные пользователя
```

#### Профиль
```
GET    /profile/{client_id}    - Получить профиль
PATCH  /profile/{client_id}    - Обновить профиль
```

#### Секции
```
GET    /sections/              - Список секций (с фильтрами)
GET    /sections/{id}          - Детали секции
```

#### Расписание
```
GET    /schedule/              - Расписание (с фильтрами)
GET    /schedule/{id}          - Детали занятия
```

#### Бронирования
```
POST   /bookings/              - Создать бронирование
GET    /bookings/client/{id}   - Бронирования клиента
DELETE /bookings/{id}          - Отменить бронирование
```

### 8.2. Админские endpoints

#### Авторизация админа
```
POST   /admin/auth/login       - Вход администратора
GET    /admin/auth/me/{emp_id} - Данные сотрудника
```

#### Управление клиентами
```
GET    /admin/clients/         - Список клиентов
GET    /admin/clients/{id}     - Детали клиента
PATCH  /admin/clients/{id}     - Обновить клиента
DELETE /admin/clients/{id}     - Удалить клиента
```

#### Управление тренерами
```
GET    /admin/trainers/        - Список тренеров
POST   /admin/trainers/        - Создать тренера
PATCH  /admin/trainers/{id}    - Обновить тренера
DELETE /admin/trainers/{id}    - Удалить тренера
```

#### Управление секциями
```
GET    /admin/sections/        - Список секций
POST   /admin/sections/        - Создать секцию
PATCH  /admin/sections/{id}    - Обновить секцию
DELETE /admin/sections/{id}    - Удалить секцию
```

#### Управление расписанием
```
GET    /admin/schedule/        - Расписание
POST   /admin/schedule/        - Добавить занятие
PATCH  /admin/schedule/{id}    - Обновить занятие
DELETE /admin/schedule/{id}    - Удалить занятие
```

#### Управление бронированиями
```
GET    /admin/bookings/        - Список бронирований
GET    /admin/bookings/{id}    - Детали бронирования
PATCH  /admin/bookings/{id}    - Изменить статус
```

#### Статистика
```
GET    /admin/stats/dashboard  - Статистика для дашборда
```

#### Сотрудники и роли
```
GET    /admin/employees/       - Список сотрудников
POST   /admin/employees/       - Создать сотрудника
PATCH  /admin/employees/{id}   - Обновить сотрудника
DELETE /admin/employees/{id}   - Удалить сотрудника
GET    /admin/roles/           - Список ролей
```

### 8.3. Health Check
```
GET    /health                 - Проверка работоспособности
HEAD   /health                 - Проверка для uptime роботов
```

---

## 9. Функциональные возможности

### 9.1. Для клиентов

✅ **Регистрация и авторизация**
- Создание учетной записи
- Вход по email и паролю
- Сохранение сессии

✅ **Профиль**
- Просмотр личных данных
- Редактирование контактов
- История бронирований

✅ **Секции**
- Просмотр доступных секций
- Фильтрация по виду спорта и возрасту
- Детальная информация о секции

✅ **Расписание**
- Просмотр расписания всех занятий
- Фильтрация по секции и дню недели
- Информация о тренере и времени

✅ **Бронирование**
- Запись на занятие
- Указание данных ребенка (опционально)
- Отмена записи
- Просмотр своих бронирований

### 9.2. Для администраторов

✅ **Dashboard**
- Общая статистика системы
- Количество клиентов, тренеров, секций
- Количество бронирований
- Быстрый доступ к разделам

✅ **Управление клиентами**
- Просмотр всех клиентов
- Редактирование данных
- Удаление клиентов
- Поиск и фильтрация

✅ **Управление тренерами**
- Добавление новых тренеров
- Редактирование информации
- Удаление тренеров
- Просмотр специализации

✅ **Управление секциями**
- Создание секций
- Настройка возрастных ограничений
- Указание бесплатных секций
- Редактирование и удаление

✅ **Управление расписанием**
- Создание занятий
- Привязка тренера и секции
- Указание времени и места
- Редактирование расписания

✅ **Управление бронированиями**
- Просмотр всех заявок
- Изменение статуса (Ожидание → Подтверждено)
- Отмена бронирований
- Детальная информация

✅ **Управление сотрудниками**
- Добавление администраторов
- Назначение ролей
- Управление доступом

---

## 10. Развертывание проекта

### 10.1. Production окружение

#### Backend (Render)
- **URL:** https://gymflow-oozb.onrender.com
- **База данных:** Neon PostgreSQL
- **Автоматический деплой:** При push в main ветку
- **Environment variables:**
  - `DATABASE_URL` — строка подключения к PostgreSQL
  - `PYTHON_VERSION` — 3.11

#### Frontend (Netlify)
- **URL:** https://gymflowasd.netlify.app
- **Build command:** `npm run build`
- **Publish directory:** `dist`
- **Environment variables:**
  - `VITE_API_URL` — URL backend API

### 10.2. Локальная разработка

#### Backend
```bash
cd back
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend
```bash
cd front
npm install
npm run dev
```

---

## 11. Заключение

### Достигнутые результаты

✅ **Полнофункциональная система** управления спортзалом
✅ **Современный технологический стек** (FastAPI + Vue 3)
✅ **Реляционная база данных** с корректными связями
✅ **RESTful API** с автоматической документацией
✅ **SPA frontend** с роутингом и state management
✅ **Production деплой** на облачных платформах
✅ **Responsive design** (адаптив под мобильные)
✅ **Разграничение прав доступа** (клиенты и админы)

### Применимость в реальных проектах

Разработанная система может быть использована:
- В спортивных клубах и фитнес-центрах
- В детских спортивных школах
- В танцевальных студиях
- В образовательных центрах

### Возможности для расширения

🔮 **Будущие улучшения:**
- Онлайн оплата занятий
- Push-уведомления о занятиях
- Мобильное приложение
- Интеграция с календарем
- Система отзывов о тренерах
- Групповые занятия и абонементы
- QR-коды для отметки посещений
- Аналитика и отчеты
- Многоязычность
- Email рассылки

### Выводы

В ходе разработки проекта были изучены и применены:
- Принципы REST API
- ORM и работа с БД
- Реактивность во frontend
- State management
- Аутентификация и авторизация
- CORS и безопасность
- Cloud deployment
- CI/CD процессы

Проект демонстрирует **полный цикл разработки** веб-приложения — от проектирования базы данных до production деплоя.

---

## 📚 Список использованных технологий

### Backend
- FastAPI 0.104+
- SQLAlchemy 2.0
- PostgreSQL 15
- Pydantic 2.0
- Uvicorn
- Python 3.11

### Frontend
- Vue.js 3.3
- Vite 4.0
- Vue Router 4.0
- Pinia 2.0
- Tailwind CSS 3.3
- Axios 1.6

### DevOps
- Git/GitHub
- Render (backend)
- Netlify (frontend)
- Neon (PostgreSQL)

---

**Дата:** 2025
**Автор:** [Ваше имя]
**Проект:** GymFlow — Система управления спортзалом
**Live Demo:** https://gymflowasd.netlify.app/
