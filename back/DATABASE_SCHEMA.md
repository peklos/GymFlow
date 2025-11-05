# 🗺️ GymSystem - Схема базы данных и связей

## 📊 Диаграмма связей таблиц

```
┌─────────────────┐
│     ROLES       │
│─────────────────│
│ id (PK)         │
│ name            │
└────────┬────────┘
         │
         ├──────────────────┐
         │                  │
┌────────▼────────┐  ┌──────▼──────────┐
│   EMPLOYEES     │  │  USER_CLIENTS   │
│─────────────────│  │─────────────────│
│ id (PK)         │  │ id (PK)         │
│ login           │  │ login           │
│ password        │  │ password        │
│ role_id (FK)    │  │ role_id (FK)    │
└─────────────────┘  └────────┬────────┘
                              │
                     ┌────────▼────────┐
                     │     CLIENTS     │
                     │─────────────────│
                     │ id (PK)         │
                     │ user_id (FK)    │
                     │ full_name       │
                     │ phone           │
                     │ email           │
                     │ address         │
                     │ date_of_birth   │
                     │ registration_dt │
                     └────────┬────────┘
                              │
                              │
┌─────────────────┐           │
│    TRAINERS     │           │
│─────────────────│           │
│ id (PK)         │           │
│ full_name       │           │
│ email           │           │
│ phone           │           │
│ address         │           │
│ specialization  │           │
└────────┬────────┘           │
         │                    │
         │                    │
┌────────▼────────┐           │
│    SECTIONS     │           │
│─────────────────│           │
│ id (PK)         │           │
│ name            │           │
│ sport_type      │           │
│ age_from        │           │
│ age_to          │           │
│ is_free         │           │
│ description     │           │
└────────┬────────┘           │
         │                    │
         ├────────────────────┤
         │                    │
┌────────▼────────┐  ┌────────▼────────┐
│   SCHEDULES     │  │    BOOKINGS     │
│─────────────────│  │─────────────────│
│ id (PK)         │  │ id (PK)         │
│ section_id (FK) │  │ client_id (FK)  │
│ trainer_id (FK) │  │ section_id (FK) │
│ day_of_week     │  │ booking_date    │
│ start_time      │  │ status          │
│ end_time        │  │ child_full_name │
│ location        │  │ child_age       │
└────────┬────────┘  └────────┬────────┘
         │                    │
         └────────┬───────────┘
                  │
         ┌────────▼────────┐
         │   ATTENDANCE    │
         │─────────────────│
         │ id (PK)         │
         │ booking_id (FK) │
         │ schedule_id(FK) │
         │ visit_date      │
         │ was_present     │
         └─────────────────┘
```

---

## 🔄 Связи между таблицами

### Основные связи:

1. **ROLES → EMPLOYEES** (One-to-Many)
   - Одна роль может быть у многих сотрудников

2. **ROLES → USER_CLIENTS** (One-to-Many)
   - Одна роль может быть у многих пользователей

3. **USER_CLIENTS → CLIENTS** (One-to-One)
   - У каждой учетной записи один профиль клиента

4. **CLIENTS → BOOKINGS** (One-to-Many)
   - Один клиент может иметь много бронирований

5. **SECTIONS → BOOKINGS** (One-to-Many)
   - Одна секция может иметь много бронирований

6. **SECTIONS → SCHEDULES** (One-to-Many)
   - У одной секции может быть много расписаний

7. **TRAINERS → SCHEDULES** (One-to-Many)
   - Один тренер может вести много расписаний

8. **SCHEDULES → ATTENDANCE** (One-to-Many)
   - У одного расписания может быть много отметок посещаемости

9. **BOOKINGS → ATTENDANCE** (One-to-Many)
   - У одного бронирования может быть много отметок посещаемости

---

## 📋 Описание таблиц

### ROLES (Роли)
Определяет роли в системе:
- Администратор (полный доступ)
- Менеджер (управление клиентами и бронированиями)
- Тренер (просмотр расписания и посещаемости)
- Клиент (стандартный пользователь)

### EMPLOYEES (Сотрудники)
Учетные записи сотрудников для входа в админ-панель.

### USER_CLIENTS (Пользователи-клиенты)
Учетные записи клиентов для входа в систему.

### CLIENTS (Клиенты)
Профили клиентов с личной информацией.

### TRAINERS (Тренеры)
Информация о тренерах, ведущих занятия.

### SECTIONS (Секции)
Направления занятий (фитнес, йога, бокс и т.д.).

### SCHEDULES (Расписание)
Расписание занятий с привязкой к секции и тренеру.

### BOOKINGS (Бронирования/Заявки)
Заявки клиентов на посещение секций.

### ATTENDANCE (Посещаемость)
Отметки о посещении/непосещении занятий.

---

## 🔑 Индексы для оптимизации

### Основные индексы:

