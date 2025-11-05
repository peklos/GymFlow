from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import models, database
from schemas import role as role_schemas
from typing import List

router = APIRouter(prefix="/admin/roles", tags=["Админ: Роли"])

@router.get("/", response_model=List[role_schemas.RoleResponse])
def get_all_roles(db: Session = Depends(database.get_db)):
    """Получить все роли"""
    roles = db.query(models.Role).all()
    return roles
