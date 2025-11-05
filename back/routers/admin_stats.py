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
        "total_clients": total_clients,
        "total_trainers": total_trainers,
        "total_sections": total_sections,
        "total_bookings": total_bookings,
        "pending_bookings": pending_bookings,
        "approved_bookings": approved_bookings,
        "total_visits": total_visits,
        "present_visits": present_visits,
        "attendance_rate": attendance_rate,
        "popular_sections": popular_sections_list,
        "active_clients": active_clients_list
    }
