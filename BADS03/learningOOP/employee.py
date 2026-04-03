from person import Person


class Employee(Person):      # is a relation

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def greet(self):      # overriding
        super().greet()
        print(f"and earning {self.salary} per month")

    def __str__(self):
        return f"name {self.name} age {self.age} salary {self.salary}"
