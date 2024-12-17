print("--- Python OOP Project: Employee Management System ---\n")
class Employee:
    def __init__(self,id,name,age,salary,department):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
    def setData(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.id = (input("Enter Employee ID : "))
        self.salary = int(input("Enter Salary: "))
    def getData(self):
        print(f"Employee created with Name: {self.name} , Age: {self.age}, Employee ID: {self.id}, Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, id, name, age, salary, department):
        super().__init__(id, name, age, salary, department)
    def setmanagerdata(self):
          self.department = input("Enter department :")
    def display(self):
        return f"Manager - Name: {self.name}, Age: {self.age}, Employee ID: {self.id}, Salary: {self.salary}, Department: {self.department}"
class Developer(Employee):
    pass

while True:
    choice = int(input("Choose an operation : \n 1. Create a Person\n 2. Create an Employee\n 3. Create a Manager\n 4. Show Details\n 5. Compare Salaries\n 6.Exit\n Enter your Choice : "))
    if choice == 1:
        person_name = input("Enter name : ")
        age_person = int(input("Enter age :\n"))
        print(f"Person created with name : {person_name} and age: {age_person}.\n")
        print("\n---Choose another operation---\n")

    elif choice == 2:
        emp = Employee("", "", 0, 0, "")
        emp.setData()
        emp.getData()
        print("\n---Choose another operation---\n")
    elif choice == 3:
        man = Manager("", "", 0, 0, "",)
        man.setmanagerdataData()
        print(man.display())
        print("\n---Choose another operation---\n") 
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        print("\nExiting the system. All resources have been Freed. ")
        print("\nGoodbye!")       
        break
    else:
        print("You have Entered the wrong option....")