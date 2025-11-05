from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import employee as employee_schemas

router = APIRouter(prefix="/admin/auth", tags=["Авторизация сотрудников"])

@router.post("/login")
def employee_login(login_data: employee_schemas.EmployeeLogin, db: Session = Depends(database.get_db)):
    """Вход сотрудника"""
    employee = db.query(models.Employee).filter(models.Employee.login == login_data.login).first()

    if not employee or employee.password != login_data.password:
        raise HTTPException(status_code=401, detail="Неверный login или пароль")

    # Получаем роль
    role = db.query(models.Role).filter(models.Role.id == employee.role_id).first()

    return {
        "message": "Вход выполнен успешно",
        "employee": {
            "id": employee.id,
            "login": employee.login,
            "role": role.name if role else None,
            "role_id": employee.role_id
        }
    }

@router.get("/me/{employee_id}", response_model=employee_schemas.EmployeeResponse)
def get_current_employee(employee_id: int, db: Session = Depends(database.get_db)):
    """Получить данные текущего сотрудника"""
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")

    return employee
