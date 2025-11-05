from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import models, database
from schemas import booking as booking_schemas
from typing import List
from datetime import date

router = APIRouter(prefix="/bookings", tags=["Бронирования (клиент)"])


@router.post("/", response_model=booking_schemas.BookingResponse)
def create_booking(
    booking_data: booking_schemas.BookingCreate,
    client_id: int = Query(..., description="ID клиента"),
    db: Session = Depends(database.get_db)
):
    """Создать бронирование"""

    # Проверка: существует ли клиент
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    # Проверка: существует ли секция
    section = db.query(models.Section).filter(models.Section.id == booking_data.section_id).first()
    if not section:
        raise HTTPException(status_code=404, detail="Секция не найдена")

    # Создаем бронирование
    new_booking = models.Booking(
        client_id=client_id,
        section_id=booking_data.section_id,
        booking_date=date.today(),
        status="pending",
        child_full_name=booking_data.child_full_name,
        child_age=booking_data.child_age
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking


@router.get("/client/{client_id}", response_model=List[booking_schemas.BookingResponse])
def get_client_bookings(client_id: int, db: Session = Depends(database.get_db)):
    """Получить все бронирования клиента"""

    bookings = db.query(models.Booking).filter(models.Booking.client_id == client_id).all()

    result = []
    for booking in bookings:
        booking_dict = {
            "id": booking.id,
            "client_id": booking.client_id,
            "section_id": booking.section_id,
            "booking_date": booking.booking_date,
            "status": booking.status,
            "child_full_name": booking.child_full_name,
            "child_age": booking.child_age,
            "section_name": booking.section.name if booking.section else None,
        }
        result.append(booking_dict)

    return result


@router.delete("/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(database.get_db)):
    """Отменить бронирование"""

    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")

    # Обновляем статус или удаляем
    booking.status = "cancelled"
    db.commit()

    return {"message": "Бронирование отменено", "booking_id": booking_id}
