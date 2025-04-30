# import my_math_functions as math
# from my_math_functions import add,sub
# print('the name of main.py file is:',__name__)
# print(add(1,2,3,4))
# print(sub(10,4,3,2,1))
from college import College
from student import Student

current_college = None
current_student = None
colleges =[]
def colleges_name():
    for i in range(len(colleges)):
        print(i,colleges[i])

def choose_college():
    colleges_name()
    index = int(input("Chose College with index"))
    current_college = colleges[index]

def show_students():
    for i in range(len(colleges)):
        for j in colleges[i].students:
            print(j,'is in college ' ,colleges[i])
def add_college():
    name = input("Name: ")
    location = input("Location: ")
    colleges.append( College(name,location) )
    print(colleges[-1])

def add_student():
    if not current_college:
        choose_college()
    name = input("Name: ")
    roll_number = int(input("roll_number: "))
    current_college.students.append( Student(roll_number,name))


input_value=True
while(input_value):
    print("""
          

        1.add college
        2.add student
        3.show colleges
        4.show students
        5.change College
        0.Exit
          

          """)
    input_value = int(input("enter Choice "))

    if not input_value:
         break
    if input_value ==1:#     1.add college
        add_college()
        continue
    if input_value ==2:#     2.add student
        add_student()
        continue
    if input_value==3: #    3.show colleges
        colleges_name()
        continue
    if input_value==4: #     4.show students
        show_students()
    if input_value==5: #      5.change College
        choose_college()
print("Thank You")