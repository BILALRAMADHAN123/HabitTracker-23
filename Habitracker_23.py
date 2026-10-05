# Membuat To Do list sederhana dengan menggunakan python

# the place where store the tasks
tasks = []

# the function for show up the menu
def menu ():
    print("\n" + 30* "=" )
    print("    BYV TO DO LIST")
    print(30 * "=")
    print("Select an Option Below:")
    print("1. See all Tasks ")
    print("2. Add a Task")
    print("3. Insert task by number ")
    print("4. Extract the Last task")
    print("5. Extract the task by number ")
    print("6. Search a task")
    print("7. Amoun total of tasks ")
    print("8. Exit")
    print("\n" + 30* "=")

#the main program logic
while True:
    
    menu ()

    option = input("Select an option (1-8)") #first ask
    print("Option entered:", option)
    
    #logic

    if option == "1": #see all tasks
        if len(tasks) == 0:
            print("Not tasks yet")


        else:
            print("Task List:")
            for i in range(len(tasks)):
                    print(f"{i+1}.{tasks[i]}")
        

    elif option == "2": #Add a task
        task = input("Add a task: ")
        tasks.append(task)

        print("The task added succesfully")

    elif option == "3": #add a task by number

        if len(tasks) == 0:
            print(" No Task available")
            
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")

            coor = int(input("Select the position:"))
            tax = input(" Insert a Task:")

            if coor < 1 or coor > len(tasks)+1 : #cuz from zero
                    print("Failed to added the task")
                    
            else: 
                    tasks.insert(coor-1,tax)
                    print("The task added succesfully")

    elif option == "4": #remove last task

        if len(tasks) == 0:
            print("No Task Available:")
            
        else: 
            removed = tasks.pop()
            print(f"'{removed}' was succesfully to convert")

    elif option == "5": #remove task by number

        if len(tasks) == 0 :
            print("No Task Available:")

        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")

            kor = int(input("Select number of task do you want to remove:"))

            if kor < 1 or kor > len(tasks):
                print("Number not vaild")

            else:
                remoked = tasks.pop(kor -1)
                print(f"'{remoked}' was succesful6ly to convert")

    elif option == "6" : #search a task

        if len(tasks) == 0 :
            print("No Task Available:")

        else:
            seach = input("Enter your task name: ")

            located = False
            
            for i in range(len(tasks)) :

                if tasks[i].lower() == seach.lower():
                    print(f"Found in number {i+1}")
                    located = True
                    break

            if not located :
                print("Sorry, Task not founded")

    elif option == "7":
        print(f'The amount total of task is : {len(tasks)}')

    elif option == "8":
        print("Thank for using this BYV ToDoList")
        break

    else: 
        print("Sorru, The menu not listesd")
