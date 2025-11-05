from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import schedule as schedule_schemas
from typing import List, Optional

router = APIRouter(prefix="/schedule", tags=["Расписание (клиент)"])


@router.get("/", response_model=List[schedule_schemas.ScheduleResponse])
def get_schedule(
    section_id: Optional[int] = Query(None, description="Фильтр по секции"),
    trainer_id: Optional[int] = Query(None, description="Фильтр по тренеру"),
    day_of_week: Optional[str] = Query(None, description="Фильтр по дню недели"),
    db: Session = Depends(database.get_db)
):
    """Получить расписание с фильтрацией"""

    query = db.query(models.Schedule)

    # Фильтр по секции
    if section_id:
        query = query.filter(models.Schedule.section_id == section_id)

    # Фильтр по тренеру
    if trainer_id:
        query = query.filter(models.Schedule.trainer_id == trainer_id)

    # Фильтр по дню недели
    if day_of_week:
        query = query.filter(models.Schedule.day_of_week == day_of_week)

    schedules = query.all()

    # Добавляем вычисляемые поля
    result = []
    for schedule in schedules:
        schedule_dict = {
            "id": schedule.id,
            "section_id": schedule.section_id,
            "trainer_id": schedule.trainer_id,
            "day_of_week": schedule.day_of_week,
            "start_time": schedule.start_time,
            "end_time": schedule.end_time,
            "location": schedule.location,
            "section_name": schedule.section.name if schedule.section else None,
            "trainer_name": schedule.trainer.full_name if schedule.trainer else None,
            "time_start": schedule.start_time.strftime("%H:%M") if schedule.start_time else None,
            "time_end": schedule.end_time.strftime("%H:%M") if schedule.end_time else None
        }
        result.append(schedule_dict)

    return result


@router.get("/{schedule_id}", response_model=schedule_schemas.ScheduleResponse)
def get_schedule_item(schedule_id: int, db: Session = Depends(database.get_db)):
    """Получить элемент расписания"""

    schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()

    if not schedule:
        raise HTTPException(status_code=404, detail="Элемент расписания не найден")

    # Добавляем вычисляемые поля
    return {
        "id": schedule.id,
        "section_id": schedule.section_id,
        "trainer_id": schedule.trainer_id,
        "day_of_week": schedule.day_of_week,
        "start_time": schedule.start_time,
        "end_time": schedule.end_time,
        "location": schedule.location,
        "section_name": schedule.section.name if schedule.section else None,
        "trainer_name": schedule.trainer.full_name if schedule.trainer else None,
        "time_start": schedule.start_time.strftime("%H:%M") if schedule.start_time else None,
        "time_end": schedule.end_time.strftime("%H:%M") if schedule.end_time else None
    }
