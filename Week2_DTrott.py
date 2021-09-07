"""
DSC 530
Week 2
Programming Assignment 2.1
Author: Dustin Trott
Create Date: September 7, 2021

For week 2, Exercise 2.1 we will:
    
 - Display the text “Hello World! I wonder why that is always the default 
   coding text to start with”
 - Add two numbers together
 - Subtract a number from another number
 - Multiply two numbers
 - Divide between two numbers
 - Concatenate two strings together (any words)
 - Create a list of 4 items (can be strings, numbers, both)
 - Append an item to your list (again, can be a string, number)
 - Create a tuple with 4 items (can be strings, numbers, both)
"""
"""
Change Log
    - [09.07.21] Initial Commit
"""

print("\n") #adding a blank line to make the output easier to read
print("Hello World! I wonder why that is always the default coding text to start with?") #printing hello world statement
print("\n") #adding a blank line to make the output easier to read

x = 21 # defining x as 21
y = 19 # defining y as 19

sum = int(x) + int(y) # adding x(21) and y(19) together
print("21 + 19 is: ",sum) # printing x(21) plus y(19)
print("\n") #adding a blank line to make the output easier to read

minus = int(x) - int(y) # subtracting x(21) from y(19)
print("21 - 19 is: ",minus) # printing x(21) plus y(19)
print("\n") #adding a blank line to make the output easier to read

multiply = int(x) * int(y) # multiplying x(21) times y(19)
print("21 * 19 is: ",multiply) # printing x(21) plus y(19)
print("\n") #adding a blank line to make the output easier to read

divide = int(x) / int(y) # dividinging x(21) by y(19)
print("21 / 19 is: ",divide) # printing x(21) plus y(19)
print("\n") #adding a blank line to make the output easier to read

print("My name is:"+" "+"Dustin Trott") # concatenating strings
print("\n") #adding a blank line to make the output easier to read

my_list = [1, "Howdy", 5.0, "Dustin"]
print(my_list) # printing the list of 4 items I created
print("\n") #adding a blank line to make the output easier to read

my_list.append("Ohio State Buckeye's won") # appending to my origianl list
print(my_list) # printing appended list
print("\n") #adding a blank line to make the output easier to read

my_tuple = ("science", "data", "unchangeable", "coding")
print(my_tuple)