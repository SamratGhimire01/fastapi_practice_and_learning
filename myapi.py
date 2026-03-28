from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


students = {
    1: {"name": "Samrat", "age": 18, "year": 12, "email": "samrat@example.com"},
    2: {"name": "Anjali", "age": 17, "year": 11, "email": "anjali@example.com"},
    3: {"name": "Rohan", "age": 18, "year": 12, "email": "rohan@example.com"},
    4: {"name": "Sita", "age": 17, "year": 11, "email": "sita@example.com"},
    5: {"name": "Aryan", "age": 19, "year": 12, "email": "aryan@example.com"},
    6: {"name": "Maya", "age": 18, "year": 12, "email": "maya@example.com"},
    7: {"name": "Kabir", "age": 17, "year": 11, "email": "kabir@example.com"},
    8: {"name": "Isha", "age": 18, "year": 12, "email": "isha@example.com"},
    9: {"name": "Deepak", "age": 19, "year": 12, "email": "deepak@example.com"},
    10: {"name": "Pooja", "age": 17, "year": 11, "email": "pooja@example.com"}
}

class Student(BaseModel):
    name : str
    age: int
    year: int
    email : str
    
class Update_student(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[int] = None
    email:Optional[str] =None
 
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


@app.post("/create-student/{student_id}")
def create_student(student_id : int , student:Student):
    if student_id in students:
        return {"Error": f"Student Id already exists. Choose after id number {len(students)}."}
    students[student_id] = student
    return {'Success': f"{student.name}'s record is recorded succefully."}

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Update_student):
    if student_id not in students:
        return {"Error": "Id does not exist."}
    
    # Convert Pydantic object to a dict, removing anything that is None
    update_data = student.model_dump(exclude_unset=True)
    
    # Update the existing dictionary
    students[student_id].update(update_data)
    
    return {"Success": f"{students[student_id]['name']}'s record is updated successfully."}

@app.delete("/delete_student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error": "Id does not exist."}
    del students[student_id]
    return {"Success":f"{student_id}'s id is deleted. "}