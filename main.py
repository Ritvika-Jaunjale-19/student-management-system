print("===== STUDENT MANAGEMENT SYSTEM =====")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll no: ")
        marks = int(input("Enter marks: "))

        students.append([name, roll, marks])
        print("Student added!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for s in students:
                print("\nName:", s[0])
                print("Roll No:", s[1])
                print("Marks:", s[2])

    elif choice == "3":
        roll = input("Enter roll no: ")

        for s in students:
            if s[1] == roll:
                print("\nName:", s[0])
                print("Roll No:", s[1])
                print("Marks:", s[2])
                break
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll no: ")

        for s in students:
            if s[1] == roll:
                students.remove(s)
                print("Student deleted!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
