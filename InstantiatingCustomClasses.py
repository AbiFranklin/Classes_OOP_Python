class Employee:
    """
    A class to represent an employee.

    Attributes
    ----------
    name : str
        Name of the employee
    age : int
        Age of the employee
    salary : float
        Salary of the employee
    position : str
        Position of the employee

    Methods
    -------
    increase_salary(percent):
        Increases the salary of the employee by a given percentage.
    __str__():
        Returns a string representation of the employee's information.
    __repr__():
        Returns a string that would recreate the object when evaluated.
    """

    def __init__(self, name, age, salary, position) -> None:
        """
        Constructs all the necessary attributes for the employee object.

        Parameters
        ----------
        name : str
            Name of the employee
        age : int
            Age of the employee
        salary : float
            Salary of the employee
        position : str
            Position of the employee
        """
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

    def increase_salary(self, percent: float) -> None:
        """
        Increases the salary of the employee by a given percentage.

        Parameters
        ----------
        percent : float
            The percentage by which the salary should be increased
        """
        self.salary += self.salary * (percent / 100)

    def __str__(self) -> str:
        """
        Returns a string representation of the employee's information.

        Returns
        -------
        str
            A formatted string containing the employee's details
        """
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with a salary of ${self.salary:.2f}."
    
    def __repr__(self) -> str:
        """
        Returns a string that would recreate the object when evaluated.

        Returns
        -------
        str
            A string representation of the employee that can be used to recreate the object
        """
        return f"Employee('{self.name}', {self.age}, {self.salary}, '{self.position}')"


# Create instances of Employee
e = Employee('Abi', 39, 2000, "Programmer")
f = Employee('Bob', 23, 1000, "Driver")

# Increase salary and print information
e.increase_salary(30)
print(e)

# Use repr to recreate the object and print it
g = eval(repr(e))
print(g)
