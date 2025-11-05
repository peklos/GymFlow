from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import user as user_schemas
from typing import List

router = APIRouter(prefix="/admin/clients", tags=["Админ: Клиенты"])

@router.get("/", response_model=List[user_schemas.ClientResponse])
def get_all_clients(db: Session = Depends(database.get_db)):
    """Получить всех клиентов"""
    clients = db.query(models.Client).all()
    return clients

@router.get("/{client_id}", response_model=user_schemas.ClientResponse)
def get_client(client_id: int, db: Session = Depends(database.get_db)):
    """Получить клиента по ID"""
    client = db.query(models.Client).filter(models.Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    return client

@router.patch("/{client_id}", response_model=user_schemas.ClientResponse)
def update_client(client_id: int, client_data: user_schemas.ClientUpdate, db: Session = Depends(database.get_db)):
    """Обновить данные клиента"""
    client = db.query(models.Client).filter(models.Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    if client_data.full_name:
        client.full_name = client_data.full_name
    if client_data.phone:
        client.phone = client_data.phone
    if client_data.email:
        client.email = client_data.email
    if client_data.address:
        client.address = client_data.address
    if client_data.date_of_birth:
        client.date_of_birth = client_data.date_of_birth

    db.commit()
    db.refresh(client)

    return client

@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(database.get_db)):
    """Удалить клиента"""
    client = db.query(models.Client).filter(models.Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    db.delete(client)
    db.commit()

    return {"message": "Клиент удален", "client_id": client_id}
