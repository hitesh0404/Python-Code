def divide(a,b):
    return a/b
try:
    num1 = int(input("enter first number :"))
    num2 = int(input("enter second number :"))
    try:    
        print(divide(num1,num2))
    except ZeroDivisionError as e:
        print("the second number could not be zero")
        num2 = int(input("enter second number :"))
        print(divide(num1,num2))
    except Exception as e:
        print(e)
    finally:
        print("end of the program")
except ZeroDivisionError as e:
    print("sorry we can't move further as you entered zero again")
except Exception as e:
    print(e)



class MyException(Exception):
    def __init__(self, *args, **kwargs):
        super(Exception, self).__init__(*args, **kwargs)
    

raise MyException("this is my exception")
print("bye bye")