from fastapi import FastAPI, Depends, File, UploadFile
from app import models
from sqlalchemy.orm import Session
from app.database import engine, get_db
import csv
import io
from app.schemas import EmployeeCreate, PostEmployee, DepartmentsCreate, PostDepartments

models.base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {'message': 'api challenge'}   


@app.post("/upload-csv-depts/", response_model=list[PostDepartments])
async def upload_data_from_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    data = await file.read()
    csv_text = data.decode()
    csv_reader = csv.reader(io.StringIO(csv_text))
    
    created_items = []
    for row in csv_reader:
        dept_data = DepartmentsCreate(
            department=row[1]
        )
        db_employee = models.Departments(**dept_data.model_dump())
        db.add(db_employee)
        created_items.append(db_employee)
    
    db.commit()
    for item in created_items:
        db.refresh(item)
    
    return created_items


