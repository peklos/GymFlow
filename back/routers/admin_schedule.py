from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import schedule as schedule_schemas
from typing import List

router = APIRouter(prefix="/admin/schedule", tags=["Админ: Расписание"])

@router.get("/")
def get_all_schedules(db: Session = Depends(database.get_db)):
    """Получить все расписание"""
    schedules = db.query(models.Schedule).all()

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
            "time_start": str(schedule.start_time) if schedule.start_time else None,
            "time_end": str(schedule.end_time) if schedule.end_time else None,
        }
        result.append(schedule_dict)

    return result

@router.post("/")
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

    return {
        "id": new_schedule.id,
        "section_id": new_schedule.section_id,
        "trainer_id": new_schedule.trainer_id,
        "day_of_week": new_schedule.day_of_week,
        "start_time": new_schedule.start_time,
        "end_time": new_schedule.end_time,
        "location": new_schedule.location,
        "section_name": section.name,
        "trainer_name": trainer.full_name,
        "time_start": str(new_schedule.start_time) if new_schedule.start_time else None,
        "time_end": str(new_schedule.end_time) if new_schedule.end_time else None,
    }

@router.patch("/{schedule_id}")
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
    if schedule_data.location is not None:
        schedule.location = schedule_data.location

    db.commit()
    db.refresh(schedule)

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
        "time_start": str(schedule.start_time) if schedule.start_time else None,
        "time_end": str(schedule.end_time) if schedule.end_time else None,
    }

@router.delete("/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(database.get_db)):
    """Удалить элемент расписания"""
    schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()

    if not schedule:
        raise HTTPException(status_code=404, detail="Элемент расписания не найден")

    db.delete(schedule)
    db.commit()

    return {"message": "Элемент расписания удален", "schedule_id": schedule_id}
