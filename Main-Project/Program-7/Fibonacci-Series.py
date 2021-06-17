import time
x = 0
n = 1 #These are new variables being printed each time (a+b = c, b+c=d....) in series. For these we will need three variables.
a = 0 
b = 1
user_input_limit = int(input("\n Enter the nth term until which the series is required => "))
print()

for i in range(user_input_limit): #Repeat untill the range-required.
    print(a, end = " ")
    b += 1
    x = n
    n = a #Reverted back to standard value 0
    a = x + n