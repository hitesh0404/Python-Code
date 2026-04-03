# class Employee:
    #  pass





# raj = Employee()   # raj is object

# raj.id = "id_Card"
# raj.roles = "Roles"


    
# rajesh = Employee() # rajesh is object   

# rajesh.id = "id_Card"
# rajesh.roles = "Roles"










# Constructor (__init__) is dunder method(magic method)
# 
# it reaturns Object(instance) of class
#
# assign value to attribute at the time of creation of an instance(object)
# self is a current instance

# class Person:
#     def __init__(self,name,age):        #. this is constructor  it returns object
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"My name is {self.name} and I am {self.age} years old")

# raj = Person("raj Rathod",12)   # raj is object

# print(raj.__dict__)
# raj.greet()




# # class level Attribute
# # these attribute are common for all objects and  class
# # class level attribute can be modified by class only (class level method)


# class Person:
#     planet = "Earth"     # class level Attribute
#     def __init__(self,name,age):        #. this is constructor  it returns object
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"My name is {self.name} and I am {self.age} years old")
    


# raj = Person("Raj",12)
# rajesh = Person("Rajesh",12)
# raj.planet = "Mars"
# print(raj.planet,rajesh.planet,Person.planet)
# print(raj.__dict__)
# print(rajesh.__dict__)
# del raj.planet
# print(raj.planet)





# ## class level method 
# # are used to modify the class level attribute
# # they are accessible to instance and class both



class Person:
    
    planet = "Earth"     # class level Attribute
    def __init__(self,name,age):        #. this is constructor  it returns object
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old")
    
    @classmethod     # this decorator convert instance level method to class level method
    def set_planet(cls,name):
        cls.planet = name


# raj = Person("Raj",12)
# rajesh = Person("Rajesh",12)
# raj.set_planet("Mars")
# print(raj.planet,rajesh.planet,Person.planet)




## static method
# these are the simple method which doesn't interact with instance level atribute or class level atribute

class MathMethods:
    @staticmethod
    def sum(*num):
        total = 0 
        for i in num:
            total += i
        return total
    
    @staticmethod
    def mul(*num):
        total = 1
        for i in num:
            total *= i
        return total
    
# print(MathMethods.sum(1,2,3))
# obj1 = MathMethods()
# print(obj1.sum(1,2,3))
# print(obj1.mul(1,2,3))