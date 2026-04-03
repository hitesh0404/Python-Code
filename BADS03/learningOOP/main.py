from person import MathMethods as m
from person import Person
from employee import Employee
# print(m.mul(1,2,3,4))
# print(m.sum(1,2,3,4))
raj = Person("Raj Rathod",22)
raj.greet()

emp1 = Employee(age=22,name="Rajesh",salary=21200)
emp1.greet()    # overriden greet method inside employee child
print(emp1.planet)

# all classes are child of object class
print(emp1)
print(emp1.__str__())