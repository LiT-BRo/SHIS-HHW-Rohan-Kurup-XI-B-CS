print("\n\n =+=+=+=+==|=| Welcome to LiTBRo's Percentage-Aggregator |=|==+=+=+=+=\n")

def progres(): #program-reset-function
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
    def p1():
        p1 = float(input("\nEnter marks scored in Weekly-Test 1 (Out of 30) => "))
        if p1 >= 0 and p1 <= 31:
            def p2():
                p2 = float(input("Enter marks scored in Weekly-Test 2 (Out of 30) => "))
                if p2 >= 0 and p2 <= 30:
                    def t1():
                        t1 = float(input("Enter marks scored in Terminal-Exam (Out of 100) => "))
                        if t1 >= 0 and t1 <= 100:
                            res = ((p1 + p2)/3)+((t1*4)/5)
                            print("\nThe Final Aggregate result =", str(round(res, 2))+"%")
                        else:
                            t1()
                    t1()
                else:
                    p2()
            p2()
        else:
            p1()
    p1()
    progres()
main()
