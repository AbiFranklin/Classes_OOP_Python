class Employee:
    """
    A class to represent an employee.

    Attributes
    ----------
    name : str
        The name of the employee.
    _salary : float
        The private salary attribute of the employee.

    Methods
    -------
    increase_salary(percent: float) -> None:
        Increases the salary of the employee by a given percentage.
    __str__() -> str:
        Returns a string representation of the employee's details.
    __repr__() -> str:
        Returns a detailed string representation of the employee that can recreate the object.
    salary() -> float:
        Property that raises an AttributeError because salary is write-only.
    """

    def __init__(self, name, salary) -> None:
        """
        Constructs all the necessary attributes for the employee object.

        Parameters
        ----------
        name : str
            The name of the employee.
        salary : float
            The salary of the employee.
        """
        self.name = name
        self.salary = salary  # Using the setter to enforce the minimum wage

    def increase_salary(self, percent: float) -> None:
        """
        Increases the salary of the employee by a given percentage.

        Parameters
        ----------
        percent : float
            The percentage by which the salary should be increased.
        """
        self._salary += self._salary * (percent / 100)

    def __str__(self) -> str:
        """
        Returns a string representation of the employee's details.

        Returns
        -------
        str
            A formatted string containing the employee's name and salary.
        """
        return f"{self.name} has a salary of ${self._salary:.2f}."
    
    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the employee.

        Returns
        -------
        str
            A string representation of the employee that can be used to recreate the object.
        """
        return f"Employee('{self.name}', {self._salary})"
    
    @property
    def salary(self):
        """
        Property that raises an AttributeError because salary is write-only.

        Raises
        ------
        AttributeError
            If an attempt is made to access the salary.
        """
        raise AttributeError("Salary is write only")
    
    @salary.setter
    def salary(self, salary: float) -> None:
        """
        Setter for the salary property to enforce a minimum wage.

        Parameters
        ----------
        salary : float
            The salary to be set.

        Raises
        ------
        ValueError
            If the salary is less than the minimum wage.
        """
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary

# Create instances of Employee
e = Employee('Abi', 2000)
f = Employee('Bob', 1000)

# Increase the salary using the setter method
e.salary = 25000
print(e)

# Try to access the salary (will raise an AttributeError)
# print(e.salary)  # Uncommenting this line will raise an AttributeError
