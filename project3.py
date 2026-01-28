store = []

while True:
    print("\nWelcome to the student data organiszer!\n")

    print("\nselect an option: ")
    print("Enter 1 to Add student")
    print("Enter 2 to display all student")
    print("Enter 3 to update student information")
    print("Enter 4 to delete student")
    print("Enter 5 to display subject offered")
    print("Enter 6 to exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student = {
           "Student id": (int(input("Enter student id: ")),),
           "Name": input("Enter student name: "),
           "Age": int(input("Enter age: ")),
           "Grade": input("Enter student garde: "),
           "Date of Birth": (input("Enter date of birth (YYYY-MM-DD): "),),
           "Subjects": set(input("Enter Subjects (comma separated): ").split(","))
        }

        store.append(student)
        
        print("\nDetails added successfully!\n")

    elif choice == 2:
        print("\nData of all Students: \n")
        for st in store:
            print(st)

    elif choice == 3:
        stid = int(input("Enter student id for update information: "))
         
        for st in store:
            if st["Student id"][0] == stid:
                st["Name"] = input("enter new name: ")
                st["Age"] = int(input("Enter new age: "))
                st["Grade"] = input("Enter new Grade: ")
                st["Subjects"] = set(input("Enter new Subjects: ").split(","))

                print("\nUpdated Successfully!\n")

    elif choice == 4:
        stid = int(input("Enter id to delete information: "))
        for st in store:
            if st["Student id"][0] == stid:
                store.remove(st)

                print("\nDelete information successfully!\n")
        
    elif choice == 5:
        subjects = set()

        for st in store:
            for sub in st["Subjects"]:
                subjects.add(sub)

        print("\nSubjects Offered: ")
        for s in subjects:
            print(s)

    elif choice == 6:
        print("Thank You For Visiting!")
        break

    else:
        print("Invalid choice!")