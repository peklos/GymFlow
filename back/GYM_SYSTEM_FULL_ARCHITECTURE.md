# 🏋️ GymSystem Backend - ПОЛНАЯ АРХИТЕКТУРА И ИНСТРУКЦИИ ДЛЯ РЕАЛИЗАЦИИ

## 📋 ОБЩАЯ ИНФОРМАЦИЯ О ПРОЕКТЕ

**Название:** GymSystem Backend API  
**Стек:** FastAPI + PostgreSQL (Neon) + SQLAlchemy  
**Деплой:** Neon (БД) + Render (Backend) + Netlify (Frontend)  
**Цель:** Учебный проект системы управления тренажерным залом с клиентской частью и админкой  
**Особенности:**
- ❌ БЕЗ хеширования паролей (пароли хранятся в открытом виде)
- ❌ БЕЗ JWT токенов (простая авторизация по email/password)
- ✅ Два типа пользователей: клиенты (users) и сотрудники (employees)
- ✅ Разграничение прав для сотрудников по ролям
- ✅ Система бронирования занятий и секций
- ✅ Управление расписанием и тренерами
- ✅ Отслеживание посещаемости
- ✅ Полный CRUD для всех сущностей
- ✅ PostgreSQL для продакшена (Neon Database)
- ✅ Готово для деплоя на Render
- ✅ Готово для подключения фронтенда на Netlify

---

## 📁 ПОЛНАЯ СТРУКТУРА ПРОЕКТА

```
gymsystem_backend/
│
├── 📄 .env
├── 📄 .env.example
├── 📄 .gitignore
├── 📄 requirements.txt
├── 📄 runtime.txt
├── 📄 build.sh
├── 📄 start.sh
├── 📄 main.py
├── 📄 gymsystem.db (создастся автоматически)
│
├── 📁 db/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── init_data.py
│
├── 📁 schemas/
│   ├── __init__.py
│   ├── user.py (клиенты)
│   ├── employee.py (сотрудники)
│   ├── role.py
│   ├── trainer.py
│   ├── section.py
│   ├── schedule.py
│   ├── booking.py
│   └── attendance.py
│
└── 📁 routers/
    ├── __init__.py
    ├── auth.py (авторизация клиентов)
    ├── profile.py (профиль клиента)
    ├── sections.py (просмотр секций)
    ├── schedule.py (расписание занятий)
    ├── bookings.py (бронирование занятий)
    ├── attendance.py (посещаемость)
    ├── employee_auth.py (авторизация сотрудников)
    ├── admin_users.py (управление клиентами)
    ├── admin_trainers.py (управление тренерами)
    ├── admin_sections.py (управление секциями)
    ├── admin_schedule.py (управление расписанием)
    ├── admin_bookings.py (просмотр всех бронирований)
    ├── admin_attendance.py (управление посещаемостью)
    ├── admin_employees.py (управление сотрудниками)
    ├── admin_roles.py (управление ролями)
    └── admin_stats.py (статистика)
```

---

## 📦 requirements.txt

```txt
fastapi==0.115.0
uvicorn[standard]==0.31.0
sqlalchemy==2.0.35
python-dotenv==1.0.1
pydantic==2.9.2
email-validator==2.2.0
python-multipart==0.0.12
psycopg2-binary==2.9.10
```

---

## 🔐 .env.example

```env
# Database URL
# Продакшен (PostgreSQL на Neon):
# Замените на ваш Connection String из Neon
DATABASE_URL=postgresql://username:password@ep-xxx-xxx.region.aws.neon.tech/neondb?sslmode=require

# Локально для разработки (можно использовать SQLite):
# DATABASE_URL=sqlite:///./gymsystem.db
```

---

## 🗂️ .gitignore

```gitignore
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/
ENV/
*.db
*.sqlite3
.env
.env.local
.vscode/
.idea/
*.swp
*.swo
*.log
```

---

## 🔧 runtime.txt

```
python-3.11
```

---

## ⚙️ build.sh

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 start.sh

```bash
#!/usr/bin/env bash

# Запуск uvicorn на порту, который предоставляет Render
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
```

---

## 🗄️ СТРУКТУРА БАЗЫ ДАННЫХ

### Анализ диаграммы БД:

**Основные сущности:**
1. **Клиенты** (Клиенты) - пользователи системы
2. **Посещаемость** (Посещаемость) - учет посещений
3. **Расписание** (Расписание) - расписание занятий
4. **Заявки** (Заявки) - бронирования на занятия
5. **Тренеры** (Тренеры) - тренерский состав
6. **Секции** (Секции) - секции/направления занятий
7. **Роли** (Роли) - роли сотрудников
8. **User-Сотрудники** - сотрудники с логином
9. **User-Клиенты** - клиенты с логином

### SQL Schema для PostgreSQL (Neon):

