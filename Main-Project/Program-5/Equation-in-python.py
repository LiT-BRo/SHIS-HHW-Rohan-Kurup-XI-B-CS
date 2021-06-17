for i in range(30): 
    outp = []
    x = int(input("\nEnter the value of (x) => "))
    n = int(input("Enter the value of (n) => "))
    c = 1
    v1 = int(1-x)
    outp.append(v1)
    if x > 0 and n > 0:
        for i in range(n):
            c = c+1
            v2 = x*c
            outp.append(v2)
            
                        #Groups:
                        # for x = 5, n = 5:
                        #     list = [-4, 10, 15, 20, 25, 30]
                        #     Required:
                        #         First_Element(c) = -4 ##To be added.
                        #         Group_1(b)       = [15, 25] ##To be subtracted.
                        #         Group_2(a)       = [10, 20, 30] ##To be added.

    a = outp.copy()
    d = (a[1::2])       #Group2
    e = sum(d)          #Sum of Group 2
    g = a               #For the output

    b = (a[::2])        #Group1
    c = (b[0]) or v1    #First element
    b.reverse()
    b.pop()             #Final group 1, without the first element. 
    f = sum(b)          #Sum of Group 1
    output = (e+c)-f

    print("\nThe Series formed is =", (", ".join(str(x) for x in g)))
    print("\nThe solution =", output)