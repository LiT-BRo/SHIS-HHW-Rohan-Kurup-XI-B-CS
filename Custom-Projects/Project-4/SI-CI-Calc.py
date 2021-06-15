print("\n\n=+=+=+=+=|=| Welcome to LiTBRo's Interest Calculator |=|==+=+=+=+=\n")

wroval = "\n⚠️  Invalid value entered!  Please try again...\n"

def progres(): #program-reset function
    rel = str(input("\nWould you like to try again? (y/n) => "))
    if rel == "y":
        main()
    elif rel == "n":
        print("\n\n=========== Thank You For Using LiTBRo's Calculator! ===========\n\n")
        exit()
    else: #Debugged to avoid errors
        print(" ")
        progres()

def main():
    p = float((input("\nEnter the Principal => ₹")))
    r = float((input("Enter the Rate => ")))
    t = float((input("Enter the Time => ")))

    def compound():

        print("\nEnter the rate of Compound from values below:")
        print("\tCompounded Yearly        =>  1")
        print("\tCompounded Half-Yearly   =>  2")
        print("\tCompounded Quaterly      =>  3")
        print("\tCompounded Monthly       =>  4")

        n = float(input("=> "))

        def si():
            si = (p*r*t)/100
            A = p + si
            print ("\nThe Simple Interest is = ₹"+str(round(si, 2))+", the Total Amount with SI = ₹", round(A, 2))


        def ci():
            b = (p*((1+(r/(n*100)))**t))
            ci = b - p
            print ("\nThe Compound Interest is = ₹"+str(round(ci, 2))+", the Total Amount with CI = ₹", round(b, 2))
            progres()

        if n == 1:
            n = 1
            si()
            ci()
        elif n == 2:
            n = 2
            si()
            ci()
        elif n == 3:
            n = 4
            si()
            ci()
        elif n == 4:
            n = 12
            si()
            ci()
        else:
            print(wroval)
            compound()
    compound()
main()