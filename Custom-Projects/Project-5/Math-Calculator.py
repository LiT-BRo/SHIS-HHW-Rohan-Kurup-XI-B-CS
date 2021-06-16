# This is Basic Arithmatic Calculator, calculates sum, difference, product, quotient, square, square-root & factorial on the entered input.

def progres(): #program-reset function
    rel = str(input("\nWould you like to try again? (y/n) => "))
    if rel == "y":
        starter.mainp()
    elif rel == "n":
        print("\n============== Thank You For Using LiTBRo's Calculator! ==============\n")
        exit()
    else: #Debugged to avoid errors
        print(" ")
        progres()

class clascalc(): #Classic-Calc
    def ad():
        a = int(input("\nEnter your first number => "))
        b = int(input("Enter your second number => "))
        c= a+b
        print("\nThe sum of", a, "and", b, "=", c) 

        progres()
    def su():
        a = int(input("\nEnter your first number => "))
        b = int(input("Enter your second number => "))
        print("\nThe difference b/w", a, "and", b, "=", a - b)

        progres()
    def mu():
        a = int(input("\nEnter your first number => "))
        b = int(input("Enter your second number => "))
        print("\nThe product of", a, "and", b, "=", a * b)
        progres()
    def di():
        a = int(input("\nEnter your first number => "))
        b = int(input("Enter your second number => "))
        print("\nThe division of", a, "by", b, "=", a / b)
        progres()

class advcalc():
    def sq():
        a = int(input("\nEnter the number => "))
        print("The square of", a, "=", a**2)
        progres()

    def sqr():
        a = int(input("\nEnter the number => "))
        print("The square-root of", a, "=", a**0.5)
        progres()

    def fac():
        a = int(input("\nEnter the number => "))
        i, z = a, a
        while i != 1:
            i -= 1
            z = z*i
        factorial = z
        print("The factorial of", a, "=", factorial)
        progres()

class starter:

    print("\n\n =========== Welcome to LiTBRo's Math Calculator! ===========\n")
    
    def mainp():
        print("\nBelow are the classic calculators:")
        print("\tAdd          --> 1")
        print("\tSubtract     --> 2")
        print("\tMultiply     --> 3")
        print("\tDivide       --> 4")
        
        print("\nBelow are the advanced calculators:")
        print("\tSquare       --> a")
        print("\tSq.Root      --> b")
        print("\tFactorial    --> c")

        uinp = str(input("\nSelect from above the prefered operation => "))
        
        if uinp == "1":
            clascalc.ad()
        
        elif uinp == "2":
            clascalc.su()

        elif uinp == "3":
            clascalc.mu()    

        elif uinp == "4":
            clascalc.di()

        elif uinp == "a":
            advcalc.sq()

        elif uinp == "b":
            advcalc.sqr()
        
        elif uinp == "c":
            advcalc.fac()

        else:
            starter.mainp()
starter.mainp()