```sql
-- Поиск по email/login
CREATE INDEX idx_employees_login ON employees(login);
CREATE INDEX idx_user_clients_login ON user_clients(login);
CREATE INDEX idx_clients_email ON clients(email);

-- Поиск по телефону
CREATE INDEX idx_clients_phone ON clients(phone);
CREATE INDEX idx_trainers_phone ON trainers(phone);

-- Фильтрация секций
CREATE INDEX idx_sections_sport_type ON sections(sport_type);
CREATE INDEX idx_sections_is_free ON sections(is_free);

-- Фильтрация расписания
CREATE INDEX idx_schedules_day_of_week ON schedules(day_of_week);
CREATE INDEX idx_schedule_section_day ON schedules(section_id, day_of_week);

-- Фильтрация бронирований
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_booking_client_status ON bookings(client_id, status);

-- Фильтрация посещаемости
CREATE INDEX idx_attendance_visit_date ON attendance(visit_date);
CREATE INDEX idx_attendance_was_present ON attendance(was_present);
CREATE INDEX idx_attendance_schedule_date ON attendance(schedule_id, visit_date);
```

---

## 🔐 Роли и права доступа

### Администратор (role_id=1):
- ✅ Управление сотрудниками
- ✅ Управление клиентами
- ✅ Управление тренерами
- ✅ Управление секциями
- ✅ Управление расписанием
- ✅ Управление бронированиями
- ✅ Управление посещаемостью
- ✅ Просмотр статистики

### Менеджер (role_id=2):
- ✅ Просмотр клиентов
- ✅ Управление бронированиями
- ✅ Управление посещаемостью
- ✅ Просмотр статистики
- ❌ Управление сотрудниками

### Тренер (role_id=3):
- ✅ Просмотр расписания
- ✅ Просмотр посещаемости своих занятий
- ❌ Управление бронированиями
- ❌ Управление клиентами

### Клиент (role_id=4):
- ✅ Просмотр секций
- ✅ Просмотр расписания
- ✅ Создание бронирований
- ✅ Просмотр своих бронирований
- ❌ Доступ к админ-панели

---

## 📊 Статусы бронирований

- **pending** - Ожидает одобрения
- **approved** - Одобрено
- **rejected** - Отклонено
- **cancelled** - Отменено клиентом

---

## 🎯 Примеры запросов к БД

### Получить все секции для взрослых:
```sql
SELECT * FROM sections
WHERE age_from <= 18 OR age_from IS NULL;
```

### Получить расписание на понедельник:
```sql
SELECT s.*, sec.name as section_name, t.full_name as trainer_name
FROM schedules s
JOIN sections sec ON s.section_id = sec.id
JOIN trainers t ON s.trainer_id = t.id
WHERE s.day_of_week = 'Понедельник'
ORDER BY s.start_time;
```

### Получить активные бронирования клиента:
```sql
SELECT b.*, s.name as section_name
FROM bookings b
JOIN sections s ON b.section_id = s.id
WHERE b.client_id = 1 AND b.status = 'approved';
```

### Рассчитать посещаемость секции:
```sql
SELECT 
    s.name,
    COUNT(a.id) as total_visits,
    SUM(CASE WHEN a.was_present THEN 1 ELSE 0 END) as attended,
    ROUND(
        SUM(CASE WHEN a.was_present THEN 1 ELSE 0 END) * 100.0 / COUNT(a.id),
        2
    ) as attendance_rate
FROM sections s
JOIN schedules sch ON s.id = sch.section_id
JOIN attendance a ON sch.id = a.schedule_id
WHERE s.id = 1
GROUP BY s.id, s.name;
```

---

## 🚀 Оптимизация производительности

### Рекомендации:

1. **Использовать connection pooling** в SQLAlchemy
2. **Добавить кэширование** для часто запрашиваемых данных (секции, расписание)
3. **Использовать eager loading** для связанных объектов
4. **Добавить пагинацию** для больших списков
5. **Использовать индексы** на часто фильтруемых полях

### Пример eager loading:
```python
# Плохо (N+1 запросов)
bookings = db.query(Booking).all()
for booking in bookings:
    print(booking.client.full_name)

# Хорошо (1 запрос с JOIN)
from sqlalchemy.orm import joinedload

bookings = db.query(Booking).options(
    joinedload(Booking.client),
    joinedload(Booking.section)
).all()
```

---

## 📈 Масштабирование

### При росте нагрузки:

1. **Разделить БД:**
   - Основная БД (clients, bookings, attendance)
   - БД справочников (sections, schedules, trainers)

2. **Добавить read replicas** для чтения

3. **Использовать Redis** для:
   - Кэширования секций и расписания
   - Сессий пользователей (если добавить JWT)

4. **Добавить очередь задач** (Celery) для:
   - Отправки уведомлений
   - Генерации отчетов

5. **Мониторинг:**
   - Sentry для ошибок
   - Prometheus + Grafana для метрик

---

**Эта схема поможет лучше понять архитектуру системы! 📊**
