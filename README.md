# GymFlow - Система управления спортзалом

Backend API для системы управления тренажерным залом, построенный на FastAPI + PostgreSQL.

## Технологии

- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy** - ORM для работы с базой данных
- **PostgreSQL** - основная база данных (для продакшена на Neon)
- **SQLite** - для локальной разработки
- **Pydantic** - валидация данных и схемы
- **Uvicorn** - ASGI сервер

## Структура проекта

```
GymFlow/
├── db/                     # База данных
│   ├── database.py        # Конфигурация подключения
│   ├── models.py          # SQLAlchemy модели
│   └── init_data.py       # Тестовые данные
├── schemas/               # Pydantic схемы
│   ├── role.py
│   ├── employee.py
│   ├── user.py
│   ├── trainer.py
│   ├── section.py
│   ├── schedule.py
│   ├── booking.py
│   └── attendance.py
├── routers/               # API роутеры
│   ├── auth.py           # Клиентская авторизация
│   ├── profile.py        # Профиль клиента
│   ├── sections.py       # Секции
│   ├── schedule.py       # Расписание
│   ├── bookings.py       # Бронирования
│   └── admin_*.py        # Админские роутеры
├── main.py               # Точка входа приложения
├── requirements.txt      # Зависимости
├── .env.example         # Пример конфигурации
└── back/                # Документация
    ├── README.md
    ├── GYM_SYSTEM_FULL_ARCHITECTURE.md
    ├── DATABASE_SCHEMA.md
    ├── API_EXAMPLES.md
    └── DEPLOYMENT_GUIDE.md
```

## Быстрый старт

### 1. Установка зависимостей

```bash
# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt
```

### 2. Настройка базы данных

```bash
# Скопировать пример конфигурации
cp .env.example .env

# Для локальной разработки используется SQLite (по умолчанию)
# Для продакшена установите PostgreSQL URL в .env:
# DATABASE_URL=postgresql://user:password@host/database
```

### 3. Запуск сервера

```bash
uvicorn main:app --reload
```

Сервер запустится на http://localhost:8000

### 4. Документация API

После запуска сервера документация доступна на:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Клиентские endpoints

#### Авторизация
- `POST /auth/register` - Регистрация нового клиента
- `POST /auth/login` - Вход клиента
- `GET /auth/me/{user_id}` - Получить данные пользователя

#### Профиль
- `GET /profile/{client_id}` - Получить профиль
- `PATCH /profile/{client_id}` - Обновить профиль

#### Секции
- `GET /sections` - Список секций (с фильтрацией)
- `GET /sections/{id}` - Информация о секции

#### Расписание
- `GET /schedule` - Расписание (с фильтрацией)
- `GET /schedule/{id}` - Элемент расписания

#### Бронирования
- `POST /bookings` - Создать бронирование
- `GET /bookings/client/{id}` - Мои бронирования
- `DELETE /bookings/{id}` - Отменить бронирование

### Админские endpoints

#### Авторизация сотрудников
- `POST /admin/auth/login` - Вход сотрудника
- `GET /admin/auth/me/{employee_id}` - Данные сотрудника

#### Управление клиентами
- `GET /admin/clients` - Все клиенты
- `GET /admin/clients/{id}` - Клиент по ID
- `PATCH /admin/clients/{id}` - Обновить клиента
- `DELETE /admin/clients/{id}` - Удалить клиента

#### Управление тренерами
- `GET /admin/trainers` - Все тренеры
- `POST /admin/trainers` - Создать тренера
- `PATCH /admin/trainers/{id}` - Обновить тренера
- `DELETE /admin/trainers/{id}` - Удалить тренера

#### Управление секциями
- `GET /admin/sections` - Все секции
- `POST /admin/sections` - Создать секцию
- `PATCH /admin/sections/{id}` - Обновить секцию
- `DELETE /admin/sections/{id}` - Удалить секцию

#### Управление расписанием
- `GET /admin/schedule` - Все расписание
- `POST /admin/schedule` - Добавить в расписание
- `PATCH /admin/schedule/{id}` - Обновить расписание
- `DELETE /admin/schedule/{id}` - Удалить из расписания

#### Бронирования
- `GET /admin/bookings` - Все бронирования
- `GET /admin/bookings/{id}` - Бронирование по ID
- `PATCH /admin/bookings/{id}` - Изменить статус
- `GET /admin/bookings/stats/overview` - Статистика

#### Посещаемость
- `GET /admin/attendance` - Вся посещаемость
- `POST /admin/attendance` - Отметить посещение
- `PATCH /admin/attendance/{id}` - Обновить отметку

#### Управление сотрудниками (только Администратор)
- `GET /admin/employees` - Все сотрудники
- `POST /admin/employees` - Создать сотрудника
- `PATCH /admin/employees/{id}` - Обновить сотрудника
- `DELETE /admin/employees/{id}` - Удалить сотрудника

#### Роли
- `GET /admin/roles` - Все роли

#### Статистика
- `GET /admin/stats/dashboard` - Общая статистика

## Тестовые данные

После первого запуска автоматически создаются тестовые данные:

### Клиенты
- Email: `ivanov@mail.ru`, Password: `user123`
- Email: `petrova@gmail.com`, Password: `user123`

### Сотрудники
- Login: `admin@gym.ru`, Password: `admin123` (Администратор)
- Login: `manager@gym.ru`, Password: `manager123` (Менеджер)

## База данных

### Основные таблицы:
- **roles** - роли пользователей
- **employees** - сотрудники системы
- **user_clients** - учетные записи клиентов
- **clients** - информация о клиентах
- **trainers** - тренеры
- **sections** - спортивные секции
- **schedules** - расписание занятий
- **bookings** - бронирования клиентов
- **attendance** - посещаемость

Полная схема БД доступна в `back/DATABASE_SCHEMA.md`

## Деплой на Render + Neon

Подробная инструкция по деплою доступна в `back/DEPLOYMENT_GUIDE.md`

### Краткие шаги:

1. **Создать базу данных на Neon**
   - Регистрация на https://neon.tech
   - Создать проект PostgreSQL
   - Скопировать Connection String

2. **Задеплоить на Render**
   - Регистрация на https://render.com
   - Создать Web Service
   - Подключить GitHub репозиторий
   - Установить переменную окружения `DATABASE_URL`
   - Деплой!

## Разработка

### Запуск в режиме разработки

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Создание миграций (опционально)

Для продакшена рекомендуется использовать Alembic для миграций БД.

## Документация

Полная документация проекта находится в папке `back/`:
- `README.md` - краткое руководство
- `GYM_SYSTEM_FULL_ARCHITECTURE.md` - полная архитектура системы
- `DATABASE_SCHEMA.md` - схема базы данных
- `API_EXAMPLES.md` - примеры использования API
- `DEPLOYMENT_GUIDE.md` - руководство по деплою

## Особенности

- Простая авторизация без JWT (для учебного проекта)
- Пароли хранятся в открытом виде (не для продакшена!)
- Автоматическая инициализация тестовых данных
- CORS открыт для всех источников
- Поддержка SQLite (локально) и PostgreSQL (продакшен)

## Лицензия

Учебный проект

## Автор

Created with Claude Code
