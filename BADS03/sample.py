def my_print(val,about = "Value"):
    if about != "Value":
        print(f"{about.__name__} of {val} : {about(val) }")
    else:
        print(f"{about} of {val} : {val}")

num1 = input("\nEnter first num :\n")
num2 = input("\nEnter second num:\n")

print("\n",num1+num2+"\n\n")
# "13" + "15"

my_print(num1,type)
my_print(num2,type)
my_print(num1,id)
my_print(num2,id)
my_print(num2)