```sql
-- === РОЛИ ===
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE INDEX idx_roles_name ON roles(name);

-- === СОТРУДНИКИ (USER-СОТРУДНИКИ) ===
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    login VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE RESTRICT
);

CREATE INDEX idx_employees_login ON employees(login);
CREATE INDEX idx_employees_role_id ON employees(role_id);

-- === КЛИЕНТЫ (USER-КЛИЕНТЫ) ===
CREATE TABLE IF NOT EXISTS user_clients (
    id SERIAL PRIMARY KEY,
    login VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE RESTRICT
);

CREATE INDEX idx_user_clients_login ON user_clients(login);
CREATE INDEX idx_user_clients_role_id ON user_clients(role_id);

-- === КЛИЕНТЫ (ОСНОВНАЯ ИНФОРМАЦИЯ) ===
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    address VARCHAR(255),
    date_of_birth DATE,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES user_clients(id) ON DELETE CASCADE
);

CREATE INDEX idx_clients_full_name ON clients(full_name);
CREATE INDEX idx_clients_phone ON clients(phone);
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_clients_user_id ON clients(user_id);

-- === ТРЕНЕРЫ ===
CREATE TABLE IF NOT EXISTS trainers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    address VARCHAR(255),
    specialization VARCHAR(100)
);

CREATE INDEX idx_trainers_full_name ON trainers(full_name);
CREATE INDEX idx_trainers_email ON trainers(email);
CREATE INDEX idx_trainers_phone ON trainers(phone);

-- === СЕКЦИИ ===
CREATE TABLE IF NOT EXISTS sections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sport_type VARCHAR(50) NOT NULL,
    age_from INTEGER,
    age_to INTEGER,
    is_free BOOLEAN DEFAULT FALSE,
    description TEXT
);

CREATE INDEX idx_sections_name ON sections(name);
CREATE INDEX idx_sections_sport_type ON sections(sport_type);
CREATE INDEX idx_sections_is_free ON sections(is_free);

-- === РАСПИСАНИЕ ===
CREATE TABLE IF NOT EXISTS schedules (
    id SERIAL PRIMARY KEY,
    section_id INTEGER NOT NULL,
    trainer_id INTEGER NOT NULL,
    day_of_week VARCHAR(20) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    location VARCHAR(100),
    FOREIGN KEY (section_id) REFERENCES sections(id) ON DELETE CASCADE,
    FOREIGN KEY (trainer_id) REFERENCES trainers(id) ON DELETE RESTRICT
);

CREATE INDEX idx_schedules_section_id ON schedules(section_id);
CREATE INDEX idx_schedules_trainer_id ON schedules(trainer_id);
CREATE INDEX idx_schedules_day_of_week ON schedules(day_of_week);

-- === ЗАЯВКИ (БРОНИРОВАНИЯ) ===
CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    booking_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status VARCHAR(30) DEFAULT 'pending',
    child_full_name VARCHAR(100),
    child_age INTEGER,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES sections(id) ON DELETE CASCADE
);

CREATE INDEX idx_bookings_client_id ON bookings(client_id);
CREATE INDEX idx_bookings_section_id ON bookings(section_id);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_bookings_booking_date ON bookings(booking_date);

-- === ПОСЕЩАЕМОСТЬ ===
CREATE TABLE IF NOT EXISTS attendance (
    id SERIAL PRIMARY KEY,
    booking_id INTEGER,
    schedule_id INTEGER NOT NULL,
    visit_date DATE NOT NULL DEFAULT CURRENT_DATE,
    was_present BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE SET NULL,
    FOREIGN KEY (schedule_id) REFERENCES schedules(id) ON DELETE CASCADE
);

CREATE INDEX idx_attendance_booking_id ON attendance(booking_id);
CREATE INDEX idx_attendance_schedule_id ON attendance(schedule_id);
CREATE INDEX idx_attendance_visit_date ON attendance(visit_date);
CREATE INDEX idx_attendance_was_present ON attendance(was_present);
```

---

## 🏗️ ФАЙЛЫ ПРОЕКТА - ПОЛНЫЙ КОД

### 1️⃣ db/database.py

