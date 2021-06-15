print("\n\n========== Welcome to LiTBRo's Time Converter ==========\n")

def progres(): #progres - program reset
    inp = str(input("\nWould you like to try again (y/n) => "))
    if inp == "y":
        main()    
    elif inp == "n":
        print("\n\n========== Thank You For Using LiTBRo's Time Converter ==========\n\n")
    else:
        print("\nInvalid response was entered! Please try again...")
        progres()

def main():
    t1 = int(input("\nEnter the time in seconds => "))
    a = t1//86400
    b = (t1%86400)//3600
    c = ((t1%86400)%3600)//60
    d = ((t1%86400)%3600)%60

    print("The time entered =", str(t1)+"s", "has", a, "Days,", b, "Hrs,", c, "Mins and", d, "Secs.")
    progres()
main()
