# Student Management System

students = {}

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students[roll] = [name, marks]
        print("Student Added!")

    elif choice == "2":
        print("\nStudent Records")
        for roll in students:
            print("Roll No:", roll)
            print("Name:", students[roll][0])
            print("Marks:", students[roll][1])
            print("----------------")

    elif choice == "3":
        roll = input("Enter Roll No to search: ")

        if roll in students:
            print("Name:", students[roll][0])
            print("Marks:", students[roll][1])
        else:
            print("Student Not Found!")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Wrong Choice")
