#This is a 2D and 3D shape Area, Perimeter, Surface Area & Volume caluculator.
#It includes the following shapes: Square, Rectangle, Cirle (& its types), Triangles (& its types), Cube, Cuboid, Sphere (& its types).

wroval = "\n⚠️  Invalid value entered!  Please try again...\n"
#wroval -> Wrong Value "String"

thanks = "\n=========== Thank You For Using LiTBRo's Calculator! ===========\n"

def progres(): #program-reset function
    rel = str(input("\nWould you like to try again? (y/n) => "))
    if rel == "y":
        main.mainp()
    elif rel == "n":
        print(thanks)
        exit()
    else: #Debugged to avoid errors
        print(" ")
        progres()

def termin():
    print(thanks)
    exit()
    
class sq():
    def square(): #parenthesis ke beech me 'squ' -> you are passing squ in the class as an argument.
        print("\nEnter the measurements below to calculate the AREA & PERIMETER OF SQUARE:")
        def length():
            a = float(input("\tLength of a side of square => "))
            if a > 0: #Avoiding errors
                un = str(input("\tEnter the unit used => ",))
                ar = (a*a)
                per = (4*a)
                sqar = str(round(ar, 2))
                sqper = str(round(per, 2))
                print("\nThe area of square is =", sqar,"sq."+un)
                print("The perimeter of square is =", sqper, un)
                progres()
            else: #restart sequence
                print(wroval)
                length()
        length()

class rect():
    def rectangle():
        print("\nEnter the measurements below to calculate the AREA & PERIMETER OF RECTANGLE:")
        def length():
            l = float(input("\tLength of rectangle => "))
            if l > 0:
                def breadth(): #To only restart breadth input (Incase of an error), otherwise no disruption on the layout and intergration.)
                    b = float(input("\tBreadth of rectangle => "))
                    if b > 0:
                        un = str(input("\tEnter the unit used => "))
                        ar = (l*b)
                        per = (2*(l+b))
                        recar = str(round(ar, 2))
                        recper = str(round(per, 2))
                        print("\nThe area of rectangle is =", recar,"sq."+un,)
                        print("The perimeter of rectangle is =", recper, un,)
                        progres()
                    else: #restart sequence in case of error in breadth
                        print(wroval)
                        breadth()
                breadth()

            else: #restart sequence
                print(wroval)
                length()
        length()

class cir():
    def cir():
        print("\nEnter the measurements below to calculate the AREA & CIRCUMFERENCE OF CIRCLE:")
        def radius():
            r = float(input("\tLength of radius of circle => "))
            if r > 0: #Avoiding errors
                un = str(input("\tEnter the unit used => "))
                ar = ((22*(r**2))/7)
                circum = ((44*r)/7)
                cirar = str(round(ar, 2))
                circircum = str(round(circum, 2))
                print("\nThe area of circle is =", cirar,"sq."+un,)
                print("The circumference of circle is =", circircum, un,)
                progres()
            else: #restart sequence
                print(wroval)
                radius()
        radius()

    def hcir():
        print("\nEnter the measurements below to calculate the AREA & CIRCUMFERENCE OF SEMI-CIRCLE:")
        def radius():
            r = float(input("\tLength of radius of circle => "))
            if r > 0: #Avoiding errors
                un = str(input("\tEnter the unit used => "))
                ar = ((22*(r**2))/14)
                circum = ((22*r)/7)
                cirar = str(round(ar, 2))
                circircum = str(round(circum, 2))
                print("\nThe area of circle is =", cirar,"sq."+un,)
                print("The circumference of circle is =", circircum, un,)
                progres()
            else: #restart sequence
                print(wroval)
                radius()
        radius()

    def circle():
        print("\nSelect the type of triangle:")
        print("\tRegular Circle      =======>   a")
        print("\tSemi-Circle         =======>   b")
        sbcom = (input("==> "))
        if sbcom == "a":
            cir.cir()
        elif sbcom == "b":
            cir.hcir()
        else:
            print(wroval)
            cir.circle()

