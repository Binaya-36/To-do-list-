#create an empty list to store the tasks and their status
todo_list= []
#function to add task to the todo list
def add_task():
    task=input("Enter the task:")
    todo_list.append({"Task":task,"Status":"Pending"})
    print("Task added succesfully")


# function to display the menu
def menu():
    while(True):
        print("**Menu**")
        print("1,Add a new task")
        print("2,View all the tasks")
        print("3,Remove the tasks")
        print("4,Mark a task as completed")
        print("5,Exit")

        choice=input("What you want to do?")
        if(choice=="1"):
            add_task()
        elif(choice=="2"):
            view_task()
        elif(choice=="3"):
            remove_task()
        elif(choice=="4"):
            mark_done()
        elif(choice=="5"):
            exit()
        else:
            print("Wrong choice")
menu()


