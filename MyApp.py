from fastapi import FastAPI


app = FastAPI()

students_database = {
    1: {"Name": "shivam bhilarkar", "Age": 24, "Phone No": 5968743281},
    2: {"Name": "anas patni", "Age": 23, "Phone No": 1928374659},
}


# Get  -> get information from server.
# Put  -> update information from the server.
# Post -> create new information in server.
# Delete -> delete information from server.


# Get Method
@app.get("/")
def get_homepage():
    return {"Message": "Welcome to basic practical of FastAPI."}


@app.get("/about")
def about_page():
    return {"Message": "This is about section from website."}


@app.get("/get_students")
def get_all_students():
    return {"Students": students_database}


# Post Method - create or upate
@app.post("/update_student")
def update_user(student_id: int, age: int, student_name: str, phone_no: int):
    if student_id in students_database:
        return {"Message": "Student already exist with same student id"}
    students_database[student_id] = {
        "Name": student_name,
        "Age": age,
        "Phone No": phone_no,
    }
    return students_database


#  Put Method
@app.put("/add_student")
def add_student(student_name: str, age: int, phone_no: int):
    # check already exist in dictionary
    # Not working correctly fix this later
    for entry in students_database.items():
        if student_name in entry:
            return {"Message": "Student already exist!!"}
    students_database[len(students_database) + 1] = {
        "Name": student_name,
        "Age": age,
        "Phone No": phone_no,
    }
    return {"Message": f"Student : {student_name} successfully added in database."}


# Delete Method
@app.delete("/delete/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_database:
        return {
            "Message": f"Student not present in database with student id = {student_id}"
        }
    del students_database[student_id]
    return {"Message": f"Student : {student_id} successfully deleted from database. "}
