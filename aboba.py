from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str

maxim = User(user_id=10, name="aboba", age=15, email="afs@mail.ru")
