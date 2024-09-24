from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    employees = relationship("Employee", back_populates="company")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    salary = Column(Float)
    manager_id = Column(Integer, nullable=True)  # Manager ID can be null
    department_id = Column(Integer, nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="employees")
