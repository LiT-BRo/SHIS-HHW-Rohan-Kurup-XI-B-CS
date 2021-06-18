print("\n\n======== Welcome to Ro's Fabonacci Number Simululator ========")
while True:
    x = 0
    n = 1 #These are new variables being printed each time (a+b = c, b+c=d....) in series. For these we will need three variables.
    a = 0 
    b = 1
    user_input_limit = int(input("\n Enter the nth term until which the series shall be printed\n=> "))
    print()

    for number_in_series in range(user_input_limit): #Repeat untill the range-required.
        print(a, end = " ")
        b += 1
        x = n
        n = a #Reverted back to standard value 0
        a = x + n