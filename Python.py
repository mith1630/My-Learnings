# OPERATORS IN PYTHON
# 
# # Arithmetic operation
# a = 12
# b = 12
# print(a+b)
# print(a*b)

# print(a/b)
# print(a//b)

# print(a**b)
# print(a%b)

# compound Assignment operator
# a = 20
# # a = 40
# a = a+20
# a = a+40
# a = a+60

# #use this 
# a =20
# a += 20

# a += 40
# print(a)

# Comaparison operator
# always provide answer in boolean format
# 6 types: > , < , >= , <= , == , !=
# example 
# a = 12
# b = 12
# print(a==b) : TRUE
# print(a!=b)  : False

# a = 13
# b = 15
# print(a < b) : TRUE
# print(23>23) ; FALSE
# print(23>=23) ; TRUE

# ascii Value
# print(ord("A"))           : 65

# print(ord("a"))           : 97
# what if try camparison operator on ascci value
# print("a" > "A")    ; True
# print("A" > "B")      ; False

# what if 
# print("ABC" > "ACD")     ; FALSE on behalf of precedence
# you cannot compare different datatypes with each other

# Logical Operators ( AND , OR , NOT )

#  AND
# print(123 > 100 and 34 == 34)    : True
# print(123 > 100 and 34 == 34 and 450< 90)  : False
#  all condition must be true in and operator , if anyone of them does not meet , then it will be false

#  OR
# print(12==12 or 12!=12) : TRUE
# any one of the condition is true , then whole statement going to be true

#  NOT
# print( not 12==12) : False
#  if we use not logical operator , then its change true to false and false to true


#  EXAMPLES
# print(126 > 130)  # False
# print((456==456) != (235==236))  #True

####################################################################################################################################

# CONDITIONAL STATEMENTS
#  Task A < 10
#  Task B > 10

# a = 13
# if a > 10:
#     print("I will do Task A")

# else:
#     print(" I will do task B")

### I will do Task A


# a = 5
# if a > 10:
#     print("I will do Task A")

# else:
#     print(" I will do task B")

### I will do task B


### EXAMPLE 1
# money = int(input("Please provide me the money :-"))
# if money == 10:
#     print("Chocobar")

# else:
#     print("Mango Dolly")


### EXAMPLE 2
# money = int(input("Please provide me the money :-"))
# if money == 10:
#     print("Chocobar")

# elif money == 20:
#     print("CONE")

# else:
#     print("Mango Dolly")

#......................................................................................................
#Pactice questions
 # Que 1 :-
# a = 12
# b = 15
# if a > b:
#     print(a)
# else:
#     print(b)

# OR
# a = int(input("Enter First Digit"))
# b = int(input("Enter Second Digit"))
# if a > b:
#     print(a)
# else:
#     print(b)


### Que 2 :-
# a = str(input("Please enter your gender M/F:-"))
# if a == 'M':
#     print("Good Morning Sir")
# else:
#     print("Good Morning Mam")

### Que 3:-
# a = int(input("Please enter any digit"))
# if a%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")

### Que 3:-
# name = str(input("Enter your name"))
# age = int(input("Please eter your age"))
# if age >= 18:
#     print("You are a Valid voter")
# else:
#     print("You are a Invalid voter")

### Que 4 :-
# name = str(input("Enter your name"))
# age = int(input("Please eter your age"))
# if age < 18:
#     a = 18 - age
#     print(f"You are a valid voter after {a} years")
# else:
#     print("You are a Valid voter")


########################################################################################################################3
### LOOPs
# For Loop work on the range.
# While loop works on the condition


# FOR LOOP
# range() is imp for this loop, (S,S,S) , START , STOP , STEP
# EXAMPLE : range(1,20,2)  what i get : 1,3,5,7.... start from 1 , stop at 20 and step of 2

# a = range(1,20,1)
# for i in a:
#     print(i)   #output : 1,2,3,4.....19 , so why its 19 , i choose range of 20, so its cache

# OR
# for i in range(1,21,2):
#     print(i)

# OR
# for i in range(45):   # Start by default from 0 , and step by default take 1
#     print(i)

# Reverse order : 16 to 1
# for i in range(16,0,-1):
#     print(i)

# from -5 to -14
# for i in range(-5,-15,-1):
#     print(i)

# Table of 5 by using for loop
# for i in range(5,51,5):
#     print(i)

# user input and make a table by using for loop
# n = int(input("Please enter a number which table you want"))
# for i in range(n,(n*10)+1,n):
#     print(i)

# loops for strings:
# a = "Mithilesh"   # 0 1 2 3 4 5 6 7 8
# for i in range(8):
#     print(a[i])

# but what if you have a large string
# so use len function
# a = " My name is Mithilesh Bairwa"
# for i in range(len(a)):
#     print(a[i])
# .................
# a = "Mithilesh bairwa"
# for i in a:
#     print(i)
#.................

# for i in range(1,21):
#     if i == 15:
#         break
#     print(i)
#### 1,2,3,4.......14 , break on 15, not moving ahead
# #................
# for i in range(1,21):
#     if i == 15:
#         continue
#      print(i)

# 1,2,3.......14,16,17,18,19,20 , its skip 15 ,no need to iterate ,moving ahead


