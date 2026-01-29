import os
from pathlib import Path
# we need path , so we import path library to know the path

def readfileandfolder(): # show a list of existing files and folder are there.
# work on this folder, not on whole OS
    path = Path('') # why i leave as empty, because its directly take the current directory path
    items = list(path.rglob('*'))  #Recursive globe function provide all the items of current file or folder recusrrsively
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")  # its show me all files or folder in that folder with indexing


def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name:-")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,'w') as fs:
                data = input("What do you want to write in this files:-")
                fs.write(data)
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("File already Exist")
    except Exception as err:
        print(f"Error occurred as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read:-")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("READED SUCCESSFULLY")
        else:
            print("File is not exist")
    except Exception as err:
        print(f"Error occurred as {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to update:-")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing a name of your file:-")
            print("Press 2 for overwriting the data of your file:-")
            print("Press 3 for appending content in your file:-")
            res = int(input("Tell Your Response:-"))

            if res == 1:
                name2 = input("Tell your file name:-")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p,'w') as fs:
                    data = input("Tell What you want to write, this will overwrite the data:-")
                    fs.write(" "+ data)
                
            if res == 3:
                with open(p,'a') as fs:
                    data = input("Tell what do you want to append or add:- ")
                    fs.write(data)

    except Exception as err:
        print("Error occurred as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)

            print("FILE DELETED SUCCESSFULLY")

        else:
            print("No such file exist")
    
    except Exception as err:
        print("Error occurred as {err}")



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("Please enter your resposne:-"))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()