# This is a simple tool which determines whether an entered number is a composite number a prime number or even none of them.

print("\n\n====== Welcome to Ro's Number Detector v0.2 ======\n")
notice = "\n\tNOTICE: To exit press E"

while True:
    def program():
        for i in range(2):
            number = input("\nEnter a number => ")

            if number.lower() == 'e':
                print("====== Thanks for using Ro's Number Detector v0.2 ======")
                exit()

            elif int(number) <= 1:
                print(f"\nThe number {number} is NITHER PRIME NOR COMPOSITE")

            elif int(number) > 1:
                for i in range(2, (int(number))): #So the Divisor(i) is ranging from 2 to the Inputed Number.
                    if int(number) % i == 0: #If number is divisibe by any of the numbers in range.
                        print(f"\nThe number {number} is a COMPOSITE NUMBER")
                        break
                else: 
                    print(f"\nThe number {number} is a PRIME NUMBER")

        print(notice)
        program()
    program()
