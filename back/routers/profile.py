from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import user as user_schemas

router = APIRouter(prefix="/profile", tags=["Профиль клиента"])


@router.get("/{client_id}", response_model=user_schemas.ClientResponse)
def get_profile(client_id: int, db: Session = Depends(database.get_db)):
    """Получить профиль клиента"""

    client = db.query(models.Client).filter(models.Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    return client


@router.patch("/{client_id}", response_model=user_schemas.ClientResponse)
def update_profile(client_id: int, update_data: user_schemas.ClientUpdate, db: Session = Depends(database.get_db)):
    """Обновить профиль клиента"""

    client = db.query(models.Client).filter(models.Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    # Обновляем поля, которые были переданы
    if update_data.full_name:
        client.full_name = update_data.full_name
    if update_data.phone:
        # Проверяем уникальность телефона
        existing = db.query(models.Client).filter(
            models.Client.phone == update_data.phone,
            models.Client.id != client_id
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Телефон уже используется")
        client.phone = update_data.phone
    if update_data.email:
        # Проверяем уникальность email
        existing = db.query(models.Client).filter(
            models.Client.email == update_data.email,
            models.Client.id != client_id
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email уже используется")
        client.email = update_data.email
    if update_data.address:
        client.address = update_data.address
    if update_data.date_of_birth:
        client.date_of_birth = update_data.date_of_birth

    db.commit()
    db.refresh(client)

    return client
