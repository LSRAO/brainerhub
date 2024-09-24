from sqlalchemy.orm import Session
from app import models

# CRUD operations
def get_company_by_name(db: Session, company_name: str):
    return db.query(models.Company).filter(models.Company.name == company_name).first()

def create_company(db: Session, company_name: str):
    db_company = models.Company(name=company_name)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def bulk_insert_employees(db: Session, employees):
    db.bulk_insert_mappings(models.Employee, employees)
    db.commit()