#..................................................................................................................
# For Loop Practice Question
# #1.  Print hello world n times
# n = int(input("Please enter how many no of times you have to print"))
# for i in range(n):
#     print("Hello Mithilesh")

# #2. Print natural no. up to n
# n = int(input("Enter your number"))
# for i in range(1,n+1):
#     print(i)

# #3. Reverse loop n to 1
# n = int(input("Enter your number"))
# for i in range(n,0,-1):
#     print(i)

# # #4. User input and print its table
# n = int(input("Enter your number which table you want"))
# for i in range(n,(n*10)+1,n):
#     print(i)
# #OR
# n = int(input("Enter your number which table you want"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# #5. Sum up to n terms
# n = int(input("Enter your n term"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)  

# #6. Factoria of any number
# n = int(input("Enter your number which factorial you want"))
# f = 1
# for i in range(1,n+1):
#     f = f*i
# print(f)

# #7. sum of even and odd no. in a range seperately
# n = int(input("Enter your number"))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2==0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"sum of even no. is {even} and sum of odd no. is {odd}")

# #8. All the factors of number
# n = int(input("Enter your number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# #9. Perfect no. or not(A number whose sum of factors is equal to itself)
# n = int(input("Enter your number"))
# sum = 0
# for i in range(1,n):
#     if n%i==0:
#         sum = sum + i

# if sum == n:
#     print(f"{n} is perfect number")
# else:
#     print(f"{n} is not a perfect number")

# #10. Number is prime or not
# n = int(input("Enter your number"))
# fcount = 0
# for i in range(1,n+1):
#     if n%i==0:
#         fcount = fcount+1
# if fcount == 2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")

# #11. Reverese a string without using in built function
# n = input("Enter your string")
# print(n[::-1])

## USE FOR LOOP
# n = input("Enter your string")
# r = ""     # empty string to store concatenation of our reverse string
# for i in range(len(n)-1,-1,-1):
#     r = r + n[i]
# print(r)

# #12. string is palidrome or not
# n = input("Enter your string")
# p = ""
# for i in range(len(n)-1,-1,-1):
#     p = p + n[i]

# if p == n:
#     print(f"Your string {n} is palindorme")
# else:
#     print(f"Your string {n} is not palindorme")

# #13. Count all letters, digits and symbols in given string

# n = input("Enter your string")
# Lcount = 0
# Dcount = 0
# Scount = 0
# for i in n:
#     if i.isdigit():
#         Dcount += 1
#     elif i.isalpha():
#         Lcount += 1
#     else:
#         Scount += 1

# print(f"Total no of digits in your string is {Dcount}")
# print(f"Total no of letters in your string is {Lcount}")
# print(f"Total no of Symbols in your string is {Scount}")

#....................................................................................................

# WHILE LOOP ( use when the number of iteration is unknown)
# example only for understanding( use for loop for this type of questions)
# a = 1
# while a<=30:
#     print(a)   # print value of a =1 infinite times because condition is always true
#     # so here we reassign the value of a, how?
#     a = a+1
#.................................................................................................
# WHILE LOOP PRACTICE QUESTIONS

# 1. Seperate each digit in given number and print it in new line
# a = 1234
# while a > 0:
#     print(a%10) # Extract last digit , mode give you remainder
#     a //= 10  # a = a//10  ( use this for terminate the condtion and only take the remaing number from the previous operation)
# OR ( USER INPUT)
# a = int(input("Enter your number which you want to seperate"))
# while a > 0:
#     print(a%10)
#     a = a//10

# 2. Accept a number and print its reverse
# a = int(input("Enter your number which you want to reverse"))
# rev = 0
# while a > 0:
#     rev = rev*10 +a%10
#     a = a//10
# print(rev)

# # 3. Check a number is palindorme or not
# a = int(input("Enter your number"))
# b= a # why? , because (a) will be detroyed in further ops
# # why its important to detroy (a), because its needed to break while loop, otherwise its perfoming infinite times
# p = 0
# while a>0:
#     p = p*10 + a%10
#     a //= 10

# if p == b :
#     print("Your number is palindrome")
# else:
#     print("Your number is not palindrome")

# 4 . Create a random number guessing game in python
# for this game we have use libraries of python
# so here we import our first library 
# import random
# num = random.randint(1,10)
# print(num) ##Every time when you run the code , system provide a random number in between 1 to 10
# Its take a number from 1 to 10, not worked line range function, so random number is 10 also.
# so come back to the question

# import random
# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("Please guess your number in between 1-10"))
#     if num == guess:
#         tries +=1
#         print(f"Right!, You won the game in {tries} attempts")
#         break

#     elif num < guess:
#         tries +=1
#         print("Go a liitle lower")

#     elif num > guess:
#         tries +=1
#         print("Go a liitle higher")

#     else:
#         tries +=1
#         print("Wrong!, You lose the game")

###################################################################################################

# FUNCTIONS IN PYTHON

# so there are so many function in python which is in built function.
# If you create any function by yourself or define any function which will be called by you and have their on functionality
# that function is called user defined function.
# how we define funtion , we use def keyword 
# Example
# def hello():  # why we use colon everywhere, because colon manage the flow of your code.
#     print("Hey, how are you")  # its my first demo function for understanding
    
