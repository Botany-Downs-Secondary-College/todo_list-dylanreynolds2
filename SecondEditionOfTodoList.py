# ToDoList.py
# Dylan Reynolds 18/02/2021

#Clears textbox
import os
import time

# Declares the list
todo_list = []

# Functions
def todo_menu():
    selections = input('Chose a mode by entering the the number: \n1: Add a task\n2: View List\n3: Exit\n: ')
    return selections

def add_task():
    while True:
        task = input("Enter the task to add or type 'end' to return to menu: ")
        if task == 'end':
            break
        else:
            todo_list.append(task)
	    break

def view_list():
    print('this is your list:')
    for task in todo_list:
        print('- {}'.format(task))

# Welcomes the user and asks what they would like
print('Welcome to the to do list program!')

# Main Routine
while True:
    selection=todo_menu()

    if selection == '1':
        add_task()
        
    elif selection == '2':
        view_list()
        
    elif selection == '3':
        break
    else:
        print('That isnt a valid option: ')

print('thank you for using our program!')
