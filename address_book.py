''' Simple address book program that allows users to store and manage contact information '''

def add():
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter email: ")

    with open("contacts.txt", "a") as f:
        f.write(f"Name: {name} Phone: {number} Email: {email}\n")

def view():
    with open("contacts.txt", "r") as f:
        for line in f.readlines():
            contact = line.rstrip()
            print(contact)

def edit():
    option = int(input("Which contact would you like to edit? (enter line number): "))
    with open("contacts.txt", "r") as f:
        lines = f.readlines()
    
    name = input("Enter new name: ")
    number = input("Enter new number: ")
    email = input("Enter new email: ")

    lines[option - 1] = f"Name: {name} Phone: {number} Email: {email}\n"
    with open("contacts.txt", "w") as f:
        f.writelines(lines)

def delete():
    option = int(input("Which contact would you like to delete? (enter line number): "))
    with open("contacts.txt", "r") as f:
        lines = f.readlines()

    with open("contacts.txt", "w") as f:
        for number, line in enumerate(lines):
            if number + 1 not in [option]:
                f.write(line)

while True:
    mode = input("What would you like to do with the address book? (add/view/edit/delete) press q to exit: ").lower()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "edit":
        edit()
    elif mode == "delete":
        delete()
    elif mode == "q":
        break
    else:
        print("Invalid mode.")