# #why its not executed because you have to call properly, let's see how
# # so here i call
# hello() # just with simple parentheses brackets
# output = Hey, how are you
# so its not enough, there are two things which is so important
# Arguments and Parameters
# so now first we understand PARAMETERS
# example: I am defining a small function 

# def sum(a,b):    # a and b is the parameter of this function
#     print(f"The sum of your number is {a+b}")

# # its not working if i call this function like this sum()
# # why?, because when i try to run this block of code , they ask for arguments
# # so how argument passes, we have to give a value of a nd b
# # like this
# sum(12,13)  # so this what how we call my function with arguments
# # a is 12 and b is 13 respectively, because without arguments , there is no sense of function
# # so now if i run this code and call my function , hopefully i get 25 as a answer
# #OUTPUT = The sum of your number is 25
# # if i call sum function again with different parameters, see what i get

# sum(25,45)
# #OUTPUT - The sum of your number is 70
# so this is positinal arguments - FIRST

# now we discussed different types of parameters and arguments
# now we talked about default aguments
# Example
# def hello(name,age):
#     print(f"Your name is {name} and your age is {age}")
# # now i call this function
# hello("Mith",26)
# # output - Your name is Mith and your age is 26
# # but what if i give age first and name after that, like this:=
# hello(26,"Mith")
# # output - Your name is 26 and your age is Mith
# # see what going on, its take the value respectively 
# # so what should i do
# # see
# # i call my function
# hello(age = 26, name = "Mith") # if i call like this, so this is keyword arguments
# # OUTPUT - Your name is Mith and your age is 26
# # here age is keyword and we give value directly
# # but what is default argument

# simply i define sum function again, we need atleat two value 
# but with thw help of default arguments we give by default value in function
# see how../
# def sum(a,b=15):
#     print(f"The sum of your numbers is {a+b}")
# # now i simply call my function
# sum(12,13) # I give both value first a=12 and b=13
# # if i run : I get this:-
# # The sum of your numbers is 25

# # but if i give only one value like this
# sum(12)  # see what i get
# ## output - The sum of your numbers is 27
# # its taking b=15 bu default, so this is called default arguments
# # but if i provide the second value (Value of b), it replace the default one

# Question = Check given string is palindrome or not by using function

# def palindrome(strr):
#     rev = ""
#     for i in range(len(strr)-1,-1,-1):
#         rev= rev + strr[i]

#     if rev == strr:
#         print(f"{strr} :-Its Palindrome")
#     else:
#         print(f"{strr} :-Its not Palindrome")

# # Now i call my function
# palindrome("asdfghjkl") # Its not Palindrome
# palindrome("naman") # Its Palindrome

# now see what return do 
# simply i create a hello function
# def hello():
#     return "Hey, whassup!"
#  # but if i call my function like this
 
#  # hello() # i got error

# # but if i call like this
# print(hello()) # Hey, whassup! = OUTPUT
# so this is difference b/w print and return

##########################################################################

# DATA STRUCTURES:-----------
# if we store multiple values in a single variable , then we use data structure

# LIST: its always in square brackets ,
# syntax : 
# a = [12,13,14,15,16,12,13,14,True,26.4,print()]
# mutable : we change the Value
# duplicates : list allow duplicates
# Heterogenous: store all datatypes, function and all
# Ordered : we access any element of the list by indexing, because of ordered nature

# Indexing and slicing
# a = [12,13,14,15,16,17,18,19,20]
# print(a[1])  # same as string : INDEXING
# print(a[0:5:2]) # same as string : SLICING
# OUTPUT - 13
# [12, 14, 16]


# TRAVERSE on LIST:
# a = [12,13,14,15,16,34.5]
# # 1st way using index
# for i in range(len(a)):
#     # print(i) , this provide me the the index number
#     print(a[i])  # provide value of that index

# # 2nd way , directly on values
# for i in a:
#     print(i) # drawback, wont be able to access index, which is helpful , so 1st way is right.

# Difference b/w function and method
# print() this is function
# a.print() this is method, which is used inside a class

# How to see method of list
# print(dir(list))

# method description : use this
# help(list) , you can see what method does

# APPEND Method : add element at the end of the list

# l = [1,2,3,4,5,6]
# l.append(7) 
# print(l)
# OUTPUT = [1, 2, 3, 4, 5, 6, 7]

# # INSERT  Method
# l = [1,3,4,5,6]
# l.insert(1,2)  #you can choose index also, so here i choose index 1 and element value is 2
# print(l)
# OUTPUT = [1, 2, 3, 4, 5, 6]


# l = [1, 2, 3, 4, 5, 6]
# l[0] = 7  
# # this is what mutability , you can change the vaule
# print(l)
# OUTPUT-[7, 2, 3, 4, 5, 6]  # 1 is replace by 7

# QUESTIONS

#1. Print +ve and -ve elements of list
# l = [-45,67,12,-68,-69,34]
# print("Positive elements:-")
# for i in l:
#     if i >=0:
#         print(i)
# # WHY I am not using else, because they print negative one woth positive elements
# print("Negative elements:-")
# for i in l:
#     if i < 0:
#         print(i)

#2. Mean of list elements
# l = [1,2,3,4,5]
# sum = 0
# for i in l:
#     sum = sum + i
# print(sum/len(l))

