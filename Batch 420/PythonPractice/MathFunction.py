def minimum(*a):
    return min(a)
def maximum(*a):
    return max(a)
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b,fl=2):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        # di=a/b
        # return (f"%.{fl}f"%di)
        # return round(a / b, fl)
        return float(f"{a/b:.{fl}f}")

if __name__ == '__main__':
    print('hello world')
    print(div(1,76))

fun="python"