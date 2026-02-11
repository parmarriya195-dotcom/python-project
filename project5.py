class Employee:
    def __init__(self,employee_id=None,name="",age=0,salary=0):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    def getter_id (self):
        return self.__employee_id
    
    def setter_id(self,employee_id):
        self.__employee_id = employee_id
    
    def getter_salary (self):
        return self.__salary
    
    def setter_salary (self,salary):
        self.__salary = salary
    
    def display (self):
        print(f"Employee_id: {self.getter_id()}\n Name: {self.name}\n Age: {self.age}\n Salary: {self.getter_salary()}")

    def __del__ (self):
        pass

class Manager(Employee):
    def __init__(self, employee_id, name, age, salary,department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display (self):
        super().display()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, employee_id, name, age, salary,programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")

print("Manager is subclass of Employee:", issubclass(Manager, Employee))
print("Developer is subclass of Employee:", issubclass(Developer, Employee))

employees = []
managers = []
developers = []

while True:

    print("\nWelcome to Employee management system!\n")
    print("Enter 1 to add Employee!")
    print("Enter 2 to add Manager!")
    print("Enter 3 to add Developer!")
    print("Enter 4 to to view Info!")
    print("Enter 0 to Exit!\n")

    choice = int(input("Enter your choice: "))

    if choice == 1 :
        eid = int(input("\nEnter Employee_id: "))
        ename = input("Enter Employee name: ")
        eage = int(input("Enter Employee age: "))
        esalary = int(input("Enter Employee salary: "))

        eobj = Employee(eid,ename,eage,esalary)
        employees.append(eobj)
        
        print(isinstance(eobj, Employee))  
        print("Employee added successfully !\n")
    
    elif choice == 2:
        mid = int(input("\nEnter Manager_id: "))
        mname = input("Enter Manager name: ")
        mage = int(input("Enter Manager age: "))
        msalary = int(input("Enter Manager salary: "))
        mdepartment = input("Enter Department of Manager: ")

        mobj = Manager(mid,mname,mage,msalary,mdepartment)

        managers.append(mobj)

        print(isinstance(mobj, Employee))  
        print("Manager added successfully !\n")

    elif choice == 3:
        did = int(input("\nEnter Developer_id: "))
        dname = input("Enter Developer name: ")
        dage = int(input("Enter developer age: "))
        dsalary = int(input("Enter Developer salary: "))
        dlanguage = input("Enter Programming language of developer: ")

        dobj = Developer(did,dname,dage,dsalary,dlanguage)

        print(isinstance(dobj, Employee))  
        developers.append(dobj)

        print("Developer added successfully !\n")

    elif choice == 4:
        print("\nEnter 1 to view Employee info!")
        print("Enter 2 to view Manager info!")
        print("Enter 3 to view Developer info!\n")

        vchoice = int(input("Enter your choice to view Info: "))

        if vchoice == 1:
            if not employees:
                print("No Employee found!")
            else:
                for emp in employees:
                    emp.display()

        elif vchoice == 2:
            if not managers:
                print("No Manager found!")
            else:
                for mgr in managers:
                    mgr.display()

        elif vchoice == 3:
            if not developers:
                print("No Developer found!")
            else:
                for dev in developers:
                    dev.display()

        else:
            print("Invalid choice!")

    elif choice == 0:
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice!")