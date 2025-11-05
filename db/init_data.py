from datetime import date, time
from sqlalchemy.orm import Session
from . import models


def initialize_database(db: Session):
    """Инициализация базы данных тестовыми данными"""

    # Проверяем, есть ли уже данные
    if db.query(models.Role).count() > 0:
        print("База данных уже инициализирована")
        return

    print("Инициализация базы данных...")

    # === 1. РОЛИ ===
    roles = [
        models.Role(id=1, name="Администратор"),
        models.Role(id=2, name="Менеджер"),
        models.Role(id=3, name="Тренер"),
        models.Role(id=4, name="Клиент")
    ]
    db.add_all(roles)
    db.commit()

    # === 2. СОТРУДНИКИ ===
    employees = [
        models.Employee(login="admin@gym.ru", password="admin123", role_id=1),
        models.Employee(login="manager@gym.ru", password="manager123", role_id=2),
        models.Employee(login="trainer1@gym.ru", password="trainer123", role_id=3)
    ]
    db.add_all(employees)
    db.commit()

    # === 3. КЛИЕНТЫ (USER_CLIENTS + CLIENTS) ===
    user_clients = [
        models.UserClient(login="ivanov@mail.ru", password="user123", role_id=4),
        models.UserClient(login="petrova@gmail.com", password="user123", role_id=4),
        models.UserClient(login="sidorov@yandex.ru", password="user123", role_id=4),
        models.UserClient(login="kozlova@mail.ru", password="user123", role_id=4),
        models.UserClient(login="novikov@gmail.com", password="user123", role_id=4)
    ]
    db.add_all(user_clients)
    db.commit()

    clients = [
        models.Client(
            user_id=1,
            full_name="Иванов Иван Иванович",
            phone="+79161234501",
            email="ivanov@mail.ru",
            address="Москва, ул. Ленина, 10",
            date_of_birth=date(1990, 5, 15),
            registration_date=date(2024, 1, 10)
        ),
        models.Client(
            user_id=2,
            full_name="Петрова Анна Сергеевна",
            phone="+79161234502",
            email="petrova@gmail.com",
            address="Москва, ул. Пушкина, 20",
            date_of_birth=date(1992, 8, 20),
            registration_date=date(2024, 1, 15)
        ),
        models.Client(
            user_id=3,
            full_name="Сидоров Петр Алексеевич",
            phone="+79161234503",
            email="sidorov@yandex.ru",
            address="Москва, ул. Чехова, 5",
            date_of_birth=date(1988, 3, 10),
            registration_date=date(2024, 2, 1)
        ),
        models.Client(
            user_id=4,
            full_name="Козлова Мария Дмитриевна",
            phone="+79161234504",
            email="kozlova@mail.ru",
            address="Москва, ул. Гоголя, 15",
            date_of_birth=date(1985, 12, 5),
            registration_date=date(2024, 2, 10)
        ),
        models.Client(
            user_id=5,
            full_name="Новиков Дмитрий Викторович",
            phone="+79161234505",
            email="novikov@gmail.com",
            address="Москва, ул. Тургенева, 25",
            date_of_birth=date(1995, 7, 18),
            registration_date=date(2024, 2, 20)
        )
    ]
    db.add_all(clients)
    db.commit()

    # === 4. ТРЕНЕРЫ ===
    trainers = [
        models.Trainer(
            full_name="Смирнов Алексей Петрович",
            email="smirnov@gym.ru",
            phone="+79165551001",
            address="Москва, ул. Спортивная, 1",
            specialization="Фитнес"
        ),
        models.Trainer(
            full_name="Васильева Елена Игоревна",
            email="vasilieva@gym.ru",
            phone="+79165551002",
            address="Москва, ул. Зеленая, 10",
            specialization="Йога"
        ),
        models.Trainer(
            full_name="Кузнецов Сергей Николаевич",
            email="kuznetsov@gym.ru",
            phone="+79165551003",
            address="Москва, ул. Боевая, 5",
            specialization="Бокс"
        ),
        models.Trainer(
            full_name="Михайлова Ольга Андреевна",
            email="mikhailova@gym.ru",
            phone="+79165551004",
            address="Москва, ул. Водная, 3",
            specialization="Плавание"
        ),
        models.Trainer(
            full_name="Федоров Игорь Викторович",
            email="fedorov@gym.ru",
            phone="+79165551005",
            address="Москва, ул. Восточная, 8",
            specialization="Карате"
        )
    ]
    db.add_all(trainers)
    db.commit()

    # === 5. СЕКЦИИ ===
    sections = [
        models.Section(
            name="Общий фитнес",
            sport_type="Фитнес",
            age_from=18,
            age_to=65,
            is_free=False,
            description="Общие занятия фитнесом для поддержания формы"
        ),
        models.Section(
            name="Йога для начинающих",
            sport_type="Йога",
            age_from=16,
            age_to=70,
            is_free=False,
            description="Занятия йогой для новичков"
        ),
        models.Section(
            name="Бокс для взрослых",
            sport_type="Бокс",
            age_from=18,
            age_to=45,
            is_free=False,
            description="Тренировки по боксу для взрослых"
        ),
        models.Section(
            name="Детское плавание",
            sport_type="Плавание",
            age_from=6,
            age_to=14,
            is_free=False,
            description="Обучение плаванию для детей"
        ),
        models.Section(
            name="Карате для детей",
            sport_type="Карате",
            age_from=7,
            age_to=16,
            is_free=False,
            description="Занятия карате для детей и подростков"
        ),
        models.Section(
            name="Утренняя зарядка",
            sport_type="Фитнес",
            age_from=18,
            age_to=80,
            is_free=True,
            description="Бесплатная утренняя зарядка для всех"
        ),
        models.Section(
            name="Кроссфит",
            sport_type="Фитнес",
            age_from=20,
            age_to=50,
            is_free=False,
            description="Интенсивные функциональные тренировки"
        ),
        models.Section(
            name="Пилатес",
            sport_type="Фитнес",
            age_from=18,
            age_to=70,
            is_free=False,
            description="Занятия пилатесом для всех уровней подготовки"
        )
    ]
    db.add_all(sections)
    db.commit()

    # === 6. РАСПИСАНИЕ ===
    schedules = [
        # Общий фитнес (секция 1, тренер Смирнов)
        models.Schedule(section_id=1, trainer_id=1, day_of_week="Понедельник", start_time=time(10, 0), end_time=time(11, 30), location="Зал №1"),
        models.Schedule(section_id=1, trainer_id=1, day_of_week="Среда", start_time=time(10, 0), end_time=time(11, 30), location="Зал №1"),
        models.Schedule(section_id=1, trainer_id=1, day_of_week="Пятница", start_time=time(10, 0), end_time=time(11, 30), location="Зал №1"),

        # Йога (секция 2, тренер Васильева)
        models.Schedule(section_id=2, trainer_id=2, day_of_week="Вторник", start_time=time(18, 0), end_time=time(19, 30), location="Зал №2"),
        models.Schedule(section_id=2, trainer_id=2, day_of_week="Четверг", start_time=time(18, 0), end_time=time(19, 30), location="Зал №2"),

        # Бокс (секция 3, тренер Кузнецов)
        models.Schedule(section_id=3, trainer_id=3, day_of_week="Понедельник", start_time=time(19, 0), end_time=time(20, 30), location="Зал №3"),
        models.Schedule(section_id=3, trainer_id=3, day_of_week="Среда", start_time=time(19, 0), end_time=time(20, 30), location="Зал №3"),
        models.Schedule(section_id=3, trainer_id=3, day_of_week="Пятница", start_time=time(19, 0), end_time=time(20, 30), location="Зал №3"),

        # Детское плавание (секция 4, тренер Михайлова)
        models.Schedule(section_id=4, trainer_id=4, day_of_week="Суббота", start_time=time(10, 0), end_time=time(11, 0), location="Бассейн"),
        models.Schedule(section_id=4, trainer_id=4, day_of_week="Воскресенье", start_time=time(10, 0), end_time=time(11, 0), location="Бассейн"),

        # Карате (секция 5, тренер Федоров)
        models.Schedule(section_id=5, trainer_id=5, day_of_week="Вторник", start_time=time(16, 0), end_time=time(17, 30), location="Зал №4"),
        models.Schedule(section_id=5, trainer_id=5, day_of_week="Четверг", start_time=time(16, 0), end_time=time(17, 30), location="Зал №4"),

        # Утренняя зарядка (секция 6, тренер Смирнов)
        models.Schedule(section_id=6, trainer_id=1, day_of_week="Понедельник", start_time=time(8, 0), end_time=time(8, 45), location="Площадка"),
        models.Schedule(section_id=6, trainer_id=1, day_of_week="Среда", start_time=time(8, 0), end_time=time(8, 45), location="Площадка"),
        models.Schedule(section_id=6, trainer_id=1, day_of_week="Пятница", start_time=time(8, 0), end_time=time(8, 45), location="Площадка"),

        # Кроссфит (секция 7, тренер Смирнов)
        models.Schedule(section_id=7, trainer_id=1, day_of_week="Вторник", start_time=time(20, 0), end_time=time(21, 30), location="Зал №1"),
        models.Schedule(section_id=7, trainer_id=1, day_of_week="Четверг", start_time=time(20, 0), end_time=time(21, 30), location="Зал №1"),

        # Пилатес (секция 8, тренер Васильева)
        models.Schedule(section_id=8, trainer_id=2, day_of_week="Понедельник", start_time=time(17, 0), end_time=time(18, 30), location="Зал №2"),
        models.Schedule(section_id=8, trainer_id=2, day_of_week="Среда", start_time=time(17, 0), end_time=time(18, 30), location="Зал №2"),
    ]
    db.add_all(schedules)
    db.commit()

    # === 7. БРОНИРОВАНИЯ ===
    bookings = [
        models.Booking(client_id=1, section_id=1, booking_date=date(2024, 3, 1), status="approved"),
        models.Booking(client_id=1, section_id=6, booking_date=date(2024, 3, 2), status="approved"),
        models.Booking(client_id=2, section_id=2, booking_date=date(2024, 3, 3), status="approved"),
        models.Booking(client_id=2, section_id=8, booking_date=date(2024, 3, 4), status="approved"),
        models.Booking(client_id=3, section_id=3, booking_date=date(2024, 3, 5), status="approved"),
        models.Booking(client_id=3, section_id=7, booking_date=date(2024, 3, 6), status="approved"),
        models.Booking(client_id=4, section_id=4, booking_date=date(2024, 3, 7), status="pending", child_full_name="Козлов Иван", child_age=10),
        models.Booking(client_id=5, section_id=5, booking_date=date(2024, 3, 8), status="pending", child_full_name="Новикова Мария", child_age=9),
    ]
    db.add_all(bookings)
    db.commit()

    # === 8. ПОСЕЩАЕМОСТЬ ===
    attendance = [
        models.Attendance(booking_id=1, schedule_id=1, visit_date=date(2024, 3, 4), was_present=True),
        models.Attendance(booking_id=1, schedule_id=2, visit_date=date(2024, 3, 6), was_present=True),
        models.Attendance(booking_id=2, schedule_id=13, visit_date=date(2024, 3, 4), was_present=True),
        models.Attendance(booking_id=3, schedule_id=4, visit_date=date(2024, 3, 5), was_present=True),
        models.Attendance(booking_id=4, schedule_id=18, visit_date=date(2024, 3, 6), was_present=False),
        models.Attendance(booking_id=5, schedule_id=6, visit_date=date(2024, 3, 4), was_present=True),
        models.Attendance(booking_id=6, schedule_id=16, visit_date=date(2024, 3, 5), was_present=True),
    ]
    db.add_all(attendance)
    db.commit()

    print("База данных успешно инициализирована!")
    print(f"- Ролей: {len(roles)}")
    print(f"- Сотрудников: {len(employees)}")
    print(f"- Клиентов: {len(clients)}")
    print(f"- Тренеров: {len(trainers)}")
    print(f"- Секций: {len(sections)}")
    print(f"- Расписаний: {len(schedules)}")
    print(f"- Бронирований: {len(bookings)}")
    print(f"- Посещаемости: {len(attendance)}")
