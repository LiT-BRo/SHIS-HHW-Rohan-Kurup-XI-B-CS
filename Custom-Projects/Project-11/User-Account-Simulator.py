# This is a smart simulation of how large industries make use of the JSON data transfer system to exchange data across databases to store user's data collectively and use them effectively to link it with any external service. 
#What makes this simulation smart is the exchange of data across JSON files, minimum chances of runtime errors, demonstrates the simple logic behind creating accounts and accessing them, only in-built Python Modules have been used, which makes the program the most stable.


# Dependencies:
import json, time

###Source Code:
print("\n\n======== Welcome to Ro's User-Account Simulator ========")

yes = ["yes", 'y', '1', 'continue', 'go', 'yea', 'yesh', 'yeah']
no = ["no", 'n', '0', 'stop', 'pause', 'nah', 'neh', 'nope']

filename="login_ids.json"

##Creating an account:
def account_complete(name, surname, username, email, password, has_phone, phone): #Ending of the account making task. [Shorten down to accomodate 2 path closures (person with phone, without phone) of the account creation process.]

    def json_writing(data, filename="login_ids.json"):
        with open(filename, "w", encoding='utf-8') as updated_file:
            json.dump(data, updated_file, indent=4, ensure_ascii=False, sort_keys=True) # Exporting existing data onta the json database.

    with open(filename) as json_file:
        data = json.load(json_file)
        temp = data["accounts"]
        new_data = {"name":name, "surname":surname, "username":username, "email":email, "password":password, "has_phone":has_phone, "phone":phone}
        temp.append(new_data) #Appending a dict form of user info onto the open list
        
    json_writing(data) # Overwriting the existing databse with the added user
    print("\n======== Processing... ========")
    time.sleep(2.5) # Added to simulate internet latency
    print(f"\n\n======== Congratulations {name}! Your account was successfully made... ========") #Account was made! :)
    time.sleep(3)
    main()

def password_strength(password): #Checks the strength of password
    score = 0
    if len(password) > 5:
        score += 1
    for letter in password:
        if letter in ["!", "@", "#", "$", "%"]:
            score += 1
        if letter.isupper() == True:
            score += 1
        elif letter.isdigit() == True:
            try:
                score += 1
            except:
                pass
        else:
            pass
    if score > 5:
        return True #Password is Strong
    else:
        return False #Password is Weak

def create_account(): #Create a new account for a user.
    def name(): # Full name of the user
        name = input("\n= = = Enter you First Name => ")
        surname = input("= = = Enter you Last Name => ")
        confirm = input(f"\n= = = You entered your Full Name as {name} {surname}.\n= = = Would you like to continue?\n=> ")
        if confirm.lower() in yes:
            def user_n(): # User - username
                username = input('\n= = = Enter your username => ')
                username_input = username
                if username_exists(username_input) == False:
                    confirm = input(f"\n= = = Your current username is this = {username}.\n= = = Would you like to continue?\n=> ")
                    if confirm.lower() in yes:
                        def user_email(): # User - email address
                            email = input("\n= = = Enter your email address => ")
                            confirm = input(f"\n= = = Your entered email address is = {email}\n= = = Would you like to continue?\n=> ")
                            if confirm.lower() in yes:
                                def user_p(): # User - password
                                    password = input("\n= = = Enter your password (A strong password should contain the following characters: Uppercase, Lowercase, Symbol, Numeric)\n=> ")
                                    if password_strength(password) == True: #Checking users password strength
                                        confirm_password = input("\n= = = Re-enter your password\n=> ")
                                        if confirm_password == password: # Re-checking users password
                                            confirm = input(f"\n= = = Your current password is {password}.\n\n= = = Would you like to continue?\n=> ")
                                            if confirm.lower() in yes:
                                                def user_pho(): # If user wants to add mobile contacts
                                                    has_phone = input("\n= = = Would you like to register your Phone Number?\n=> ")
                                                    if has_phone in yes: # If the user has a phone he registers the phone
                                                        has_phone = True
                                                        def user_phone():
                                                            phone = int(input("\n= = = Enter your Phone Number => "))
                                                            if len(str(phone)) == 10:
                                                                confirm = input(f"\n= = = Your entered phone number is {phone}\n= = = Would you like to continue?\n=> ")
                                                                if confirm.lower() in yes:
                                                                    account_complete(name, surname, username, email, password, has_phone, phone)
                                                                    #End - Type 1

                                                                elif confirm.lower() in no:
                                                                    user_phone()
                                                            else:
                                                                print("\n⚠️  Enter a vaild phone number! Please try again...")
                                                                time.sleep(2.5)
                                                                user_phone()
                                                        user_phone()
                                                    elif has_phone in no: # If not the user is refered to in the database as not having a phone
                                                        has_phone = False
                                                        phone = None
                                                        account_complete(name, surname, username, email, password, has_phone, phone)
                                                        #End - Type 2
                                                user_pho()
                                            elif confirm.lower() in no:
                                                user_p()
                                        else:
                                            print("\n⚠️  Passwords do not match! Please try again...")
                                            time.sleep(2.5)
                                            user_p()
                                    else:
                                        print("\n⚠️  Password is Not Strong Enough! Please try another password...")
                                        time.sleep(2.5)
                                        user_p()
                                user_p()
                            else:
                                user_email()
                        user_email()
                    elif confirm.lower() in no:
                        user_n()
                else:
                    print("\n⚠️  Username not available! Try choosing a different one...")
                    time.sleep(2.5)
                    user_n()
            user_n()
        else:
            name()
    name()

