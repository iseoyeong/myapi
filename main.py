# https://github.com/hogeline/sample_fastapi

from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware

from database import session
from model import UserTable, User

app = FastAPI() #애플리케이션 생성

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------API 정의------------
@app.get("/users")
def read_users():
    users = session.query(UserTable).all()
    return users

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user

@app.post("/user")
# /user?name="이름"&password=...
async def create_user(name: str, password : str):

    user = UserTable()
    user.name = name
    user.password = password

    session.add(user)
    session.commit()

    return f"{name} created..."

@app.put("/users")
# users=[{"id": 1, "name": "이름1", "password": ..}]
async def update_users(users: List[User]):

    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.name = i.name
        user.password = i.password
        session.commit()

    return f"{users[0].name} updated..."


@app.delete("/user")
async def delete_users(userid: int):

    user = session.query(UserTable).filter(UserTable.id == userid).delete()
    session.commit()

    return f"User deleted..."