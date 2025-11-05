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
