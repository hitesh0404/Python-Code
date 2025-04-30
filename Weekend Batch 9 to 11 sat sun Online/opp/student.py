class Student:
    def __init__(self:object,roll_number:int,name:str)->object:
        self.roll_number= roll_number
        self.name = name
    def info(self)->str:
        return f"roll number: {self.roll_number} and name is : {self.name}"
    def __str__(self):
        return f"{self.roll_number} : {self.name}"
