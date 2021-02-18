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

# Welcomes the user and asks what they would like
os.system('cls')
print('Welcome to the to do list program!')

# Main Routine
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
        os.system('cls')
        print('That isnt a valid option: ')
        time.sleep(0.5)
        os.system('cls')

print('thank you for using our program!')
