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
