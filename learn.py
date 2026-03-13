from fastapi import FastAPI
from pydantic import BaseModel,Field    
import json
import os

app = FastAPI()

FILE_NAME = "users.json"

class User(BaseModel):
    user_id: int
    name: str
    email: str
    address: str
    phone: str  = Field(..., pattern=r'^\d{10}$')
    occupation: str
    pincode:int

def read_users():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def write_users(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

@app.post("/add-users")
def add_user(user: User):
    users = read_users()
    users.append(user.dict())
    write_users(users)
    return {"message": "User added successfully"}

@app.get("/get-users")
def get_users():
    return read_users()

@app.get("/get-user/{user_id}")
def get_user(user_id: int):
    users = read_users()
    for user in users:
        if user["user_id"] == user_id:
            return user
    return {"error": "User not found"}
@app.put("/update-user/{user_id}")
def update_user(user_id: int, updated_user: User):
    users = read_users()

    for index, user in enumerate(users):
        if user["user_id"] == user_id:
            # Update user data
            users[index] = updated_user.dict()
            write_users(users)
            return {"message": "User updated successfully"}

    return {"error": "User not found"}


@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    users = read_users()
    updated_users = [user for user in users if user["user_id"] != user_id]

    if len(users) == len(updated_users):
        return {"error": "User not found"}

    write_users(updated_users)
    return {"message": "User deleted successfully"}