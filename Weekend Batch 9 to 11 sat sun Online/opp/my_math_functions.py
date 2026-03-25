def add(*args:list):
    sum=0
    for i in args:
        sum+=i;
    return sum

def sub(*args:list): 
    sum=args[0]
    for i in args[1:]:
        sum-=i
    return sum
if __name__ == "__main__":
    print('this is my_math_functions.py file')
    print('the name of my_math_functions.py file is:',__name__)