#3. Find the greatest element in list and its index too
# l = [10,20,15,14,30,15,45]
# greatest = l[0]
# for i in range(len(l)):
#     if l[i] > greatest:
#         greatest = l[i]
#         index = i
# print(f"Greatest element in list is {greatest} at index {index}")

# #4. Second largest?
# l = [12,16,13,19,17]
# fl = l[0]
# sl = l[0]

# for i in l:
#     if i>fl:
#         sl=fl
#         fl = i
#     elif i > sl:
#         sl=i
# print(fl,sl)

# TUPLES :- its always in parentheses
# a = (1,2,3,4,5)
# Immutable
# Duplicates allowed
# Ordered
# Heterogenous

# TRAVERSEING on Tuple
# a = [1,2,3,4,5,6.6]
# for i in range(len(a)):
#     #print(i)  , show index
#     print(a[i]) # show values

#INDEX
# a = [1,2,3,4,5,6.6]
# index = a.index(6.6)
# print(index)   #OUTPUT 5

# # COUNT
# a = [1,2,3,6.6, 4, 5, 7, 6.6,4,5,6.6]
# count = a.count(6.6)
# print(count) output - 3

# SETS :- always in curly braces
# Mutable
# Duplicates : not allowed
# Unordered ; dont have index value
# Semi -Heterogenous : only store string, number , tuples, not everything

# Set Traversing :
# a ={1,8,9,2,3,4,5}
# for i in a:
#     print(i) 

# Sets Method
# a = {1,2,3,4,5}
# sets don't have indexing feature , then how is it mutbale...
# sets have a method for mutability
# a.remove(2)
# print(a)
# a.pop()
# print(a)

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# # s = a.union(b) # also use a|b, same work as union

# # s = a.intersection(b) # 4 and 5
# # s = b^a  # Syymetric diff. {1,2,3,6,7,8}
  
# print(s)

##################################################
# DICTIONARIES: Its a key value pair
# d ={1:"hello", 2:56} :- SYNTAX
# Mutable, you can change the value but not do any chnages in key
# key = 1 and vaule= "hello"
# Duplicates, keys must be unique, duplicate value allowed 
# Order, don't have indexing but key works as a index
# Heterogenous 
# you can access any vaue by their keys



## CRUD ops on dictionay
# d ={10:100,20:200,30:300,40:400}
# d[10] = 150   UPDATING
# print(d)   
# output - {10: 150, 20: 200, 30: 300, 40: 400} update value by their Key

# d ={10:100,20:200,30:300,40:400}
# d[10] = 150
# d[50] = 500    #CREATING new pair/
# del d[30]
# print(d)   
# output - {10: 150, 20: 200, 40: 400, 50: 500}


# TRAVERSING
# d ={10:100,20:200,30:300,40:400}
# for i in d:
#     print(i) # it prints only keys
#     print(d[i])  # it prints only values

# for i in d.values():
#     print(i)  # now its prints values

# a = [1,2,3,4,5]
# b = a
# b[0] = 100
# print(a)  
# output = [100, 2, 3, 4, 5]
# its change the vaues of (a) because of a deep copy,
# this is happened every time time in list and dict
# so what can i do 
# we use copy function who make a shallow copy , which is original list ot dict

# a =[1,2,3,4,5]
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)
# now see what i get\
# output = [1, 2, 3, 4, 5]
# # [100, 2, 3, 4, 5]
# that's why copy function is impp
# same things happens in dict also , so use copy func instead of b=a

# If you want to see key value pair of our dict
# use item() method
# d ={10:100,20:200,30:300,40:400}
# print(d.items())
# OUTPUT = dict_items([(10, 100), (20, 200), (30, 300), (40, 400)])

# QUESTIONS
# Python script to merge two python dict
# a = {1:100,2:200,3:300}
# b = {4:400,5:500,6:600}
# # a.update(b) worked but try different method
# for i in b:
#     a[i] = b[i]

# print(a)
# OUTPUT - {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

# Sum of all values in  dict
# a = {1:100,2:200,3:300}
# sum = 0
# for i in a:
#     sum = sum + a[i]
# print(sum)   # OUTPUT = 600

# Count the frequency of each elemnts
# a =[1,1,1,1,1,3,3,15,454,544,12,14,4512]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1
# print(d)
# OUTPUT = {1: 5, 3: 2, 15: 1, 454: 1, 544: 1, 12: 1, 14: 1, 4512: 1}

 ######################################################################################

# EXCEPTION HANDLING:-
# a = int(input("Tell your number"))
# print(10/a)
# print("DONE")
# i get this output:if i give input as a 5
# 2.0
# DONE 
# but what happened if i give input 0, let see
# its give me this:
# ZeroDivisionError: division by zero
# and done is not printed because error break the flow of program
# so this error is called exception, and handling this error is called exception handling

# there are 5 keyword which use mostly for exception handling
# try
# except
# else
# finally
# raise
#..........................................................................................................



# INPUT == 0 to check all cases
# TRY and EXCEPT :-
# if try not executed , then except works...
# a = int(input("Tell your number"))
# try:   # try always works with except or finally clause
#     print(10/a)
# except ZeroDivisionError:
#     print("Sorry you cannot divide by 0")
# print("DONE")

# OUTPUT = 
# Sorry you cannot divide by 0
# DONE 
#...........................................................................................

