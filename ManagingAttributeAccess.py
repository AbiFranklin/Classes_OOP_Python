class Employee:
    """
    A class to represent an employee.

    Attributes
    ----------
    name : str
        The name of the employee.
    age : int
        The age of the employee.
    salary : float
        The monthly salary of the employee.
    position : str
        The job position of the employee.
    _annual_salary : float
        The cached annual salary of the employee (initialized to None).

    Methods
    -------
    increase_salary(percent: float) -> None:
        Increases the salary of the employee by a given percentage.
    __str__() -> str:
        Returns a string representation of the employee's details.
    __repr__() -> str:
        Returns a detailed string representation of the employee that can recreate the object.
    salary() -> float:
        Property that returns the monthly salary of the employee.
    salary(salary: float) -> None:
        Setter for the salary property to enforce a minimum wage.
    annual_salary() -> float:
        Property that calculates and returns the annual salary of the employee, caching the result.
    """

    def __init__(self, name, age, salary, position) -> None:
        """
        Constructs all the necessary attributes for the employee object.

        Parameters
        ----------
        name : str
            The name of the employee.
        age : int
            The age of the employee.
        salary : float
            The monthly salary of the employee.
        position : str
            The job position of the employee.
        """
        self.name = name
        self.age = age
        self.salary = salary  # This will use the setter to enforce the minimum wage
        self.position = position
        self._annual_salary = None  # Initialize the cached annual salary to None

    def increase_salary(self, percent: float) -> None:
        """
        Increases the salary of the employee by a given percentage.

        Parameters
        ----------
        percent : float
            The percentage by which the salary should be increased.
        """
        self.salary += self.salary * (percent / 100)

    def __str__(self) -> str:
        """
        Returns a string representation of the employee's details.

        Returns
        -------
        str
            A formatted string containing the employee's name, age, position, and salary.
        """
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with a salary of ${self.salary:.2f}."
    
    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the employee.

        Returns
        -------
        str
            A string representation of the employee that can be used to recreate the object.
        """
        return f"Employee('{self.name}', {self.age}, {self.salary}, '{self.position}')"
    
    @property
    def salary(self):
        """
        Property that returns the monthly salary of the employee.

        Returns
        -------
        float
            The monthly salary of the employee.
        """
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        """
        Setter for the salary property to enforce a minimum wage and reset the annual salary cache.

        Parameters
        ----------
        salary : float
            The monthly salary to be set.

        Raises
        ------
        ValueError
            If the salary is less than the minimum wage.
        """
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._annual_salary = None  # Reset the annual salary cache
        self._salary = salary

    @property
    def annual_salary(self):
        """
        Property that calculates and returns the annual salary of the employee, caching the result.

        Returns
        -------
        float
            The annual salary of the employee.
        """
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12  # Calculate and cache the annual salary
        return self._annual_salary

# Create instances of Employee
e = Employee('Abi', 39, 1200, "Programmer")
f = Employee('Bob', 23, 1000, "Driver")

# Print the monthly salary of employee 'e'
print(e.salary)

# Print the string representation of employee 'e'
print(e)

# Print the annual salary of employee 'e'
print(e.annual_salary)

# Update the salary of employee 'e'
e.salary = 1000

# Print the updated annual salary of employee 'e'
print(e.annual_salary)
