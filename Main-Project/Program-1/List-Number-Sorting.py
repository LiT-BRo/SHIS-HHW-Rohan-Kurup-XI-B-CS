#This is a program which displays the Greatest and the Smallest numbers among 3 the three inputted integers.
#It is handled in a array Frame-Work/Data-Structure.

print("\n\n========== Welcome to LiTBRo's Number Sorter ==========\n")
list = []
cardinal = ['First', 'Second', 'Third']
for i in range(3):
    number = int(input(f"\nEnter the {cardinal[i]} Number => "))
    list.append(number)

list.sort(reverse=True)
print(f"\nAmong the three numbers, the greatest number is = {list[0]},\nThe smallest number is = {str(list[-1])}.")