class tri:
    def rat(): #Right-Angled-Triangle
        print("\nEnter the measurements below to calculate the AREA & PERIMETER OF RIGHT-ANGELED TRIANGLE:")
        def base():
            b = float(input("\tBase of Triangle => "))
            if b > 0:
                def height(): #To only restart height input (Incase of an error), otherwise no disruption on the layout and intergration.)
                    h = float(input("\tHeight of Triangle => "))
                    if h > 0:
                        un = str(input("Enter the unit used => "))
                        ar = ((b*h)/2)
                        per = (h+b+(((h**2)+(b**2))**(1/2)))
                        ratar = str(round(ar, 2))
                        ratper = str(round(per, 2))
                        print("\nThe area of triangle is =", ratar,"sq."+un,)
                        print("The perimeter of triangle is =", ratper, un,)
                        progres()
                    else: #restart sequence in case of error in height
                        print(wroval)
                        height()
                height()
            else: #restart sequence
                print(wroval)
                base()
        base()

    def equ(): #Equilateral-Triangle
        print("\nEnter the measurements below to calculate the AREA & PERIMETER OF EQUILATERAL TRIANGLE:")
        def side():
            a = float(input("\tSide of Triangle => "))
            if a > 0: #Avoiding errors
                un = str(input("\tEnter the unit used => "))
                ar = (((3**(1/2))*(a**2))/4)
                peri = (3*a)
                eqtar = str(round(ar, 2))
                eqtperi = str(round(peri, 2))
                print("\nThe area of triangle is =", eqtar,"sq."+un,)
                print("The perimeter of triangle is =", eqtperi, un,)
                progres()
            else: #restart sequence
                print(wroval)
                side()
        side()

    def iso():
        print("\nEnter the measurements below to calculate the AREA & PERIMETER OF ISOCELES TRIANGLE:")
        def side():
            a = float(input("\tCommon side of Triangle => "))
            if a > 0:
                p = a**2
                def height(): #To only restart height input (Incase of an error), otherwise no disruption on the layout and intergration.)
                    b = float(input("\tBase of Triangle => "))
                    if b > 0:
                        q = b**2
                        un = str(input("Enter the unit used => "))
                        ar = ((b*(((4*p)-q)**(1/2)))/4)
                        per = ((2*a)+b)
                        isotar = str(round(ar, 2))
                        isotper = str(round(per, 2))
                        print("\nThe area of triangle is =", isotar,"sq."+un,)
                        print("The perimeter of triangle is =", isotper, un,)
                        progres()
                    else: #restart sequence in case of error in breadth
                        print(wroval)
                        height()
                height()
            else: #restart sequence
                print(wroval)
                side()
        side()

    def triangle():
        print("\nSelect the type of triangle:")
        print("\tRight-Angled        =======>   a")
        print("\tEquilateral         =======>   b")
        print("\tIsoceles            =======>   c")
        sbcom = (input("=> "))
        if sbcom == "a":
            tri.rat()
        elif sbcom == "b":
            tri.equ()
        elif sbcom == "c":
            tri.iso()
        else:
            print(wroval)
            tri.triangle()

class cu:
    def cube():
        print("\nEnter the measurements below to calculate the TSA, LSA & VOLUME OF CUBE:")
        def side():
            a = float(input("\tCommon side of Cube => "))
            if a > 0:
                vol = a**3
                tsa = 6*a**2
                lsa = 4*a**2
                un = str(input("Enter the unit used => "))
                print("\nThe TSA of Cube is =", tsa,"sq."+un,)
                print("The LSA of Cube is =", lsa, "sq."+un,)
                print("The Volume of Cube is =", vol, "cub."+un)
                progres()
            else: #restart sequence
                print(wroval)
                side()
        side()


