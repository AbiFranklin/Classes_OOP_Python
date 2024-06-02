from datetime import date


class Employee:
    """
    A class representing an employee.

    Attributes:
        minimum_wage (int): The minimum wage for all employees. Default is 1000.
    """
    minimum_wage = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage):
        """
        Changes the minimum wage for all employees.

        Args:
            new_wage (int): The new minimum wage.

        Raises:
            ValueError: If the new wage is greater than 3000.
        """
        if new_wage > 3000:
            raise ValueError("Company is bankrupt")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):
        """
        Creates a new employee with the minimum wage salary.

        Args:
            name (str): The name of the employee.
            dob (date): The date of birth of the employee.

        Returns:
            Employee: A new instance of Employee.
        """
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name, age, salary) -> None:
        """
        Initializes an Employee object.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            salary (float): The salary of the employee.
        """
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percentage):
        """
        Increases the salary of the employee by a given percentage.

        Args:
            percentage (float): The percentage to increase the salary by.
        """
        self.salary += self.salary * (percentage / 100)

    @property
    def salary(self):
        """
        Gets the salary of the employee.

        Returns:
            float: The salary of the employee.
        """
        return self._salary

    @salary.setter
    def salary(self, salary):
        """
        Sets the salary of the employee.

        Args:
            salary (float): The salary to set.

        Raises:
            ValueError: If the salary is less than the minimum wage.
        """
        if salary < Employee.minimum_wage:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary


# Create an instance of Employee
e = Employee("Abi", 39, 50000)

# Increase the salary of the employee using the increase_salary method
Employee.__dict__["increase_salary"](e, 20)
print(e.salary)  # Output the salary after increase

# Output the minimum wage for the employee instance and the Employee class
print(e.minimum_wage)  # This will output 1000
print(Employee.minimum_wage)  # This will output 1000

# Change the minimum wage using the class method
Employee.change_minimum_wage(400)
print(Employee.minimum_wage)  # Output the updated minimum wage, which will be 400

# Create a new employee using the class method
f = Employee.new_employee("Mary", date(1999, 8, 12))
print(f.name)  # Output the name of the new employee
print(f.age)  # Output the age of the new employee
print(f.salary)  # Output the salary of the new employee, which will be the minimum wage
