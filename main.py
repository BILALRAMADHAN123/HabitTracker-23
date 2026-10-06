# Membuat To Do List sederhana dengan Python

tasks = []

# =========================
# FUNCTION
# =========================

# Non-return tanpa parameter
def menu():
    print("\n" + 30 * "=")
    print("       KELEOMPOK 23 " \
    "")
    print(30 * "=")
    print("1. See all Tasks")
    print("2. Add a Task")
    print("3. Insert task by number")
    print("4. Extract the Last task")
    print("5. Extract the task by number")
    print("6. Search a task")
    print("7. Amount total of tasks")
    print("8. Exit")
    print(30 * "=")

# Non-return dengan parameter
def tampilkan_tugas(data):
    print("\nTask List:")
    for i in range(len(data)):
        print(f"{i + 1}. {data[i]}")

# Return tanpa parameter
def jumlah_tugas():
    return len(tasks)

# Return dengan parameter
def cek_tugas(nama):
    for task in tasks:
        if task.lower() == nama.lower():
            return True
    return False

# =========================
# METHOD
# =========================

class TodoList:

    def __init__(self, data):
        self.data = data

    # Non-return tanpa parameter
    def tampilkan(self):
        tampilkan_tugas(self.data)

    # Non-return dengan parameter
    def tambah(self, task):
        self.data.append(task)
        print("The task added successfully")

    # Return tanpa parameter
    def jumlah(self):
        return len(self.data)

    # Return dengan parameter
    def cari(self, nama):
        for task in self.data:
            if task.lower() == nama.lower():
                return True
        return False

# Membuat object
todo = TodoList(tasks)

# =========================
# MAIN PROGRAM
# =========================

while True:

    menu()

    option = input("Select an option (1-8): ")
    print("Option entered:", option)

    if option == "1":

        if len(tasks) == 0:
            print("No tasks yet")
        else:
            todo.tampilkan()

    elif option == "2":

        task = input("Add a task: ")
        todo.tambah(task)

    elif option == "3":

        if len(tasks) == 0:
            print("No task available")
        else:
            todo.tampilkan()

            coor = int(input("Select the position: "))
            task = input("Insert a task: ")

            if coor < 1 or coor > len(tasks) + 1:
                print("Failed to add the task")
            else:
                tasks.insert(coor - 1, task)
                print("The task added successfully")

    elif option == "4":

        if len(tasks) == 0:
            print("No task available")
        else:
            removed = tasks.pop()
            print(f"'{removed}' was successfully removed")

    elif option == "5":

        if len(tasks) == 0:
            print("No task available")
        else:
            todo.tampilkan()

            number = int(input("Select number of task to remove: "))

            if number < 1 or number > len(tasks):
                print("Number not valid")
            else:
                removed = tasks.pop(number - 1)
                print(f"'{removed}' was successfully removed")

    elif option == "6":

        if len(tasks) == 0:
            print("No task available")
        else:
            search = input("Enter your task name: ")

            if todo.cari(search):
                print("Task found")
            else:
                print("Sorry, task not found")

    elif option == "7":

        print(f"Total amount of tasks: {todo.jumlah()}")

    elif option == "8":

        print("Thank you for using this BYV To Do List")
        break

    else:

        print("Sorry, the menu is not listed")
