# Microsoft: DEV274x Introduction to Python: Fundamentals
# Module 2 Required Coding Activity
# Introduction to Python (Unit 2) Fundamentals
# This Activity is intended to be completed in the jupyter notebook, Required_Code_MOD2_IntroPy.ipynb,
# and then pasted into the assessment page that follows.
# All course .ipynb Jupyter Notebooks are available from the project files download topic in Module 1, Section 1.
# This is an activity based on code similar to the Jupyter Notebook Practice_MOD02_IntroPy.ipynb
# which you may have completed.
# Important Assignment Requirements
# NOTE: This program requires creating a function using def and return, using print output, input, if,
# in keywords, .append(), .pop(), .remove() list methods. As well as other standard Python
# Program: list-o-matic
# This program takes string input and checks if that string is in a list of strings
# if string is in the list it removes the first instance from list
# if string is not in the list the input gets appended to the list
# if the string is empty then the last item is popped from the list
# if the list becomes empty the program ends
# if the user enters "quit" then the program ends
# program has 2 parts
# program flow which can be modified to ask for a specific type of item. This is the programmers choice.
# Add a list of fish, trees, books, movies, songs.... your choice.
# list-o-matic Function which takes arguments of a string and a list.
# The function modifies the list and returns a message as seen below.


def list_o_matic(input_string, input_list):
    if input_string == "":
        return print(input_list.pop(), "popped from list")
    else:
        if input_string in input_list:
            input_list.remove(input_string)
            return print(input_string, "removed from list")

        else:
            input_list.append(input_string)
            return print("1 instance of", input_string, "appended to list")


check_list = ['cat', 'goat', 'cat', 'horse']

while check_list:
    check_string = input("enter the name of an animal or Quit/quit for quit:")
    if check_string.lower() == "quit":
        break
    else:
        list_o_matic(check_string, check_list)