def username_exists(username_input): #Checks if a username exists in current database.

    user_names = [] #Store house where all usernames are stored in a list.
    with open(filename, "r") as json_file: #Looping used to access database within a nested dictionary (JSON format)
        data = json.load(json_file)
        temp = data['accounts'] #Into the accounts Dict.
        for users in temp: #Into the list
            user_ids = users["username"] #Collecting necessary data
            user_names.append(user_ids) #Appending to Store House

    if username_input in user_names: #Value check
        return True #Existing username found
    else:
        return False #Username not found

##Logging into an account:
class account:
    def user_accounts_verification(username_input, userpassword_input): #Checks if the entered username and password match the user account

        accounts = [] #Store house where all user accounts will be stored in the format (Username:Password)

        with open(filename, "r") as json_file:
            data = json.load(json_file)
            temp = data['accounts']
            for users in temp:
                # print(keys, ":", users[keys]) #Separated values with name, value exposed
                user_ids = users["username"]
                user_password = users["password"] #Collecting the passwords of each Account
                temp_acc = {user_ids:user_password}
                accounts.append(temp_acc) #Appending (username:Password) to Store House.
        if {username_input:userpassword_input} in accounts: #Account details check
            return True #Account exists and the entered password matches the username
        else:
            return False #Account does not exist or entered password does not match.

    def user_dashboard(username_input): #Login screen after a successful login

        time.sleep(1)
        print(f"\n\n======== Welcome to your Dashboard {username_input}! ========")
        time.sleep(1)
        print(f"Username: {username_input}")
        print("\nNote: <This feature is currently in Alpha-Stage>")
        time.sleep(1)

        user_choice = input("\nTo log-out enter 'bye':\n=> ")
        if user_choice.lower() == "bye":
            time.sleep(1)
            print("\n======== Successfully logged out ========")
            time.sleep(2)
            main()

def user_login(): #The core-login function 
    def temp(): #For recursion to occur and suggest to create a new account instead in 3 attempts
        for i in range(3):
            username_input = input("\nEnter your username => ")
            if username_exists(username_input) == True:
                for i in range(3):
                    userpassword_input = input("\nEnter your password => ")
                    if account.user_accounts_verification(username_input, userpassword_input) == True:
                        time.sleep(1)
                        print("\n======== Processing... ========")
                        time.sleep(2.5) # Added to simulate internet latency
                        print("\n======== Login Successful! ========")
                        time.sleep(1)
                        account.user_dashboard(username_input)
                        break

                    elif account.user_accounts_verification(username_input, userpassword_input) == False:
                        print("\n⚠️  Entered password does not match with the username! Please try again...")
                        pass
                user_choice = input("Incase you forgot your password, would you like to create a new account? (Yes/No)\n=> ")
                if user_choice in yes:
                    create_account()
                else:
                    user_login()
            else:
                print("\n⚠️  Entered username does not exist! Please try again...")
                pass
        user_choice = input("\nIncase you forgot your username, would you like to create a new account? (Yes/No)\n=> ")
        if user_choice in yes:
            create_account()
        else:
            user_login()
    temp()

##In Beta-Testing, will be implemented in future :)

# def admin_login(): #would give admin rights like deleting a user, over-view on the database, adding/editing details manually, etc.
#     credentials = {"ID" : "Admin@123", "Password" : "Pa$$word@123"}
#     print(f"\nAdmin Credentials: {credentials}")
#     admin_id = input("\n\n= = = Enter id => ")
#     admin_password = input("= = = Enter password => ")

##Main Core Menu:

def leave():
    print(f"\n======== Thank You for using Ro's User Account Simulator ========")
    time.sleep(4)
    exit()

def main():
    user_choice = input("""\n= = = Enter below your desired choice:
    \n\t-Create a new account (C)
    \t-Login onto existing acount (L)
    \t-Login as an Admin (A) #Not available currently
    \t-Exit the interface (E)\n=> """)
    user_choice = user_choice.lower()
    
    if user_choice in ['c', 'l', 'a', 'e']:

        def switch(user_choice): #An attempt to recreate a switch in python (unoffcial-method)'
            dict = { 
                "c" : lambda : create_account(),
                "l" : lambda : user_login(),
                "e" : lambda : leave()
            }
            dict.get(user_choice, lambda : None)()
            del dict # Simultaneously deleted to optize ram usage
        switch(user_choice)

    else:
        print("\n⚠️  Invalid option selected! Please try again carefully...")
        time.sleep(2.5)
        main()

main()