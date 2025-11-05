# GymFlow 💪

![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=flat&logo=vue.js&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=flat&logo=postgresql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.x-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)

Система управления спортивным залом с полнофункциональным API и современным веб-интерфейсом.

## 🚀 Live Demo

**Frontend:** [https://gymflowasd.netlify.app/](https://gymflowasd.netlify.app/)

## 📦 Стек технологий

### Backend
- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy** - ORM для работы с базой данных
- **PostgreSQL** - основная база данных (Neon)
- **Pydantic** - валидация данных

### Frontend
- **Vue 3** - прогрессивный JavaScript фреймворк
- **Vite** - быстрый сборщик
- **Pinia** - управление состоянием
- **Tailwind CSS** - utility-first CSS фреймворк
- **Axios** - HTTP клиент

## ✨ Функционал

- 🔐 Авторизация клиентов и администраторов
- 👥 Управление клиентами
- 🏋️ Управление тренерами
- 📋 Управление секциями и расписанием
- 📅 Система бронирования занятий
- 📊 Административная панель со статистикой
- 👤 Профили пользователей

## 🏗️ Структура проекта

```
GymFlow/
├── back/          # Backend (FastAPI)
│   ├── db/        # Модели и база данных
│   ├── routers/   # API endpoints
│   └── schemas/   # Pydantic схемы
└── front/         # Frontend (Vue 3)
    ├── src/
    │   ├── api/       # API сервисы
    │   ├── views/     # Страницы
    │   ├── components/# Компоненты
    │   └── stores/    # Pinia stores
    └── public/
```

## 🛠️ Локальная разработка

### Backend
```bash
cd back
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd front
npm install
npm run dev
```

## 📝 API Documentation

После запуска backend документация доступна по адресу:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📄 License

MIT
