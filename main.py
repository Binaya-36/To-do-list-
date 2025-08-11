#create an empty list to store the tasks and their status
todo_list= []

#function to add task to the todo list
def add_task():
    task=input("\nEnter the task:")
    todo_list.append({"Task":task,"Status":"Pending"})
    print("Task added succesfully\n")

#function to view the task
def view_task():
            if(len(todo_list)==0):
                print("No task available")
            else:
                for index,task in enumerate(todo_list,start=1):
                  print(f"{index:}.{task['Task']}-{task['Status']}")

#function to remove the task
def remove_task():
    if len(todo_list)==0:
        print("List is empty")
    else:
        value=int(input("Enter the task number you want to remove:"))-1
        if 0<= value <len(todo_list):
         removed_task=todo_list.pop(value)
        else:
            print("The number you wrote isn't available")   

#function to mark task as completed
def mark_done():
        if len(todo_list)==0:
          print("List is empty")
        else:
            value=int(input("Enter the work you want to mark as completed:\n"))-1
        if 0<= value <len(todo_list):
            todo_list[value]['Status']='Completed'
            print(f"{todo_list[value]['Task']} is marked as completed")
        else:
            print("The number you wrote isn't available")

def exit_button():
    print("Byee byee")
    exit()

# function to display the menu
def menu():
    while(True):
        print("**Menu**")
        print("1.Add a new task")
        print("2.View all the tasks")
        print("3.Remove the tasks")
        print("4.Mark a task as completed")
        print("5.Exit")

        

        choice=input("What you want to do?\n")
        if(choice=="1"):
            add_task()
        elif(choice=="2"):
            view_task()
        elif(choice=="3"):
            remove_task()
        elif(choice=="4"):
            mark_done()
        elif(choice=="5"):
            exit_button()
        else:
            print("Wrong choice")

menu()

