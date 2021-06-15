import time

list = ["a", "e", "i", "o", "u"]
symbols =  (('s', '$'),
            ('a', '&'),
            ('at', '@'),
            ('o', '0'),
            ('i', '!'),
            ('I', '|'),
            ("0", "O"),
            ("A", "@"),
            ("h", "#"))
print("\n\n============= Welcome To Ro's Password Generator! =============\n")
f_name = input("\nEnter your first-name => ")
print("\nHello,", f_name)
f_name = f_name.lower()
time.sleep(1)
s_name = input("\nEnter your surname => ")
s_name = s_name.lower()

password=f_name[0].upper()+f_name[1]+s_name[2]+s_name[0]+f_name[2]+"@"+str(len(s_name))

for x, y in symbols:
    password = password.replace(x, y)

print("\nYour secure password is ",password)

print("\n=========== Thanks for using  Ro's Password Generator! ===========\n")