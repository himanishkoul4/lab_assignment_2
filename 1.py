class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif key == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif key == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")

    def display_table(self):
        for employee in self.employees:
            print(employee)


def main():
    employee_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    employee_table = EmployeeTable(employee_data)

    print("Select sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    sorting_parameter = int(input("Enter your choice (1/2/3): "))

    employee_table.sort_employees(sorting_parameter)

    print("\nSorted Employee Table:")
    employee_table.display_table()


if __name__ == "__main__":
    main()
