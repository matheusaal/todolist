from ToDoList import *
from interface import *

def main():

    layout = Interface()

    layout.logo()

    layout.menu()

    userToDoList = ToDoList()

    userOption = -1
        
    while (userOption != "6"):

        userOption = input("Enter your option: ")

        if (userOption == "1"):

            userTask = input("\nAdd the task: ")
            userToDoList.addTask(userTask)

        if (userOption == "2"):

            userToDoList.viewTasks()

        if (userOption == "3"):
            
            taskToBeUpdated = input("Choose the task: ")
            userToDoList.updateTaskStatus(taskToBeUpdated)

        if (userOption == "4"):
            
            userToDoList.removeTask()

        if (userOption == "5"):

            pass

    print("Thanks for using our program.")

if __name__ == "__main__":

    main()

