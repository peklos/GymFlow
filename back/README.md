# 🏋️ GymSystem Backend - Quick Start Guide

## 📋 О проекте

**GymSystem** - это учебный backend API для системы управления тренажерным залом, построенный на FastAPI + PostgreSQL (Neon) с деплоем на Render.

**Основной документ:** [GYM_SYSTEM_FULL_ARCHITECTURE.md](./GYM_SYSTEM_FULL_ARCHITECTURE.md) - содержит ПОЛНЫЙ код всех файлов!

---

## 🚀 Быстрый старт (3 шага)

### 1️⃣ Создай базу данных на Neon

1. Зарегистрируйся на [neon.tech](https://neon.tech)
2. Создай новый проект
3. Скопируй **Connection String**
   ```
   postgresql://username:password@ep-xxx-xxx.region.aws.neon.tech/neondb?sslmode=require
   ```

### 2️⃣ Задеплой на Render

1. Зарегистрируйся на [render.com](https://render.com)
2. Создай **New Web Service**
3. Подключи свой GitHub репозиторий
4. Настрой:
   - **Build Command:** `./build.sh`
   - **Start Command:** `./start.sh`
   - **Environment Variable:**
     - `DATABASE_URL` = твой Connection String из Neon
5. Нажми **Create Web Service**

### 3️⃣ Готово! 

После деплоя:
- API: `https://your-app.onrender.com`
- Docs: `https://your-app.onrender.com/docs`
- Health: `https://your-app.onrender.com/health`

---

## 📁 Структура проекта

```
gymsystem_backend/
├── .env.example
├── .gitignore
├── requirements.txt
├── runtime.txt
├── build.sh
├── start.sh
├── main.py
├── db/
│   ├── database.py
│   ├── models.py
│   └── init_data.py
├── schemas/
│   ├── role.py
│   ├── employee.py
│   ├── user.py
│   ├── trainer.py
│   ├── section.py
│   ├── schedule.py
│   ├── booking.py
│   └── attendance.py
└── routers/
    ├── auth.py
    ├── profile.py
    ├── sections.py
    ├── schedule.py
    ├── bookings.py
    ├── employee_auth.py
    ├── admin_users.py
    ├── admin_trainers.py
    ├── admin_sections.py
    ├── admin_schedule.py
    ├── admin_bookings.py
    ├── admin_attendance.py
    ├── admin_employees.py
    ├── admin_roles.py
    └── admin_stats.py
```

---

## 🔑 Тестовые данные

### Клиенты:
| Email | Password |
|-------|----------|
| ivanov@mail.ru | user123 |
| petrova@gmail.com | user123 |

### Сотрудники:
| Login | Password | Роль |
|-------|----------|------|
| admin@gym.ru | admin123 | Администратор |
| manager@gym.ru | manager123 | Менеджер |

---

## 📊 Основные API endpoints

### Клиентские:
- `POST /auth/register` - Регистрация
- `POST /auth/login` - Логин
- `GET /sections` - Список секций
- `GET /schedule` - Расписание
- `POST /bookings` - Создать бронирование

### Админские:
- `POST /admin/auth/login` - Логин сотрудника
- `GET /admin/clients` - Все клиенты
- `GET /admin/trainers` - Все тренеры
- `GET /admin/stats/dashboard` - Статистика

---

## 🛠️ Локальная разработка

```bash
# Клонировать репозиторий
git clone <your-repo>
cd gymsystem_backend

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt

# Создать .env файл
echo "DATABASE_URL=your_neon_connection_string" > .env

# Запустить сервер
uvicorn main:app --reload

# Открыть документацию
open http://localhost:8000/docs
```

---

## 📚 Полная документация

**Весь код со всеми файлами находится в:**  
[GYM_SYSTEM_FULL_ARCHITECTURE.md](./GYM_SYSTEM_FULL_ARCHITECTURE.md)

Этот файл содержит:
- ✅ Полный код всех 40+ файлов
- ✅ SQL схему для PostgreSQL
- ✅ Все Pydantic схемы
- ✅ Все роутеры с полной логикой
- ✅ Инструкции по деплою
- ✅ Тестовые данные
- ✅ Примеры запросов

---

## 🎯 Для Claude Code

Если используешь Claude Code для генерации кода:

1. Закинь файл `GYM_SYSTEM_FULL_ARCHITECTURE.md` в проект
2. Попроси Claude Code:
   ```
   Создай backend по файлу GYM_SYSTEM_FULL_ARCHITECTURE.md.
   Создай все файлы из контрольного списка по порядку.
   ```
3. Claude Code создаст все файлы автоматически!

---

## 📝 Чеклист создания проекта

- [ ] Создать базу данных на Neon
- [ ] Скопировать Connection String
- [ ] Создать все файлы из архитектуры
- [ ] Добавить DATABASE_URL в .env
- [ ] Протестировать локально
- [ ] Запушить на GitHub
- [ ] Задеплоить на Render
- [ ] Проверить работу API

---

## 🔗 Полезные ссылки

- **Neon:** https://neon.tech
- **Render:** https://render.com
- **FastAPI:** https://fastapi.tiangolo.com
- **SQLAlchemy:** https://docs.sqlalchemy.org

---

**Удачи! 🚀💪**
