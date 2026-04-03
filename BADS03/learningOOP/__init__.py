# OOP
# Object oriented Programming 

# class Objects     

# A programming language support class object concepts
# are known as Object Oriented Programming Language(OOPL)


# python is OOPL

# 4 pillars of OOP
# (APIE)
# A = >  Abstraction
# P = >  Polymorphism
# I = >  Inheritance
# E = >  Encapsulation


# A = >  Abstraction

#  -Hide Complexity and show necessary thing
#  -the concept of hiding complex internal implementation details 
#  and exposing only essential features or functionality to the user


#  -Extract or take out necessary info about the domain
#   Understand Entity  their data(Attribute) and behaviour(Method)












# E = >  Encapsulation

# Binding Data and Method together 

# defining data and method inside class is known as encapsulation

class Car:
    def __init__(self):
        self.color = "White"
        self.make = "xyz"
    def run(self):
        pass










# Inheritance 

# mechanism where a new class (child/derived) inherits properties and methods 
# from an existing class (parent/base)

#  here the Car class act as parent and HondaCity takes all 
# Attribute and Method


class HondaCity(Car):  # here the Car class act as parent and HondaCity takes all Attribute and Method 
    pass






# Polymorphism


# the ability of an object, variable, or method to take on multiple forms, 
# allowing a single interface to represent different underlying types.


## it can be implemented in two way on method

### 1. Overloading

### 2. Overriding



### 1. Overloading 

####   same method name                eg wash 
####   within same class               eg Cloth
####   but with different parameter    eg one cloth you may wash only with soap
#                                      eg one cloth you may wash with      soap and Conditioner
#  

## Python doesn't support overloading




class Cloth:
    def __init__(self):
        pass
    def wash(self,soap):
        pass
    def wash(self,soap,conditioner):
        pass









# 2. Overriding


# same method name.         eg wash
# with same parameter       eg shoe you wash in different way compare to paren
# within child class        eg Shoe   with parent Cloth

class Cloth:
    def __init__(self):
        pass
    
    def wash(self,soap,conditioner):
        print("Washing with soap first and then apply conditioner")




class Shoe(Cloth):
    def __init__(self):
        pass
    def wash(self,soap,conditioner):
        print("don't wash directly with soap make foam water and drench  and then apply conditioner")




# Class 
# and Object


# Class : Class is blueprint of an real world entity(Object)
# an entity can be any living or non-living thing or tangible or non-tangible or conceptual


# eg.     If we are making a digital application like whatsapp
#        
#         what are the things of which we need to store the data
#         person
#         chat (messages)
#         media files
#         status
#            

# we can create class of each entity as of they has 2 thing
# data and method


# class Person:
#      name
#      contact
#      turnOnVisibility()
#      turnOffVisibility()
#      uploadStatus()





# Object :    it is instance of class
#             each object follow the structure given by class



# eg.    hitesh = Person()



