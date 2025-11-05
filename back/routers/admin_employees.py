from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import models, database
from schemas import employee as employee_schemas
from typing import List

router = APIRouter(prefix="/admin/employees", tags=["Админ: Сотрудники"])

@router.get("/", response_model=List[employee_schemas.EmployeeResponse])
def get_all_employees(db: Session = Depends(database.get_db)):
    """Получить всех сотрудников"""
    employees = db.query(models.Employee).all()

    # Добавляем имя роли
    result = []
    for emp in employees:
        emp_dict = {
            "id": emp.id,
            "login": emp.login,
            "password": emp.password,
            "role_id": emp.role_id,
            "role_name": emp.role.name if emp.role else None
        }
        result.append(emp_dict)

    return result

@router.post("/", response_model=employee_schemas.EmployeeResponse)
def create_employee(employee_data: employee_schemas.EmployeeCreate, admin_id: int = Query(..., description="ID администратора"), db: Session = Depends(database.get_db)):
    """Создать нового сотрудника (только для Администратора)"""
    # Проверка прав
    admin = db.query(models.Employee).filter(models.Employee.id == admin_id).first()
    if not admin or admin.role_id != 1:
        raise HTTPException(status_code=403, detail="Доступ запрещен")

    # Проверка login
    existing = db.query(models.Employee).filter(models.Employee.login == employee_data.login).first()
    if existing:
        raise HTTPException(status_code=400, detail="Login уже используется")

    new_employee = models.Employee(
        login=employee_data.login,
        password=employee_data.password,
        role_id=employee_data.role_id
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

@router.patch("/{emp_id}", response_model=employee_schemas.EmployeeResponse)
def update_employee(emp_id: int, employee_data: employee_schemas.EmployeeUpdate, admin_id: int = Query(..., description="ID администратора"), db: Session = Depends(database.get_db)):
    """Обновить сотрудника (только для Администратора)"""
    # Проверка прав
    admin = db.query(models.Employee).filter(models.Employee.id == admin_id).first()
    if not admin or admin.role_id != 1:
        raise HTTPException(status_code=403, detail="Доступ запрещен")

    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")

    if employee_data.login:
        employee.login = employee_data.login
    if employee_data.password:
        employee.password = employee_data.password
    if employee_data.role_id:
        employee.role_id = employee_data.role_id

    db.commit()
    db.refresh(employee)

    return employee

@router.delete("/{emp_id}")
def delete_employee(emp_id: int, admin_id: int = Query(..., description="ID администратора"), db: Session = Depends(database.get_db)):
    """Удалить сотрудника (только для Администратора)"""
    # Проверка прав
    admin = db.query(models.Employee).filter(models.Employee.id == admin_id).first()
    if not admin or admin.role_id != 1:
        raise HTTPException(status_code=403, detail="Доступ запрещен")

    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")

    db.delete(employee)
    db.commit()

    return {"message": "Сотрудник удален", "employee_id": emp_id}
