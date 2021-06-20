#This program prints the number pattern as required by the question.

for i in range(1, 6):
    a = 65 #Converting the ASCII values to charaters and using this creating the list and the desired pattern.
    print()
    for alphabet in range(i):
        print(chr(a), end="")
        a += 1
#-LiTBRo