# TRY and EXCEPT :- Exception stored in variable
# a = int(input("Tell your number"))
# try:   # try always works with except or finally clause
#     print(10/a)
# except Exception as err:
#     print(f"Sorry, there is an error as {err}")
# print("DONE")
#  output = Sorry, there is an error as division by zero
# DONE
#...................................................................................

# TRY , EXCEPT and ELSE:- 
# ELSE works when try executed , otherwise except executed
# a = int(input("Tell your number"))
# try:   # try always works with except or finally clause
#     print(10/a)

# except Exception as err:
#     print(f"Sorry, there is an error as {err}")

# else:
#     print("Good, there is no error occurs")
# print("DONE") # this line is only for understanding,
# # Its always executed , doesn't matter error occurs or not
# OUTPUT = INPUT = 5
# 2.0    # TRY works
# Good, there is no error occurs   # ELSE works
# DONE
# if input is 0: then except bloack executed
# OUTPUT - Sorry, there is an error as division by zero
#  DONE
#.....................................................................................

# TRY, EXCEPT, ELSE and FINALLY:-
# Finally always executed, no matter what:- GUNDARAJ
# a = int(input("Tell your number"))
# try:   # try always works with except or finally clause
#     print(10/a)

# except Exception as err:
#     print(f"Sorry, there is an error as {err}")

# else:
#     print("Good, there is no error occurs")

# finally:
#     print("I will run, no matter what")
# print("DONE")

# INPUT = 5:
# output = 
# 2.0   # TRY works
# Good, there is no error occurs  # ELSE works
# I will run, no matter what  # and FINALLY Works
# DONE # After Error code works

# but if i give input = 0
# OUTPUT :-
# Sorry, there is an error as division by zero # EXCEPT works
# I will run, no matter what    # FINALLY works
# DONE # After error code works
#.......................................................................................................

# TRY, EXCEPT, ELSE, FINALLY and RAISE:-
# RAISE:- We can throw exception manually
# age = int(input("Tell your age:-"))
# if age <10 or age>18:
#     raise ValueError("Your age must be in b/w 10 to 18")
# else:
#     print("WELCOME TO THE CLUB")

# print("Club will start soon")

# what i get if i give input in b/w 10-18
# WELCOME TO THE CLUB
# Club will start soon
# but if i give input = 22, then what i get:-
# ValueError: Your age must be in b/w 10 to 18,
# and after error code does not works
# so we will use try here to run after error code
# how? , see below:-

# age = int(input("Tell your age:-"))
# try:

#     if age <10 or age>18:
#         raise ValueError("Your age must be in b/w 10 to 18")
#     else:
#         print("WELCOME TO THE CLUB")

# except Exception as err:
#     print(f"Error Occurred as {err}")

# print("Club will start soon")

# NOW if i run this code , and give input as 25:
# #OUTPUT :-
# Error Occurred as Your age must be in b/w 10 to 18
# Club will start soon

#################################################################################################################################
# FILE HANDLING :-
# CRUD Operation on any files like .csv , .txt and so on.., THis is called file handling
# WE use open() function to open any type of file in python

#open('write a path of file')
# p = open(r'D:\OneDrive\Desktop\requirements.txt')
# print(p.read()) # Simply see the content of file

# p = open('main.py') # NO need to give path because its exist in current directory
# print(p.read())

# there are four mode 
# 'r' = READ  , its a default mode but file must exist
# 'w' = WRITE ,  Create files or overwrites
# 'a' = APPEND , Adds at the end of the file
# 'x' = CREATE , Create a new files, fails if already exists.

# 'w' - EXAMPLE
# p = open("mith.txt",'w')   # use 'w' ,otherwise read ops executed by default
# now see what happen:
# new file is create in the same directory as mith.txt
# now i want to write something in mith.txt
# p.write("My name is Mithilesh Bairwa")
# p.close()  # close the file is imp otherwise its open all the time
# The above line will be added in mith.txt
# but if i write something else with 'w' feature , it overwrites the previous one
# so if i want to add something , i use 'a' feature, how?
# see
# p = open("mith.txt",'a') 
# p.write(" and I am from UJJAIN")
# p.close()
#..............................................................................................................

# OOPs in python:-
# a=12
# b= 12
# print(a+b)/  # This is Comparative approach

# def add(a,b):
#     return a+b

# print(add(4,5))
# print(add(5,9))   # This is Funcyinal Approach

# Now come to the OOPs approach:-
# Create a reusable code
# Secure
# Exceute multiple things at once
# Helpful for management

# CLASS: A blueprint of objects
# class Factory:
    # there are two things inside a class: ATTRIBUTES and METHODS
    # Attribute : Variables inside a class is called Attribute
    # Method : Functions inside a class is called Method
    # a = 12 # ATTRIBUTE
    
    # def hello(self):  # METHOD
    #     print("Hey, how are you")

    # print("Hello!")  
# OUTPUT - Hello!    # Its simple run everything inside a class
# now I just call my class 
#  Factory() # nothing happen , just HELLO! getting as output

# but if i print(a), i got error, because the vaule of (a) do't have global scope
# so if want to get that vaule of (a), i have to call kij=e this:-
# print(Factory().a)
# Factory().hello()

