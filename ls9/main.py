from dataclasses import dataclass
from uuid import uuid4

@dataclass
class User: 
    login: str
    name: str
    surname: str 
    password: str
    email: str | None = None
    age: int | None = None 

    def send_verfication_code(self):
        if not self.email:
            print("Please, fill email field for account verification")
            return
        code = uuid4()
        print(code) 
        print(f'Verification code had been sended on {self.email}. Please check')



user1 = User(
    login='scsvv', 
    name="Sam",
    surname="Skorobohatov", 
    password="hjkgfd", 
    email="d@d.com"
)

print(user1)
user1.send_verfication_code()

user2 = User(
    login='xawav', 
    name="Sam",
    surname="Skorobohatov", 
    password="hjkgfd", 
)
user2.send_verfication_code()