class cub:
    def cuboid():
        print("\nEnter the measurements below to calculate the TSA, LSA & VOLUME OF CUBOID:")
        def length():
            l = float(input("\tLength of Cuboid => "))
            if l > 0:
                def breadth():
                    b = float(input("\tBreadth of Cuboid => "))
                    if b > 0:
                        def height():
                            h = float(input("\tHeight of Cuboid => "))
                            if h > 0:
                                vol = l*b*h
                                tsa = 2*((l*b)+(b*h)+(h*l))
                                lsa = 2*((b*h)+(h*l))
                                un = str(input("\tEnter the unit used => "))
                                print("\nThe TSA of Cuboid is =", tsa,"sq."+un,)
                                print("The LSA of Cuboid is =", lsa, "sq."+un,)
                                print("The Volume of Cuboid is =", vol, "cub."+un)
                                progres()
                            else:
                                print(wroval)
                                height()
                        height()
                    else:
                        print(wroval)
                        breadth()
                breadth()
            else: #restart sequence
                print(wroval)
                length()
        length()

class sph:
    def regsphere():
        print("\nEnter the measurements below to calculate the TSA & VOLUME OF SPHERE:")
        def radius():
            r = float(input("\tRadius of sphere => "))
            if r > 0:
                tsa = (88*(r**2))/7
                vol = (88*(r**2))/21
                ar = round(tsa, 2)
                v = round(vol, 2)

                un = str(input("\tEnter the unit used => "))
                print("\nThe TSA of Sphere is =", ar,"sq."+un,)
                print("The Volume of Sphere is =", v, "cub."+un)
                progres()
            else:
                print(wroval)
                radius()
        radius()        

    def hsphere():
        print("\nEnter the measurements below to calculate the TSA & VOLUME OF SPHERE:")
        def radius():
            r = float(input("\tRadius of sphere => "))
            if r > 0:
                csa = (44*(r**2))/7
                tsa = (66*(r**2))/7
                vol = (44*(r**2))/21
                ar = round(tsa, 2)
                v = round(vol, 2)
                car = round(csa, 2)

                un = str(input("\tEnter the unit used => "))
                print("\nThe TSA of Hemi-Sphere is =", ar,"sq."+un,)
                print("\nThe CSA of Hemi-Sphere is =", car,"sq."+un,)
                print("The Volume of Hemi-Sphere is =", v, "cub."+un)
                progres()
            else:
                print(wroval)
                radius()
        radius()        
        
    def sphere():
        print("\nSelect the type of sphere:")
        print("\tRegular Sphere      =======>   a")
        print("\tHemi-Sphere         =======>   b")
        sbcom = (input("==> "))
        if sbcom == "a":
            sph.regsphere()
        elif sbcom == "b":
            sph.hsphere()
        else:
            print(wroval)
            sph.triangle()

class main():
    def mainp():
        #mainp- Main-Program1
        print("\nAvailable 2D Shape Calculators:")
        print("\tSquare         ============>   1")
        print("\tRectangle      ============>   2")
        print("\tCircle         ============>   3")
        print("\tTriangle       ============>   4")

        print("\nAvailable 3D Shape Calculators:")
        print("\tCube           ============>   5")
        print("\tCuboid         ============>   6")
        print("\tSphere         ============>   7")
        # print("\tCone           ============>   8")
        #print("\n\tTerminate      ============>   0")

        bcom = (input("==> ")) #bcom -> 'base-command'(Menu Selection)

        if bcom == "1":
            sq.square()
        elif bcom == "2":
            rect.rectangle()
        elif bcom == "3":
            cir.circle()
        elif bcom == "4":
            tri.triangle()
        elif bcom == "5":
            cu.cube()
        elif bcom == "6":
            cub.cuboid()
        elif bcom == "7":
            sph.sphere()
        # elif bcom == "8":
        #     tri.triangle()
        elif bcom == "0":
            termin()
        else: #restart sequence
            print(wroval)
            main.mainp()

print("\n\n============= Welcome To LiTBRo's Calculator! =============\n")
main.mainp()
