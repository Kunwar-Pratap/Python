# Python Program to find LCM of Two Numbers

def find_lcm(a, b):
    if(a > b):
        maximum = a
    else:
        maximum = b

    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            lcm = maximum;
            break;
        maximum = maximum + 1
    return lcm

num1 = float(input(" Please Enter the First Value: "))
num2 = float(input(" Please Enter the Second Value: "))
lcm = find_lcm(num1, num2)
print("\n LCM of {0} and {1} = {2}".format(num1, num2, lcm))