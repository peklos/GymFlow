from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base, SessionLocal
from db.init_data import initialize_database

# Роутеры клиентов
from routers import auth
from routers import profile
from routers import sections
from routers import schedule
from routers import bookings

# Роутеры админов
from routers import employee_auth
from routers import admin_users
from routers import admin_trainers
from routers import admin_sections
from routers import admin_schedule
from routers import admin_bookings
from routers import admin_attendance
from routers import admin_employees
from routers import admin_roles
from routers import admin_stats

app = FastAPI(
    title="GymSystem API",
    description="API для системы управления тренажерным залом (учебный проект)",
    version="1.0.0"
)

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Инициализация начальных данных
db = SessionLocal()
try:
    initialize_database(db)
finally:
    db.close()

# CORS (разрешаем все для учебного проекта)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# === КЛИЕНТСКИЕ РОУТЕРЫ ===
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(sections.router)
app.include_router(schedule.router)
app.include_router(bookings.router)

# === АДМИНСКИЕ РОУТЕРЫ ===
app.include_router(employee_auth.router)
app.include_router(admin_users.router)
app.include_router(admin_trainers.router)
app.include_router(admin_sections.router)
app.include_router(admin_schedule.router)
app.include_router(admin_bookings.router)
app.include_router(admin_attendance.router)
app.include_router(admin_employees.router)
app.include_router(admin_roles.router)
app.include_router(admin_stats.router)

@app.get("/", tags=["Main"])
def root():
    return {
        "message": "GymSystem API работает",
        "version": "1.0.0",
        "docs": "/docs",
        "client_endpoints": "/auth, /profile, /sections, /schedule, /bookings",
        "admin_endpoints": "/admin/auth, /admin/clients, /admin/trainers, /admin/sections, /admin/schedule, /admin/bookings, /admin/attendance, /admin/employees, /admin/roles, /admin/stats"
    }

@app.get("/health", tags=["Health"])
@app.head("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
