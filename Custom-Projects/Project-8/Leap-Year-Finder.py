# This is a simple tool which helps quickly find and check whether a year is/was a leap year or not just by entering a particular year.

def year():
    year = int(input("\nEnter the year: "))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
year()

def progres(): 
    year()
    progres()
progres()
