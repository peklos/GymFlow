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
