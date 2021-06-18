print("\n\n======Welcome to Ro's user_input Detector v0.2======\n")

while True:
    user_input = int(input("\nEnter a user_input => "))
    if user_input <= 1:
        print(f"\n{user_input} is neither Prime nor Composite.")

    else:
        for divisor in range(2, (user_input)): #So the Divisor is ranging from 2 to (Inputed Number-1).
            if user_input % divisor == 0: #If user_input is divisibe by any of the user_inputs in range.
                print(f"\n{user_input} is a Composite Number.")
                break
        else: 
            print(f"\n{user_input} is Prime Number.")