# OUTPUT = 
# Hello! : Whole class exceuted only once from line 982-989
# 12 : I call only Attribute via class in line 998
# Hey, how are you : I call method via class in line 999

# OBJECT : Required things to create a productive output, 
# eg - If i want to create a bag, it needs requirements like material, zip, pockets
# so Requirif bag is a class , their objects is zip, pockets and all
# If i have fruits like banana , apple, mango
# so fruits is a class and their object is banana , apple, mango
# AND imp thing is , you can access class attributes and method by their objects
# here is the example
# class demo:
#     a= 12
#     b =15   # ATTRIBUTES

#     def hey(self):
#         print("Hey, how are you")  # METHOD

# Now i create a object and put my class in it
# obj = demo()
# so now i simply call any attrubutes or method in my class like this:-
# print(obj.a)  # 12 is my output as expected
# directly call my method:-
# obj.hey() # Hey, how are you



#..........................................................................
# now see , what is self and MOST IMP. :- Constructor
# we cannot take parameter through class like this
# class factory(material, zips):    WRONG
# then how we can take parameter:
# so here we use constructor : to accept parameter from user
# A constructor is a method that runs automatically when we call class
# And this constructor function target the objects loaction
# see how?

# class Factory:
    # def __init__(self, material,zips,pockets):
        #here the first parameter is self automatically,
        # and we add our parameter manually in the above function
        # pass

# now see clearly , i call class, 
# Factory()   # so now class needs arguments , 
# # its show me something like this :-
# class Factory(
#     material: Any,
#     zips: Any,
#     pockets: Any)
#   Its automatically access my parameter which i give in __init__ method
# if i run diretly , they give me a error
# why its not showing self parameter, because self(By default) parameter targets your class location

# so now i call my class in proper way:-
# Factory("Leather",3,2)
# but why i provide this all parameter to class, i provide this things to object
# so now i create a object: reebok
# reebok = Factory("Leather",3,2)
# so reebok (object) have all access of my class

# so for better understaning, i write here again:-
# class Factory:
#     def __init__(self,material,zips,pockets):
#         # so self target the location of the object(reebok)
#         # how?, see
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets 
# we can say that self = reebok
# so if i write self.material = material
# by default it means, reebok.material = Leather, reebok.zips = 3, reebok.pockets = 2
# because self target object(reebok) location

# reebok = Factory("Leather",3,2)
# one more example:-
# campus = Factory("Nylon",3,3)
# so if self taret objects location, this time its target is campus which is our object
# so by default campus.material = Nylon and so on.......

# so now finally we run that class Factory
# print(reebok.pockets)  # OUTPUT - 2
# print(campus.zips)     # OUTPUT - 3
# print(campus.material) # OUTPUT - Nylon

#..................................................................................................................
# Types of attributes and methods:-
# attrubutes:-
# class Animal:
#     name = "Lion"  # class attributes

#     def __init__(self,age):
#         self.age = age # Instance attributes
        #instance is what , instance is object, and self target obj
        # so if i create a variable like self.age is known as Instances attributes
# only this two types of attributes are there.

# methods:-
# Instance method - the method which is used above are all of the one is instance method

# Class method - the method have their own decorator @classmethod and 
# default parameter is cls just like self, which target the class loaction

# Static method - Not target anyone but use their own decorator @staticmethod





# class Animal:
#     name = "Lion"  # class attributes

#     def __init__(self,age):
#         self.age = age # Instance attributes 

#     def show(self):      # Instance method
#         print("Hey,how are you")  
#         print("Hey,what is your age :- {self.age}")  # its works

#     @classmethod                  # Class Method
#     def hello(cls):            # cls =self, but this time , its target is class
#                                # cls targe class and self taregt obj
#         print("how are you brother")
#         # print("how are you brother:- {cls.age}")  # not worked like instance method

#     @staticmethod     # Static Method
#     def static():
#         print("How are you")

# obj = Animal(12)

# obj.hello()

# obj.static()

# So this three is the only methods which is used in oops in python
#############################################################################################################################

# so now move to the four pillar of oops:-
#1. Encapsulation
#2. Polymorphism
#3. Abstraction
#4. Inheritance

############################################################################################################################################
# INHERITANCE:-
# It allows a class(CHILD) to inherit properties and behaviours
# (attributes and methods) from another class (PARENT)
# BENEFITS: Code reusability, Organzied Structure, Easy to maintain and Extend
# SYNTAX:-
# class Factoryindore:  # PARENT Class/ Superclass
#     a ="I am an attribute inside Indore factory"
#     def hello(self):
#         print("I am an method inside Pune factory")

# class Factorypune(Factoryindore):   # CHILD Class / Subclass
#     pass

# obj = Factoryindore()

# obj2 = Factorypune() # now see
# if i call obj2
# print(obj2.hello())
# OUTPUT = 
# I am an method inside Pune factory
# None
# why this NONE is here , because i call function inside function,
# so i have to call like this:
# obj2.hello() # I am an method inside Pune factory

# so Factorypune inherit the property of Factoryindore

# Constructor in inheritance:-
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal): # human have age and they ask for it
#     # so here again we use constructor function and add parameter age
#     def __init__(self, name, age):
#         super().__init__(name) # but we dont give age parameter, because parent class won't be able to inherit child class property
#         # so what can i do?
#         # I simply use instance attribut here
#         self.age = age

