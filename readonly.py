class Employee:
    """
    A class to represent an employee.

    Attributes
    ----------
    name : str
        The name of the employee.
    _salary : float
        The private salary attribute of the employee (read-only).

    Methods
    -------
    __str__():
        Returns a string representation of the employee's details.
    __repr__():
        Returns a detailed string representation of the employee that can recreate the object.
    salary():
        Property that returns the salary of the employee.
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
        self._salary = salary  # Use a private attribute to store the salary

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
    def salary(self) -> float:
        """
        Property that returns the salary of the employee.

        Returns
        -------
        float
            The salary of the employee.
        """
        return self._salary
    
    @salary.setter
    def salary(self, salary: float) -> None:
        """
        Setter for the salary property to prevent modification of the salary attribute.

        Parameters
        ----------
        salary : float
            The salary to be set (not used since salary is read-only).

        Raises
        ------
        AttributeError
            If an attempt is made to set the salary.
        """
        raise AttributeError("Salary is read only")

# Create instances of Employee
e = Employee('Abi', 2000)
f = Employee('Bob', 1000)

# Print the salary and details of the employee
print(e.salary)
print(e)

# Try to set the salary (will raise an AttributeError)
# e.salary = 30000  # Uncommenting this line will raise an AttributeError