```python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./gymsystem.db")

# Определяем connect_args в зависимости от типа БД
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# Для PostgreSQL на Render нужно заменить postgres:// на postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,  # Проверка соединения перед использованием
    echo=False  # Отключаем SQL логи в продакшене
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

### 2️⃣ db/models.py

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Boolean, Text, Index
from sqlalchemy.orm import relationship
from datetime import date
from .database import Base

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    
    employees = relationship('Employee', back_populates='role')
    user_clients = relationship('UserClient', back_populates='role')


class Employee(Base):
    """Сотрудники системы с авторизацией"""
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False, index=True)
    
    role = relationship('Role', back_populates='employees')


class UserClient(Base):
    """Учетные записи клиентов для авторизации"""
    __tablename__ = 'user_clients'
    
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False, index=True)
    
    role = relationship('Role', back_populates='user_clients')
    client = relationship('Client', back_populates='user', uselist=False)


class Client(Base):
    """Клиенты - основная информация"""
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user_clients.id'), unique=True)
    full_name = Column(String(100), nullable=False, index=True)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    address = Column(String(255))
    date_of_bi
---

### 1️⃣7️⃣ routers/employee_auth.py (Авторизация сотрудников)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import employee as employee_schemas

router = APIRouter(prefix="/admin/auth", tags=["Авторизация сотрудников"])

@router.post("/login")
def employee_login(login_data: employee_schemas.EmployeeLogin, db: Session = Depends(database.get_db)):
    """Вход сотрудника"""
    employee = db.query(models.Employee).filter(models.Employee.login == login_data.login).first()
    
    if not employee or employee.password != login_data.password:
        raise HTTPException(status_code=401, detail="Неверный login или пароль")
    
    # Получаем роль
    role = db.query(models.Role).filter(models.Role.id == employee.role_id).first()
    
    return {
        "message": "Вход выполнен успешно",
        "employee": {
            "id": employee.id,
            "login": employee.login,
            "role": role.name if role else None,
            "role_id": employee.role_id
        }
    }

@router.get("/me/{employee_id}", response_model=employee_schemas.EmployeeResponse)
def get_current_employee(employee_id: int, db: Session = Depends(database.get_db)):
    """Получить данные текущего сотрудника"""
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    
    return employee
```

---

### 1️⃣8️⃣ routers/admin_users.py (Управление клиентами)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import user as user_schemas
from typing import List

router = APIRouter(prefix="/admin/clients", tags=["Админ: Клиенты"])

@router.get("/", response_model=List[user_schemas.ClientResponse])
def get_all_clients(db: Session = Depends(database.get_db)):
    """Получить всех клиентов"""
    clients = db.query(models.Client).all()
    return clients

@router.get("/{client_id}", response_model=user_schemas.ClientResponse)
def get_client(client_id: int, db: Session = Depends(database.get_db)):
    """Получить клиента по ID"""
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    return client

@router.patch("/{client_id}", response_model=user_schemas.ClientResponse)
def update_client(client_id: int, client_data: user_schemas.ClientUpdate, db: Session = Depends(database.get_db)):
    """Обновить данные клиента"""
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    if client_data.full_name:
        client.full_name = client_data.full_name
    if client_data.phone:
        client.phone = client_data.phone
    if client_data.email:
        client.email = client_data.email
    if client_data.address:
        client.address = client_data.address
    if client_data.date_of_birth:
        client.date_of_birth = client_data.date_of_birth
    
    db.commit()
    db.refresh(client)
    
    return client

@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(database.get_db)):
    """Удалить клиента"""
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    db.delete(client)
    db.commit()
    
    return {"message": "Клиент удален", "client_id": client_id}
```

---

### 1️⃣9️⃣ routers/admin_trainers.py (Управление тренерами)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import trainer as trainer_schemas
from typing import List

router = APIRouter(prefix="/admin/trainers", tags=["Админ: Тренеры"])

@router.get("/", response_model=List[trainer_schemas.TrainerResponse])
def get_all_trainers(db: Session = Depends(database.get_db)):
    """Получить всех тренеров"""
    trainers = db.query(models.Trainer).all()
    return trainers

@router.post("/", response_model=trainer_schemas.TrainerResponse)
def create_trainer(trainer_data: trainer_schemas.TrainerCreate, db: Session = Depends(database.get_db)):
    """Создать нового тренера"""
    # Проверка email
    existing_email = db.query(models.Trainer).filter(models.Trainer.email == trainer_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email уже используется")
    
    # Проверка телефона
    existing_phone = db.query(models.Trainer).filter(models.Trainer.phone == trainer_data.phone).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Телефон уже используется")
    
    new_trainer = models.Trainer(
        full_name=trainer_data.full_name,
        email=trainer_data.email,
        phone=trainer_data.phone,
        address=trainer_data.address,
        specialization=trainer_data.specialization
    )
    
    db.add(new_trainer)
    db.commit()
    db.refresh(new_trainer)
    
    return new_trainer

@router.patch("/{trainer_id}", response_model=trainer_schemas.TrainerResponse)
def update_trainer(trainer_id: int, trainer_data: trainer_schemas.TrainerUpdate, db: Session = Depends(database.get_db)):
    """Обновить данные тренера"""
    trainer = db.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()
    
    if not trainer:
        raise HTTPException(status_code=404, detail="Тренер не найден")
    
    if trainer_data.full_name:
        trainer.full_name = trainer_data.full_name
    if trainer_data.email:
        trainer.email = trainer_data.email
    if trainer_data.phone:
        trainer.phone = trainer_data.phone
    if trainer_data.address:
        trainer.address = trainer_data.address
    if trainer_data.specialization:
        trainer.specialization = trainer_data.specialization
    
    db.commit()
    db.refresh(trainer)
    
    return trainer

@router.delete("/{trainer_id}")
def delete_trainer(trainer_id: int, db: Session = Depends(database.get_db)):
    """Удалить тренера"""
    trainer = db.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()
    
    if not trainer:
        raise HTTPException(status_code=404, detail="Тренер не найден")
    
    db.delete(trainer)
    db.commit()
    
    return {"message": "Тренер удален", "trainer_id": trainer_id}
```

