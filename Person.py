class Person:
    def __init__(self, name: str, age: int, salary=0.0, id=0) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.age}, {self.id}, {self.salary})"
