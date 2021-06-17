print("\n\n======Welcome to Ro's Number Detector v0.2======\n")

while True:
    number = int(input("\nEnter a number => "))
    if  number <= 1:
        print(number, "is neither Prime nor Composite.")

    else:
        for i in range(2, (number)): #So the Divisor(i) is ranging from 2 to the Inputed Number.
            if number % i == 0: #If number is divisibe by any of the numbers in range.
                print(number, "is a Composite Number.")
                break
        else: 
            print(number, "is Prime Number.")