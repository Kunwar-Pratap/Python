# Python program that takes input from the user and performs calculations-->

a = int(input("Enter first value: "))
b = input("Enter an operator (+, -, *, /): ")
c = int(input("Enter second value: "))

def func_cal(a, c):
    if (b == '+'):
        add = a + c
        return add
    elif (b == '-'):
        sub = a - c
        return sub
    elif (b == '*'):
        mul = a * c
        return mul
    elif (b == '/'):
        dev = a / c
        return dev
    else:
        print("You have entered wrong keyword. Please try again!")
        exit()

cal_pro = func_cal(a, c)
print(f"Your answer is: {cal_pro}")