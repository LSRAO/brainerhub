from fastapi import FastAPI
from app.endpoints import employee
from app.database import engine
from app import models

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(employee.router)