---

### 2️⃣0️⃣ routers/admin_sections.py (Управление секциями)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import section as section_schemas
from typing import List

router = APIRouter(prefix="/admin/sections", tags=["Админ: Секции"])

@router.get("/", response_model=List[section_schemas.SectionResponse])
def get_all_sections(db: Session = Depends(database.get_db)):
    """Получить все секции"""
    sections = db.query(models.Section).all()
    return sections

@router.post("/", response_model=section_schemas.SectionResponse)
def create_section(section_data: section_schemas.SectionCreate, db: Session = Depends(database.get_db)):
    """Создать новую секцию"""
    new_section = models.Section(
        name=section_data.name,
        sport_type=section_data.sport_type,
        age_from=section_data.age_from,
        age_to=section_data.age_to,
        is_free=section_data.is_free,
        description=section_data.description
    )
    
    db.add(new_section)
    db.commit()
    db.refresh(new_section)
    
    return new_section

@router.patch("/{section_id}", response_model=section_schemas.SectionResponse)
def update_section(section_id: int, section_data: section_schemas.SectionUpdate, db: Session = Depends(database.get_db)):
    """Обновить секцию"""
    section = db.query(models.Section).filter(models.Section.id == section_id).first()
    
    if not section:
        raise HTTPException(status_code=404, detail="Секция не найдена")
    
    if section_data.name:
        section.name = section_data.name
    if section_data.sport_type:
        section.sport_type = section_data.sport_type
    if section_data.age_from is not None:
        section.age_from = section_data.age_from
    if section_data.age_to is not None:
        section.age_to = section_data.age_to
    if section_data.is_free is not None:
        section.is_free = section_data.is_free
    if section_data.description:
        section.description = section_data.description
    
    db.commit()
    db.refresh(section)
    
    return section

@router.delete("/{section_id}")
def delete_section(section_id: int, db: Session = Depends(database.get_db)):
    """Удалить секцию"""
    section = db.query(models.Section).filter(models.Section.id == section_id).first()
    
    if not section:
        raise HTTPException(status_code=404, detail="Секция не найдена")
    
    db.delete(section)
    db.commit()
    
    return {"message": "Секция удалена", "section_id": section_id}
```

---

### 2️⃣1️⃣ routers/admin_schedule.py (Управление расписанием)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import schedule as schedule_schemas
from typing import List

router = APIRouter(prefix="/admin/schedule", tags=["Админ: Расписание"])

@router.get("/", response_model=List[schedule_schemas.ScheduleResponse])
def get_all_schedules(db: Session = Depends(database.get_db)):
    """Получить все расписание"""
    schedules = db.query(models.Schedule).all()
    return schedules

@router.post("/", response_model=schedule_schemas.ScheduleResponse)
def create_schedule(schedule_data: schedule_schemas.ScheduleCreate, db: Session = Depends(database.get_db)):
    """Создать элемент расписания"""
    # Проверка секции
    section = db.query(models.Section).filter(models.Section.id == schedule_data.section_id).first()
    if not section:
        raise HTTPException(status_code=404, detail="Секция не найдена")
    
    # Проверка тренера
    trainer = db.query(models.Trainer).filter(models.Trainer.id == schedule_data.trainer_id).first()
    if not trainer:
        raise HTTPException(status_code=404, detail="Тренер не найден")
    
    new_schedule = models.Schedule(
        section_id=schedule_data.section_id,
        trainer_id=schedule_data.trainer_id,
        day_of_week=schedule_data.day_of_week,
        start_time=schedule_data.start_time,
        end_time=schedule_data.end_time,
        location=schedule_data.location
    )
    
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    
    return new_schedule

@router.patch("/{schedule_id}", response_model=schedule_schemas.ScheduleResponse)
def update_schedule(schedule_id: int, schedule_data: schedule_schemas.ScheduleUpdate, db: Session = Depends(database.get_db)):
    """Обновить элемент расписания"""
    schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()
    
    if not schedule:
        raise HTTPException(status_code=404, detail="Элемент расписания не найден")
    
    if schedule_data.section_id:
        schedule.section_id = schedule_data.section_id
    if schedule_data.trainer_id:
        schedule.trainer_id = schedule_data.trainer_id
    if schedule_data.day_of_week:
        schedule.day_of_week = schedule_data.day_of_week
    if schedule_data.start_time:
        schedule.start_time = schedule_data.start_time
    if schedule_data.end_time:
        schedule.end_time = schedule_data.end_time
    if schedule_data.location:
        schedule.location = schedule_data.location
    
    db.commit()
    db.refresh(schedule)
    
    return schedule

@router.delete("/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(database.get_db)):
    """Удалить элемент расписания"""
    schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()
    
    if not schedule:
        raise HTTPException(status_code=404, detail="Элемент расписания не найден")
    
    db.delete(schedule)
    db.commit()
    
    return {"message": "Элемент расписания удален", "schedule_id": schedule_id}
```

