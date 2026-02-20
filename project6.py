from datetime import datetime

class JournalManager:

    def __init__(self, filename="Journal.txt"):
        self.filename = filename
        try:
            open(self.filename, "x").close()
        except FileExistsError:
            pass

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
            with open(self.filename, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("No journal entries found!")
        except PermissionError:
            print("Permission denied while accessing the file!")

    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ")
        try:
            with open(self.filename, "r") as file:
                content = file.read().split("\n\n")
                found = False
                for entry in content:
                    if keyword in entry:
                        print(entry)
                        print("-" * 40)
                        found = True
                if not found:
                    print("No entries found for:", keyword)
        except FileNotFoundError:
            print("No journal entries found! Please add an entry first.")


    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            try:
                open(self.filename, "w").close()
                print("All entries deleted!")
            except FileNotFoundError:
                print("No journal entries to delete.")


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
