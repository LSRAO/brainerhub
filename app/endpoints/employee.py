import io
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import process_and_insert_data
import pandas as pd

router = APIRouter()

@router.post("/upload/")
async def upload_data(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Read the uploaded file into a DataFrame (assuming it's an Excel file)
        contents = await file.read()
        print("Hello")
        df = pd.read_excel(io.BytesIO(contents))
  # Read the Excel file directly from the content
        
        # Save the DataFrame to a temporary location if needed, or process directly
        # Call your service function to process the data
        process_and_insert_data(db, df)
        
        return {"message": "Data inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/upload/")
async def get_upload_instruction():
    return {"message": "Please use POST request to upload a file"}