# # seperate show functionality is needed in subclass for age
#     def show(self):
#         print(f"Hello your name is {self.name},{self.age}")


# so now human (child) class also have access of animal(parent) class

# animal1 = Animal("Lion")
# person1 = Human("MITH",26) # Human class adapt the constructor behaviour of animal class
# that's why its asked for parameter


# person1.show()
# animal1.show()
# OUTPUT :-
# Hello your name is MITH,26
# Hello your name is Lion
#...................................................................................................

# TYPES OF INHERITANCE:-
# 1. Single Inheritance - Inheritance which we use above is all single level inheritance.
# 2. Multiple Inheritance - Two parent class and single child class which inherit all property of parent one's.
# 3. Multilevel Inheritance - Grandparent class ->> Parent class ->> Child class, attributes and method are passed on through all the class.
# 4. Hierarchy inheritance - PSingle parent class with two child class


#...............................................................................................................
# Example of Multiple Inheritance :-
# class Animal:
#     name1 = "LION"

# class Human:
#     name2 = "MITH"

# class Robot(Animal,Human):
#     name3 = "Charlie12"

# obj = Robot() # ITS INHERIT THE PROPERTY OF BOTH PARENT CLASS
# print(obj.name1)
# print(obj.name2)
# print(obj.name3)
#..............................................
# Constructor in Multiple Inheritance:-
# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robot(Animal,Human):
#     name3 = "Charlie12"

# obj = Robot() # ITS INHERIT THE PROPERTY OF BOTH PARENT CLASS
# #now here my obj needs name ,

# # but if i change the order og inheritancelike this :-
# class Robot(Human,Animal):
#     name3 = "Charlie12"

# obj2 = Robot()
# # they ask me for name and age both,
# # Python follow MRO rule (Method resolution order) and they target first class name which is given in child class

#................................................................................................................................................
# Example of Multilevel Inheritance:- Via basic projects for better understanding

# class Factory:
#     def __init__(self, material,zips):
#         self.material = material
#         self.zips = zips


# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color


# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets

# obj = PuneFactory()
#.......................................................................................................
######################################################################################################################################


# POLYMORPHISM:- POLY = "MANY FORMS"
# A same name method but work in a different way is called polymorphism

# def show():
#     print("How are you")

# def show():
#     print("You're Great!")

# # now I call show() function
# show()
# I only get this (You're Great!) as a output# why its not executing the above show()  func
# Because Its overriding the previous one with the latest one

# But i want to run both of them:
# So there are three types of polymorphism
# Method Overloading, Method Overriding , Duck Typing:-


# METHOD OVERRIDING:-
# class Animal:
#     def show2(self):
#         print("Hey, I am Mithilesh")

# class Human(Animal):
#     def show(self):
#         print("How are you")

# obj = Human()
# obj.show() # How are you
# obj.show2()   # Hey, I am Mithilesh
# but what if I give the same name to my both instance method(show())
#  Like this:-

# class Animal:
#     def show(self):     #MARKED
#         print("Hey, I am Mithilesh")

# class Human(Animal):
#     def show(self):       #MARKED
#         print("How are you")

# obj = Human()
# obj.show() # How are you
# Now I won't be to access Animal class show function because I call the the child classin my obj,
# And they have their own show() function , which override the parent class show function, and this overriding is caled as method overriding.

# METHOD OVERLOADING:- We can use same name function with different parameter in a single class.
# This is called Method Overloading, but its not acceptable in python.

# DUCK TYPING:- May be have a same naming but give a different output

# class Animal:
#     def show(self):
#         print("My name is Jaggu")

# class Human:
#     def show(self):
#         print("I am Mithilesh")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show() # now see what happen here,

# Line 1343 gimme this output: My name is Jaggu
# And Line 1344 gimme this output:  I am Mithilesh

########################################################################################################################################

# ENCAPSULATION:- Its about security
# Example- I have a class Factory which have attributes and methods, and by creating instance(object),
# I can access all the properties of that class easily, but what if I give limited access to the instance , 
# so the modification in theat accesses is called an encapsulation.
# Putting data (variables) and code (function) - inside a class
# Hiding the internal details of class and only showing which is needed
# It keep your data safe and secure from being any changes
# We can set controller over the access or any modification
# 
# So now see, how encapsulation works on code
#  so i have a class factory: now i have to do changes in access, so i use access modifier which helps me to how we give access 
# of our attributes and methods to the objects or inherited class.
# 
# there are three types of access modifier
# PUBLIC, PROTECTED and PRIVATE 

## PUBLICS ACCESS MODIFIER WITH EXAMPLE:-
# class Factory:
#     a = "Indore"
#     def show(self):
#         print("Hey, I am from Indore")

# class Ujjain(Factory):
#     def show2(self):
#         print(super().a)

# obj = Ujjain() # so here i put my child class in this object
# obj.show2() # here i access child class first and access the attributes of parent class also thrugh this

# Above is the simple and easy example of public access modifier, anyone can access to their attributes and methods 
# So i dont want to give access or full access , this is very unsafe , they will easily acquire my all data
# So here i use access modifier to do modification in access setting

