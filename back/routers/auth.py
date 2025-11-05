from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import user as user_schemas
from datetime import date

router = APIRouter(prefix="/auth", tags=["Авторизация клиентов"])


@router.post("/register")
def register(register_data: user_schemas.UserRegister, db: Session = Depends(database.get_db)):
    """Регистрация нового клиента"""

    # Проверка: существует ли уже такой login
    existing_user = db.query(models.UserClient).filter(
        models.UserClient.login == register_data.user_data.login
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Login уже зарегистрирован")

    # Проверка: существует ли email
    existing_email = db.query(models.Client).filter(
        models.Client.email == register_data.client_data.email
    ).first()

    if existing_email:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")

    # Проверка: существует ли телефон
    existing_phone = db.query(models.Client).filter(
        models.Client.phone == register_data.client_data.phone
    ).first()

    if existing_phone:
        raise HTTPException(status_code=400, detail="Телефон уже зарегистрирован")

    # Создаем UserClient
    new_user = models.UserClient(
        login=register_data.user_data.login,
        password=register_data.user_data.password,
        role_id=4  # role_id=4 это "Клиент"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Создаем Client
    new_client = models.Client(
        user_id=new_user.id,
        full_name=register_data.client_data.full_name,
        phone=register_data.client_data.phone,
        email=register_data.client_data.email,
        address=register_data.client_data.address,
        date_of_birth=register_data.client_data.date_of_birth,
        registration_date=date.today()
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return {
        "message": "Регистрация успешна",
        "user_id": new_user.id,
        "client_id": new_client.id
    }


@router.post("/login")
def login(login_data: user_schemas.UserLogin, db: Session = Depends(database.get_db)):
    """Вход клиента"""

    # Ищем пользователя
    user = db.query(models.UserClient).filter(
        models.UserClient.login == login_data.login
    ).first()

    if not user or user.password != login_data.password:
        raise HTTPException(status_code=401, detail="Неверный email или пароль")

    # Получаем клиента
    client = db.query(models.Client).filter(models.Client.user_id == user.id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Профиль клиента не найден")

    return {
        "message": "Вход выполнен успешно",
        "user_id": user.id,
        "client_id": client.id,
        "full_name": client.full_name,
        "email": client.email
    }


@router.get("/me/{user_id}")
def get_current_user(user_id: int, db: Session = Depends(database.get_db)):
    """Получить данные текущего пользователя"""

    user = db.query(models.UserClient).filter(models.UserClient.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    client = db.query(models.Client).filter(models.Client.user_id == user.id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Профиль клиента не найден")

    return {
        "user_id": user.id,
        "client_id": client.id,
        "login": user.login,
        "full_name": client.full_name,
        "email": client.email,
        "phone": client.phone
    }
