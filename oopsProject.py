# OOPS PROJECTS:
# Project Niche - BANK MANAGEMENT SYSTEM
# 1. Create an bank account for users
# 2. Deposit Money
# 3. Withdrwa Money
# 4. Details
# 5. Update Details
# 6. Delete Account

############## START ###################
import json   # Store and Save User data 
import random
import string
from pathlib import Path # JSON file path needed

# FLOW :-
# USER DATA in json file
# Create a dummy which get data from JSON file
# WHY i use dummy? because this file exists in my main file(oopsProject.py)
# And then update all the things like create, depost, withdraw etc in that dummy 
# Then transfer that updates in JSON file again


class Bank:
    database = 'data.json'
    data = []     # Store dummy data in list

    try:  # we use exception handling for any kind of exception
        if Path(database).exists():  # If json file is exists then open it otherwise else statement will be executed
            with open(database) as fs:   # Open data in read mode
                data = json.loads(fs.read())  # Load JSON file data which is readed in above step and stored it in 'data' variable in list format 
        else:
            print("No such file exist")
    except Exception as err:
        print(f"Exception occurred as {err}")

    @classmethod   # Create a static method because I dont want anyone else use this
    def __Update(cls):
        with open(cls.database,'w') as fs:   # Open Data which I get in Bank Class 
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id)
    
    

# Now I need data for creating a account:-
    def Createaccount(self):
        info = {
            "name" : input("Tell your name:-"),
            "age"  : int(input("Tell your age:-")),
            "email" : input("Tell your email ID:-"),
            "pin" : int(input("Tell your pin:-")),
            "accounNo." : Bank.__accountgenerate() , 
            "balance" : 0

        }

# Now I check data , its valid or not
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you cannot create an account")
        else:
            print("Your account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

# Now I put all that data in JSON file which I get from user
# So I use update function on our class
            Bank.data.append(info)  # Append all the input info in data
            Bank.__Update()

    def Depositmoney(self):
        accnumber = input("Please tell your account number:-")
        pin = int(input("Please enter your PIN:-"))

        userdata = [i for i in Bank.data if i['accounNo.']== accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to deposit:-"))
            if amount > 100000 or amount < 0:
                print("Sorry, The amount is too much , you can deposit in between 0-100000")

            else:
                userdata[0]["balance"] += amount
                Bank.__Update()
                print("Amount deposited successfully")


    def Withdrawmoney(self):
        accnumber = input("Please tell your account number:-")
        pin = int(input("Please enter your PIN:-"))

        userdata = [i for i in Bank.data if i['accounNo.']== accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to withdraw:-"))
            if userdata[0]["balance"] < amount:
                print("Sorry you do not have enough money")

            else:
                userdata[0]["balance"] -= amount
                Bank.__Update()
                print("Amount withdrawn successfully")


    def Showdetails(self):
        accnumber = input("Please enter your account number:-")
        pin = int(input("Please enter your PIN:-"))
        userdata = [i for i in Bank.data if i['accounNo.']== accnumber and i['pin'] == pin]
        print("Your information are:-\n\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def Updatedetails(self):
        accnumber = input("Please enter your account number:-")
        pin = int(input("Please enter your PIN:-"))
        userdata = [i for i in Bank.data if i['accounNo.']== accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("No such user found")
        
        else:
            print("You cannot change the Age, Account Number, Balance")

            print("Fill the details for change or leave it empty")

            newdata = {
                "name" : input("Enter your new name or leave empty to skip:-"),
                "email" : input("Enter your new email or leave empty to skip:="),
                "pin" : input("Enter your new PIN or leave empty to skip:-")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata["age"] = userdata[0]["age"]
            newdata["accounNo."] = userdata[0]["accounNo."]
            newdata["balance"] = userdata[0]["balance"]

            if type(newdata['pin']) == str:
                newdata["pin"] = int(newdata["pin"])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__Update()
            print("Details Updated Successfully")


    def Delete(self):
        accnumber = input("Please enter your account number:-")
        pin = int(input("Please enter your PIN:-"))
        userdata = [i for i in Bank.data if i['accounNo.']== accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry, No such record found")
        else:
            check = input("Do you want to delete your account Y/N :-")
            if check == 'N' or check == 'n':
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account delete successfully")
                Bank.__Update()






user = Bank()

print("Press 1 for creating an account")
print("Press 2 for Deposit Money")
print("Press 3 for Withdraw Money")
print("press 4 for Details")
print("Press 5 for Update Details")
print("Press 6 for Delete Account")

check = int(input("Tell Your Response:-"))

if check == 1:
    user.Createaccount()

if check == 2:
    user.Depositmoney()

if check == 3:
    user.Withdrawmoney()

if check == 4:
    user.Showdetails()

if check == 5:
    user.Updatedetails()

if check == 6:
    user.Delete()


















