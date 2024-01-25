from ToDoList import *
from interface import *

def main():

    layout = Interface()

    layout.logo()

    userToDoList = ToDoList()

    userOption = -1
        
    while (userOption != "6"):

        layout.menu()
        userOption = input("Enter your option: ")
        print()

        if (userOption == "1"):

            userTask = input("Add the task: ")
            userToDoList.addTask(userTask)

        if (userOption == "2"):

            userToDoList.viewTasks()

        if (userOption == "3"):
            
            taskToBeUpdated = input("Choose the task: ")
            userToDoList.updateTaskStatus(taskToBeUpdated)

        if (userOption == "4"):

            taskToBeRemoved = input("Choose the task: ")
            userToDoList.removeTask(taskToBeRemoved)

        if (userOption == "5"):

            fileToBeGenerated = input("Choose the file name: ")
            userToDoList.generateFile(fileToBeGenerated)

    print("Thanks for using our program.\n")

if __name__ == "__main__":

    main()