---

### 2️⃣2️⃣ routers/admin_bookings.py (Просмотр всех бронирований)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import booking as booking_schemas
from typing import List

router = APIRouter(prefix="/admin/bookings", tags=["Админ: Бронирования"])

@router.get("/", response_model=List[booking_schemas.BookingResponse])
def get_all_bookings(db: Session = Depends(database.get_db)):
    """Получить все бронирования"""
    bookings = db.query(models.Booking).all()
    return bookings

@router.get("/{booking_id}", response_model=booking_schemas.BookingResponse)
def get_booking(booking_id: int, db: Session = Depends(database.get_db)):
    """Получить бронирование по ID"""
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    
    if not booking:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    
    return booking

@router.patch("/{booking_id}", response_model=booking_schemas.BookingResponse)
def update_booking_status(booking_id: int, update_data: booking_schemas.BookingUpdate, db: Session = Depends(database.get_db)):
    """Обновить статус бронирования"""
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    
    if not booking:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    
    booking.status = update_data.status
    
    db.commit()
    db.refresh(booking)
    
    return booking

@router.get("/stats/overview")
def get_bookings_stats(db: Session = Depends(database.get_db)):
    """Статистика по бронированиям"""
    total = db.query(models.Booking).count()
    pending = db.query(models.Booking).filter(models.Booking.status == "pending").count()
    approved = db.query(models.Booking).filter(models.Booking.status == "approved").count()
    rejected = db.query(models.Booking).filter(models.Booking.status == "rejected").count()
    cancelled = db.query(models.Booking).filter(models.Booking.status == "cancelled").count()
    
    return {
        "total_bookings": total,
        "pending_bookings": pending,
        "approved_bookings": approved,
        "rejected_bookings": rejected,
        "cancelled_bookings": cancelled
    }
```

---

### 2️⃣3️⃣ routers/admin_attendance.py (Управление посещаемостью)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import attendance as attendance_schemas
from typing import List

router = APIRouter(prefix="/admin/attendance", tags=["Админ: Посещаемость"])

@router.get("/", response_model=List[attendance_schemas.AttendanceResponse])
def get_all_attendance(db: Session = Depends(database.get_db)):
    """Получить всю посещаемость"""
    attendance = db.query(models.Attendance).all()
    return attendance

@router.post("/", response_model=attendance_schemas.AttendanceResponse)
def create_attendance(attendance_data: attendance_schemas.AttendanceCreate, db: Session = Depends(database.get_db)):
    """Отметить посещение"""
    new_attendance = models.Attendance(
        booking_id=attendance_data.booking_id,
        schedule_id=attendance_data.schedule_id,
        visit_date=attendance_data.visit_date,
        was_present=attendance_data.was_present
    )
    
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    
    return new_attendance

@router.patch("/{attendance_id}", response_model=attendance_schemas.AttendanceResponse)
def update_attendance(attendance_id: int, update_data: attendance_schemas.AttendanceUpdate, db: Session = Depends(database.get_db)):
    """Обновить отметку посещения"""
    attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    
    if not attendance:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    
    attendance.was_present = update_data.was_present
    
    db.commit()
    db.refresh(attendance)
    
    return attendance
```

---

### 2️⃣4️⃣ routers/admin_employees.py (Управление сотрудниками)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import employee as employee_schemas
from typing import List

router = APIRouter(prefix="/admin/employees", tags=["Админ: Сотрудники"])

@router.get("/", response_model=List[employee_schemas.EmployeeResponse])
def get_all_employees(admin_id: int, db: Session = Depends(database.get_db)):
    """Получить всех сотрудников (только для Администратора)"""
    # Проверка прав (role_id=1 это Администратор)
    admin = db.query(models.Employee).filter(models.Employee.id == admin_id).first()
    if not admin or admin.role_id != 1:
        raise HTTPException(status_code=403, detail="Доступ запрещен. Требуется роль Администратора")
    
    employees = db.query(models.Employee).all()
    return employees

@router.post("/", response_model=employee_schemas.EmployeeResponse)
def create_employee(employee_data: employee_schemas.EmployeeCreate, admin_id: int, db: Session = Depends(database.get_db)):
    """Создать нового сотрудника (только для Администратора)"""
    # Проверка прав
    admin = db.query(models.Employee).filter(models.Employee.id == admin_id).first()
    if not admin or admin.role_id != 1:
        raise HTTPException(status_code=403, detail="Доступ запрещен")
    
    # Проверка login
    existing = db.query(models.Employee).filter(models.Employee.login == employee_data.login).first()
    if existing:
        raise HTTPException(status_code=400, detail="Login уже используется")
    
    new_employee = models.Employee(
        login=employee_data.login,
        password=employee_data.password,
        role_id=employee_data.role_id
    )
    
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    
    return new_employee

