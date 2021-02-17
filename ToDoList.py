# ToDoList.py
"""
Design and write code for to-do-list programme. The programme must 
ask user to choose '1' to add to to do list, '2' to display to do 
list and '3' to exit. Declare list called todo_list, use three functions
menu(), add_tasks(), view_list(), the main routine must have while loop
and elifs.
"""
# Dylan Reynolds 18/06/2020

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
        os.system('cls')
        task = input("Enter the task to add or type 'end' to return to menu: ")
        if task == 'end':
            os.system('cls')
            break
        else:
            todo_list.append(task)
            os.system('cls')
            break

def view_list():
    os.system('cls')
    print('this is your list:')
    for task in todo_list:
        print('- {}'.format(task))

# welcomes the user and asks what they would like
os.system('cls')
print('Welcome to the to do list program!')

# Selects the functions
while True:
    selection=todo_menu()

    if selection == '1':
        add_task()
        
    elif selection == '2':
        view_list()
        time.sleep(4)
        os.system('cls')
        
    elif selection == '3':
        os.system('cls')
        break
    else:
        print('THat isnt a valid option: ')

print('thank you for using our program')