## PROTECTED ACCESS MODIFIER WITH EXAMPLE:-
# Now i use protected access moodifier: what it does- let see
# In python we simple use single underscore before creatinf or using attributes and method
# 


# class Factory:
#     _a = "Indore"   # PROTECTED
#     def _show(self):    # PROTECTED
#         print("Hey, I am from Indore")

# class Ujjain(Factory):
#     def show2(self):
#         print(super()._a)

# obj = Ujjain() 
# obj.show2() # Still i can access the attribute of my parent class through child class 
# So there is nothing like protected in python, its work as same as public, but why we use (_) ,
# because of the naming covention , for understanding if someone works on different language like java,C++ or etc

# So if it doesn't work, how we secure our data in python,
# let's see, how?

## PRIVATE ACCESS MODIFIER WITH EXAMPLE:-
# A private method and attribute cannot be accessed from outside the class
# We use two underscore (__) before the name to make it private

# class Factory:
#     __a = "Indore"   # PRIVATE ATTRIBUTE
#     def __show(self):    # PRIVATE METHOD
#         print("Hey, I am from Indore")

# class Ujjain(Factory):
#     def show2(self):
#         print(super().__a)

# obj = Ujjain() 
# obj.show2()
# OUTPUT = 'super' object has no attribute '_Ujjain__a'
# Not able to access because of their private nature

# See one more easy example:-
# class Factory:
#     __a = "Indore"   # PRIVATE ATTRIBUTE
#     def __show(self):    # PRIVATE METHOD
#         print("Hey, I am from Indore")

# I Directly create object and put my class in that 
# obj = Factory()
# now i call the (__show) method of Factory() class through my object,
# let see , I can access it or not
# obj.__show()
# OUTPUT = 'Factory' object has no attribute '__show'
# SEE , not able to access because of private access modifier
# Again I try to access my attribute, see:-
# print(obj.__a) 
# OUTPUT = AttributeError: 'Factory' object has no attribute '__a'


########################################################################################################################
# ABSTRACTION:-
# Abstraction does not exists in python, but we can acieve it through library
#  If you want to setup some rules, that is abstraction

# Example:-

# from abc import ABC, abstractmethod  #LIBRARY 

# class Abstract(ABC):    #create abstract class which is needed for abstraction and import ABC library
#     @abstractmethod   #ABSTRACT METHOD
#     def perimeter(self):
#         pass

#     @abstractmethod      #ABSTRACT METHOD
#     def area(self):
#         pass

# class Square(Abstract):  # Inherit Abstract class 
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("I have created")

#     def area(self):
#         print("I have created this also")

# class Circle(Abstract):       # Inherit Abstract class 
#     def __init__(self,radius):
#         self.radius = radius

#     def perimeter(self):
#         print("I have created")

#     def area(self):
#         print("I have created this also")

# Now i want to create one more rule in that class, find area and parameter also:-
# but how we do it, let see:-
# so in abstraction, we have abstract classes and methods:
# abstract classes contains one or more abstract method
# A method that is defined but not implemented in the abstract class
# Subclass(child) must provide the implementation
# so for this we have to import library:
# from abc import ABC, abstractmethod
# obj = Circle(7)
# getting error - TypeError: Can't instantiate abstract class Circle without an implementation for abstract methods 'area', 'perimeter'
# because now there is essential rule to create a abstract method for area and perimeter
# After defing function for area and perimeter in circle class, i didn't get error
#  But what about Square class?...,
# There is a rule which is created in abstract for area and perimeter,
# So if you inherit abstract class in square , you have to follow rule or creating method for area and perimeter
# obj2 = Square(12)

# That's it, this rule of abstract class is abtraction

# And finally completed the four pillar of OOPs
###################################################################################################################################################

#  Now see the last thing of OOPs , which Dunder Methods>>
# so what is dunder method?
# DUNDER METHODS:-
#  A special method which is start and end by double underscore{__}
# Eg- __init__  ,   __str__   , and so on....,
# what it does?
# Automatically called when any action perform on on object

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return f"Hello, given animal is {self.name}"

# obj = Animal("Lion")
# so previously i called my method like this: obj.__str__
#  so now don't need to do like this
# simply i use return instead of print() in __str__ function
# so now i simple and directly print my object
# print(obj)
# OUTPUT - Hello, given animal is Lion


# Lets see one more example:
# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello, given animal is {self.name} and he's age is {self.age}"
    
#     def __add__(self,other): 
#         sum = 0
#         for i in other:
#             sum = sum + i.age  # LINE 1554 for reference
#         return f"Sum of ages are :- {self.age + sum}" # Direct add sum , which have a sum value of obj2 and obj3


# obj = Animal("Lion",15)
# obj2 = Animal("Wolf", 14)
# obj3 = Animal("Tiger",18)
# print(obj + obj2)
# See I simple get this output by directly printing my obj and obj2
# output - Sum of ages are :- 29
# can i add one more obj?
# and add one more parameter in __add__ method , and give name other2, so that's not possible
# if you want to add obj3 , you need to so like this :-
# so we can send our obj3 in tuple form like this, no need to use sum + sign , just use comma
# print(obj + (obj2,obj3))
# but for this , it need to do some changes in __add__ method also:-
# OUTPUT = Sum of ages are :- 47

# So that's how we can add three objects

##############################################################################################################################