@router.patch("/{emp_id}", response_model=employee_schemas.EmployeeResponse)
def update_employee(emp_id: int, employee_data: employee_schemas.EmployeeUpdate, admin_id: int, db: Session = Depends(database.get_db)):
    """Обновить сотрудника (только для Администратора)"""
    # Проверка прав
    admin = db.query(models.Employee).filter(models.Employee.id == admin_id).first()
    if not admin or admin.role_id != 1:
        raise HTTPException(status_code=403, detail="Доступ запрещен")
    
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    
    if employee_data.login:
        employee.login = employee_data.login
    if employee_data.password:
        employee.password = employee_data.password
    if employee_data.role_id:
        employee.role_id = employee_data.role_id
    
    db.commit()
    db.refresh(employee)
    
    return employee

@router.delete("/{emp_id}")
def delete_employee(emp_id: int, admin_id: int, db: Session = Depends(database.get_db)):
    """Удалить сотрудника (только для Администратора)"""
    # Проверка прав
    admin = db.query(models.Employee).filter(models.Employee.id == admin_id).first()
    if not admin or admin.role_id != 1:
        raise HTTPException(status_code=403, detail="Доступ запрещен")
    
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    
    db.delete(employee)
    db.commit()
    
    return {"message": "Сотрудник удален", "employee_id": emp_id}
```

---

### 2️⃣5️⃣ routers/admin_roles.py (Просмотр ролей)

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import models, database
from schemas import role as role_schemas
from typing import List

router = APIRouter(prefix="/admin/roles", tags=["Админ: Роли"])

@router.get("/", response_model=List[role_schemas.RoleResponse])
def get_all_roles(db: Session = Depends(database.get_db)):
    """Получить все роли"""
    roles = db.query(models.Role).all()
    return roles
```

---

### 2️⃣6️⃣ routers/admin_stats.py (Статистика)

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from db import models, database
from datetime import datetime, timedelta

router = APIRouter(prefix="/admin/stats", tags=["Админ: Статистика"])

@router.get("/dashboard")
def get_dashboard_stats(db: Session = Depends(database.get_db)):
    """Получить общую статистику для дашборда"""
    
    # Общие показатели
    total_clients = db.query(models.Client).count()
    total_trainers = db.query(models.Trainer).count()
    total_sections = db.query(models.Section).count()
    total_bookings = db.query(models.Booking).count()
    
    # Статусы бронирований
    pending_bookings = db.query(models.Booking).filter(models.Booking.status == "pending").count()
    approved_bookings = db.query(models.Booking).filter(models.Booking.status == "approved").count()
    
    # Посещаемость
    total_visits = db.query(models.Attendance).count()
    present_visits = db.query(models.Attendance).filter(models.Attendance.was_present == True).count()
    attendance_rate = round((present_visits / total_visits * 100) if total_visits > 0 else 0, 2)
    
    # Популярные секции (топ-5 по количеству бронирований)
    popular_sections = db.query(
        models.Section.id,
        models.Section.name,
        models.Section.sport_type,
        func.count(models.Booking.id).label("bookings_count")
    ).join(
        models.Booking, models.Section.id == models.Booking.section_id
    ).group_by(
        models.Section.id
    ).order_by(
        func.count(models.Booking.id).desc()
    ).limit(5).all()
    
    popular_sections_list = [
        {
            "id": s.id,
            "name": s.name,
            "sport_type": s.sport_type,
            "bookings_count": s.bookings_count
        }
        for s in popular_sections
    ]
    
    # Активные клиенты (топ-5 по количеству бронирований)
    active_clients = db.query(
        models.Client.id,
        models.Client.full_name,
        models.Client.email,
        func.count(models.Booking.id).label("bookings_count")
    ).join(
        models.Booking, models.Client.id == models.Booking.client_id
    ).group_by(
        models.Client.id
    ).order_by(
        func.count(models.Booking.id).desc()
    ).limit(5).all()
    
    active_clients_list = [
        {
            "id": c.id,
            "full_name": c.full_name,
            "email": c.email,
            "bookings_count": c.bookings_count
        }
        for c in active_clients
    ]
    
    return {
        "overview": {
            "total_clients": total_clients,
            "total_trainers": total_trainers,
            "total_sections": total_sections,
            "total_bookings": total_bookings
        },
        "bookings": {
            "pending": pending_bookings,
            "approved": approved_bookings
        },
        "attendance": {
            "total_visits": total_visits,
            "present_visits": present_visits,
            "attendance_rate": attendance_rate
        },
        "popular_sections": popular_sections_list,
        "active_clients": active_clients_list
    }
