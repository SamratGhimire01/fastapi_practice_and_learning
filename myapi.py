from fastapi import FastAPI,Path
from typing import Optional
app = FastAPI()


students = {
    1: {"name": "Samrat", "age": 18, "class": 12, "email": "samrat@example.com"},
    2: {"name": "Anjali", "age": 17, "class": 11, "email": "anjali@example.com"},
    3: {"name": "Rohan", "age": 18, "class": 12, "email": "rohan@example.com"},
    4: {"name": "Sita", "age": 17, "class": 11, "email": "sita@example.com"},
    5: {"name": "Aryan", "age": 19, "class": 12, "email": "aryan@example.com"},
    6: {"name": "Maya", "age": 18, "class": 12, "email": "maya@example.com"},
    7: {"name": "Kabir", "age": 17, "class": 11, "email": "kabir@example.com"},
    8: {"name": "Isha", "age": 18, "class": 12, "email": "isha@example.com"},
    9: {"name": "Deepak", "age": 19, "class": 12, "email": "deepak@example.com"},
    10: {"name": "Pooja", "age": 17, "class": 11, "email": "pooja@example.com"}
}


@app.get("/")
def get_all():
    return students

@app.get("/selected/{id}")
def get_selected(id: int = Path(..., description="Enter the student ID", gt=0, lt=11)):
    return students[id]

@app.get("/get-by-name/{s_id}")
def get_student(s_id: int, name: Optional[str] = None):
    if name and s_id:
        if s_id in students and students[s_id]['name'] == name:
            return students[s_id]
        return {"Error": "id and name does not match"}
    
    if name:
        for student_id in students:
            if students[student_id]['name'] == name:
                return students[student_id]
        return {"Error": "No data found."}
    
    if s_id in students:
        return students[s_id]
        
    return {"Error": "No data found."}
