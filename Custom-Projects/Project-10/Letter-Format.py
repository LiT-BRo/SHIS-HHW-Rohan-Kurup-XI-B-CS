letter = """\n\nDate: <|DATE|>

Subject: <|SUBJECT|>

Dear <|NAME|>,
Greetings from Ro's Coding Experiment House! I am very pleased to inform that you have been selected.

Thanks and regards,
<|USER|>\n\n""" #Multi-line strings are easier to format.

name = input("\nEnter the addressing name of recipient => ")
subject = input("\nEnter the subject => ")
date = input("\nEnter the date of writing => ")
user = input("\nEnter your name => ")
user_designation = input("Enter your designation => ")

letter = letter.replace("<|NAME|>", name) #We are updating the value of letter with each variable at a time.
letter = letter.replace("<|DATE|>", date)
letter = letter.replace("<|USER|>", user)
letter = letter.replace("<|SUBJECT|>", subject)
# letter = letter.replace("<|DESIGNATION|>", user_designation)
print(letter)