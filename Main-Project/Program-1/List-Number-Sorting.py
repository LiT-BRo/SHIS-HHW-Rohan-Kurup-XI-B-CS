list = []
cardinal = ['First', 'Second', 'Third']
for i in range(3):
    number = int(input(f"\nEnter the {cardinal[i]} Number => "))
    list.append(number)

list.sort(reverse=True)
print(f"\nAmong the three numbers, the greatest number is = {list[0]},\nThe smallest number is = {str(list[-1])}.")