```

---

### 2️⃣7️⃣ main.py (Главный файл приложения)

```python
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
```

---

## 🚀 ИНСТРУКЦИИ ПО ЗАПУСКУ

### Локальная разработка:

1. **Клонировать репозиторий:**
```bash
git clone <your-repo-url>
cd gymsystem_backend
```

2. **Создать виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Установить зависимости:**
```bash
pip install -r requirements.txt
```

4. **Создать .env файл:**
```env
DATABASE_URL=postgresql://username:password@host/database?sslmode=require
```

5. **Запустить сервер:**
```bash
uvicorn main:app --reload
```

6. **Открыть документацию:**
```
http://localhost:8000/docs
```

---

### Деплой на Neon + Render:

#### 1️⃣ Создание базы данных на Neon:

1. Зарегистрируйтесь на [neon.tech](https://neon.tech)
2. Создайте новый проект
3. Скопируйте Connection String
4. Формат: `postgresql://username:password@ep-xxx-xxx.region.aws.neon.tech/neondb?sslmode=require`

#### 2️⃣ Деплой на Render:

1. Создайте аккаунт на [render.com](https://render.com)
2. Создайте новый Web Service
3. Подключите GitHub репозиторий
4. Настройки:
   - **Build Command:** `./build.sh`
   - **Start Command:** `./start.sh`
   - **Environment Variables:**
     - `DATABASE_URL` = ваш Connection String из Neon
5. Нажмите "Create Web Service"

#### 3️⃣ Проверка деплоя:

После успешного деплоя:
- API будет доступен по адресу: `https://your-app.onrender.com`
- Документация: `https://your-app.onrender.com/docs`
- Health check: `https://your-app.onrender.com/health`

---

## 📊 ТЕСТОВЫЕ ДАННЫЕ

### 👤 КЛИЕНТЫ (user_clients):
| Email | Password |
|-------|----------|
| ivanov@mail.ru | user123 |
| petrova@gmail.com | user123 |
| sidorov@yandex.ru | user123 |
| kozlova@mail.ru | user123 |
| novikov@gmail.com | user123 |

### 🔧 СОТРУДНИКИ (employees):
| Login | Password | Роль |
|-------|----------|------|
| admin@gym.ru | admin123 | Администратор |
| manager@gym.ru | manager123 | Менеджер |
| trainer1@gym.ru | trainer123 | Тренер |

### 🏋️ ТРЕНЕРЫ:
- Смирнов Алексей Петрович (Фитнес)
- Васильева Елена Игоревна (Йога)
- Кузнецов Сергей Николаевич (Бокс)
- Михайлова Ольга Андреевна (Плавание)
- Федоров Игорь Викторович (Карате)

### 📋 СЕКЦИИ:
- Общий фитнес
- Йога для начинающих
- Бокс для взрослых
- Детское плавание
- Карате для детей
- Утренняя зарядка (бесплатно)
- Кроссфит
- Пилатес

---

## 🎯 API ENDPOINTS (ПОЛНЫЙ СПИСОК)

### 👤 КЛИЕНТСКИЕ:
```
POST   /auth/register           - Регистрация
POST   /auth/login              - Логин
GET    /auth/me/{user_id}       - Текущий пользователь

GET    /profile/{client_id}     - Профиль
PATCH  /profile/{client_id}     - Обновить профиль

GET    /sections                - Список секций (с фильтрами)
GET    /sections/{id}           - Инфо о секции

GET    /schedule                - Расписание (с фильтрами)
GET    /schedule/{id}           - Элемент расписания

POST   /bookings?client_id=X    - Создать бронирование
GET    /bookings/client/{id}    - Мои бронирования
DELETE /bookings/{id}           - Отменить бронирование
```

### 🔧 АДМИНСКИЕ:
```
POST   /admin/auth/login                 - Логин сотрудника
GET    /admin/auth/me/{employee_id}      - Текущий сотрудник

GET    /admin/clients                    - Все клиенты
GET    /admin/clients/{id}               - Инфо о клиенте
PATCH  /admin/clients/{id}               - Обновить клиента
DELETE /admin/clients/{id}               - Удалить клиента

GET    /admin/trainers                   - Все тренеры
POST   /admin/trainers                   - Добавить тренера
PATCH  /admin/trainers/{id}              - Обновить тренера
DELETE /admin/trainers/{id}              - Удалить тренера

GET    /admin/sections                   - Все секции
POST   /admin/sections                   - Добавить секцию
PATCH  /admin/sections/{id}              - Обновить секцию
DELETE /admin/sections/{id}              - Удалить секцию

GET    /admin/schedule                   - Все расписание
POST   /admin/schedule                   - Добавить в расписание
PATCH  /admin/schedule/{id}              - Обновить расписание
DELETE /admin/schedule/{id}              - Удалить из расписания

GET    /admin/bookings                   - Все бронирования
GET    /admin/bookings/{id}              - Инфо о бронировании
PATCH  /admin/bookings/{id}              - Изменить статус
GET    /admin/bookings/stats/overview    - Статистика

GET    /admin/attendance                 - Вся посещаемость
POST   /admin/attendance                 - Отметить посещение
PATCH  /admin/attendance/{id}            - Обновить отметку

GET    /admin/employees?admin_id=X       - Все сотрудники (Админ)
POST   /admin/employees?admin_id=X       - Добавить сотрудника (Админ)
PATCH  /admin/employees/{id}?admin_id=X  - Обновить сотрудника (Админ)
DELETE /admin/employees/{id}?admin_id=X  - Удалить сотрудника (Админ)

GET    /admin/roles                      - Все роли

GET    /admin/stats/dashboard            - Дашборд статистики
```

---

## ✅ КОНТРОЛЬНЫЙ СПИСОК ДЛЯ РЕАЛИЗАЦИИ

### Файлы конфигурации:
- [ ] .env
- [ ] .env.example
- [ ] .gitignore
- [ ] requirements.txt
- [ ] runtime.txt
- [ ] build.sh
- [ ] start.sh

### Файлы БД:
- [ ] db/__init__.py
- [ ] db/database.py
- [ ] db/models.py
- [ ] db/init_data.py

### Схемы:
- [ ] schemas/__init__.py
- [ ] schemas/role.py
- [ ] schemas/employee.py
- [ ] schemas/user.py
- [ ] schemas/trainer.py
- [ ] schemas/section.py
- [ ] schemas/schedule.py
- [ ] schemas/booking.py
- [ ] schemas/attendance.py

### Роутеры клиентов:
- [ ] routers/__init__.py
- [ ] routers/auth.py
- [ ] routers/profile.py
- [ ] routers/sections.py
- [ ] routers/schedule.py
- [ ] routers/bookings.py

### Роутеры админов:
- [ ] routers/employee_auth.py
- [ ] routers/admin_users.py
- [ ] routers/admin_trainers.py
- [ ] routers/admin_sections.py
- [ ] routers/admin_schedule.py
- [ ] routers/admin_bookings.py
- [ ] routers/admin_attendance.py
- [ ] routers/admin_employees.py
- [ ] routers/admin_roles.py
- [ ] routers/admin_stats.py

### Главный файл:
- [ ] main.py

---

## 🎓 ВАЖНЫЕ ЗАМЕЧАНИЯ

1. **БЕЗ БЕЗОПАСНОСТИ**: Пароли хранятся в открытом виде, нет JWT токенов - это учебный проект
2. **Простая авторизация**: Авторизация через передачу user_id, client_id или employee_id в query параметрах
3. **PostgreSQL**: База данных на Neon (managed PostgreSQL)
4. **Автоинициализация**: Тестовые данные заполнятся автоматически при первом запуске
5. **CORS открыт**: Разрешены все origins для удобства разработки фронтенда
6. **Swagger UI**: Доступен по адресу /docs для тестирования API
7. **Деплой**: Готово для деплоя на Render + Neon + Netlify

---

## 🔄 ЛОГИКА РАБОТЫ

### Клиенты:
1. Регистрация → Логин → Получение user_id и client_id
2. Просмотр доступных секций (с фильтрацией)
3. Просмотр расписания занятий
4. Создание бронирования на секцию
5. Просмотр своих бронирований
6. Отмена бронирования

### Админы:
1. Логин сотрудника → Получение employee_id и role_id
2. Управление клиентами, тренерами, секциями
3. Управление расписанием
4. Просмотр и одобрение бронирований
5. Отметка посещаемости
6. Администратор (role_id=1) имеет доступ ко всему
7. Менеджер, Тренер имеют ограниченный доступ

---

## 📝 ПРИМЕРЫ ЗАПРОСОВ

### Регистрация клиента:
```json
POST /auth/register
{
  "user_data": {
    "login": "test@test.ru",
    "password": "test123"
  },
  "client_data": {
    "full_name": "Тестов Тест Тестович",
    "phone": "+79991234567",
    "email": "test@test.ru",
    "address": "Москва, ул. Тестовая, 1",
    "date_of_birth": "1995-01-15"
  }
}
```

### Создание бронирования:
```json
POST /bookings?client_id=1
{
  "section_id": 1,
  "child_full_name": null,
  "child_age": null
}
```

### Отметка посещения:
```json
POST /admin/attendance
{
  "booking_id": 1,
  "schedule_id": 1,
  "visit_date": "2024-03-10",
  "was_present": true
}
```

---

## 🎯 ГОТОВО К ИСПОЛЬЗОВАНИЮ

Этот файл содержит ВСЁ необходимое для полной реализации бэкенда GymSystem:
- ✅ Полный код всех файлов
- ✅ Структура проекта
- ✅ База данных PostgreSQL для Neon
- ✅ Все роутеры и endpoints
- ✅ Тестовые данные
- ✅ Инструкции по деплою на Render + Neon
- ✅ Примеры запросов

Просто создавай файлы по порядку из контрольного списка, копируй код из этого документа, настрой Neon и Render - и всё заработает! 🚀

---

## 📚 ДОПОЛНИТЕЛЬНЫЕ ССЫЛКИ

- **Neon Database:** https://neon.tech
- **Render:** https://render.com
- **Netlify:** https://www.netlify.com
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **SQLAlchemy Docs:** https://docs.sqlalchemy.org

---

**Удачи в разработке! 💪🏋️**
