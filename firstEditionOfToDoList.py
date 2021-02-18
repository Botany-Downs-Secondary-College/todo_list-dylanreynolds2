# ToDoList.py
# Dylan Reynolds 18/02/2021

#Clears textbox

# Declares the list
todo_list = []

# Functions
urn selections

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
        
    elif selection == '3':
        break
    else:
        print('That isnt a valid option: ')

print('thank you for using our program!')
