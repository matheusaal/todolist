class ToDoList():

    def __init__(self):

        self.tasks = []
    
    def addTask(self, task):

        self.tasks.append([task, 0])
        
        print("\nTask successfully created.\n")

    def updateTaskStatus(self, taskNumber):
        
        taskIndex = int(taskNumber) - 1

        if (self.tasks[taskIndex][1] == 0):

            self.tasks[taskIndex][1] = 1

        else:

            self.tasks[taskIndex][1] = 0

        print("\nTask status successfully updated.\n")

    def viewTasks(self):
        
        tasksQuantity = len(self.tasks)
        
        for i in range(tasksQuantity):

            if (self.tasks[i][1] == 0):

                print((i + 1), ". [ ] ", self.tasks[i][0], sep="", end="\n\n")

            else:

                print((i + 1), ". [X] ", self.tasks[i][0], sep="", end="\n\n")

    def removeTask(self, taskNumber):
        
        taskIndex = int(taskNumber) - 1

        self.tasks.pop(taskIndex)
        
        print("\nTask successfully removed.\n")

    def generateFile(self, fileName):

        tasksQuantity = len(self.tasks)

        with open(fileName, 'w', encoding='utf-8') as file:

            for i in range(tasksQuantity):

                if (self.tasks[i][1] == 0):

                    file.write(str(i + 1) + ". [ ] " + self.tasks[i][0] + "\n\n")

                else:

                    file.write(str(i + 1) + ". [X] " + self.tasks[i][0] + "\n\n")

        print("\nFile successfully generated.\n")