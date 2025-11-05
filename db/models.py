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
    date_of_birth = Column(Date)
    registration_date = Column(Date, nullable=False, default=date.today)

    user = relationship('UserClient', back_populates='client')
    bookings = relationship('Booking', back_populates='client')


class Trainer(Base):
    """Тренеры"""
    __tablename__ = 'trainers'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    address = Column(String(255))
    specialization = Column(String(100))

    schedules = relationship('Schedule', back_populates='trainer')


class Section(Base):
    """Секции"""
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    sport_type = Column(String(50), nullable=False, index=True)
    age_from = Column(Integer)
    age_to = Column(Integer)
    is_free = Column(Boolean, default=False, index=True)
    description = Column(Text)

    schedules = relationship('Schedule', back_populates='section')
    bookings = relationship('Booking', back_populates='section')


class Schedule(Base):
    """Расписание"""
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey('sections.id'), nullable=False, index=True)
    trainer_id = Column(Integer, ForeignKey('trainers.id'), nullable=False, index=True)
    day_of_week = Column(String(20), nullable=False, index=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    location = Column(String(100))

    section = relationship('Section', back_populates='schedules')
    trainer = relationship('Trainer', back_populates='schedules')
    attendance = relationship('Attendance', back_populates='schedule')


class Booking(Base):
    """Бронирования/Заявки"""
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False, index=True)
    section_id = Column(Integer, ForeignKey('sections.id'), nullable=False, index=True)
    booking_date = Column(Date, nullable=False, default=date.today, index=True)
    status = Column(String(30), default='pending', index=True)
    child_full_name = Column(String(100))
    child_age = Column(Integer)

    client = relationship('Client', back_populates='bookings')
    section = relationship('Section', back_populates='bookings')
    attendance = relationship('Attendance', back_populates='booking')


class Attendance(Base):
    """Посещаемость"""
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'), index=True)
    schedule_id = Column(Integer, ForeignKey('schedules.id'), nullable=False, index=True)
    visit_date = Column(Date, nullable=False, default=date.today, index=True)
    was_present = Column(Boolean, default=False, index=True)

    booking = relationship('Booking', back_populates='attendance')
    schedule = relationship('Schedule', back_populates='attendance')
