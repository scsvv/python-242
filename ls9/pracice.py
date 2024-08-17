from dataclasses import dataclass

@dataclass
class Person:
    name : str
    age : int 
    work: str | None = None 


p1 = Person(
    name = "Egor",
    age=23, 
    work="It" 
)

p2 = Person(
    name = "Daniil",
    age=25, 
    work="Seeman" 
)

print(p1, p2)