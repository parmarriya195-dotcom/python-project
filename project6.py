# file = open("Journal.txt","w")

# while True:

#     print("welcome to personal Journal manager!\n")
#     print("Enter 1 to Add a new entry!")
#     print("Enter 2 to view all entries!")
#     print("Enter 3 to search for an entry!")
#     print("Enter 4 to delete all entry!")
#     print("Enter 0 to exit!\n")

#     try:
#         choice = int(input("Enter your choice: "))
#     except Exception:
#         print("Invalid input!")
    
#     if choice == 1:
#         add = input("Enter your Journal entry: ")

#         file = open("Journal.txt","a")
#         file.write(add+ "\n")
#         file.close()

#         print("Entry added successfully!")
    
#     elif choice == 2:
#         file = open("Journal.txt","r")
#         content = file.read()
#         print(content)
#         file.close()

#     elif choice == 3:

#         keyword = input("Enter a keyword or date to search: ")

#         file = open("Journal.txt","r")
#         content = file.readlines()

#         for line in content:
#             keyword
        
#         if keyword in line:
#             print(line)

#     elif choice == 4:
#         file = open("Journal.txt","W")
#         file.close()    

#     elif choice == 0:
#         print("Thnak you for visiting!")
#         break

#     else:
#         print("Invalid choice!")








from datetime import datetime

class JournalManager:

    def __init__(self, filename="Journal.txt"):
        self.filename = filename

    def add_entry(self):
        print("Enter your Journal entry (press ENTER on empty line to finish):")

        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        entry = "\n".join(lines)
        timestamp = datetime.now().strftime("(%d-%m-%Y %H:%M:%S)")

        try:
            with open(self.filename, "a") as file:
                file.write(f"{timestamp}\n{entry}\n\n")
            print("Entry added successfully!")
        except Exception as e:
            print("Error while writing entry:", e)


    def view_entries(self):
        try:
            file = open(self.filename, "r")
            content = file.read()
            print(content)
            file.close()
        except FileNotFoundError:
            print("No journal entries found!")

    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ")
        try:
            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword in line:
                        print(line)
                        found = True
                if not found:
                    print("No entries found for:", keyword)
        except FileNotFoundError:
            print("No journal entries found! Please add an entry first.")


    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            open(self.filename, "w").close()
            print("All entries deleted!")
        else:
            print("Delete operation cancelled.")


    def menu(self):
        while True:
            print("\nWelcome to Personal Journal Manager!\n")
            print("Enter 1 to Add a new entry!")
            print("Enter 2 to View all entries!")
            print("Enter 3 to Search for an entry!")
            print("Enter 4 to Delete all entries!")
            print("Enter 0 to Exit!\n")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input!")
                continue

            if choice == 1:
                self.add_entry()

            elif choice == 2:
                self.view_entries()

            elif choice == 3:
                self.search_entry()

            elif choice == 4:
                self.delete_entries()

            elif choice == 0:
                print("Thank you for visiting!")
                break

            else:
                print("Invalid choice!")

if __name__ == "__main__":
    jm = JournalManager()
    jm.menu()
