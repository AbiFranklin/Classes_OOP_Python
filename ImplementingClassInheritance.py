class Employee:
    """
    A class representing an employee with a name, age, and salary.

    Attributes:
        name (str): The name of the employee.
        age (int): The age of the employee.
        salary (float): The salary of the employee.
    """

    __slots__ = ("name", "age", "salary")

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

    def increase_salary(self, percent):
        """
        Increases the salary of the employee by a given percentage.

        Args:
            percent (float): The percentage to increase the salary by.
        """
        self.salary += self.salary * (percent / 100)

    def has_slots(self):
        """
        Checks if the class has defined slots.

        Returns:
            bool: True if the class has defined slots, False otherwise.
        """
        return hasattr(self, "__slots__")


class SlotsInspectorMixin:
    """
    A mixin class to check if a class has defined slots.
    """

    __slots__ = ()

    def has_slots(self):
        """
        Checks if the class has defined slots.

        Returns:
            bool: True if the class has defined slots, False otherwise.
        """
        return hasattr(self, "__slots__")


class Tester(Employee, SlotsInspectorMixin):
    """
    A class representing a tester, inheriting from Employee and SlotsInspectorMixin.
    """

    def run_tests(self):
        """
        Simulates running tests.
        """
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")


class Developer(SlotsInspectorMixin, Employee):
    """
    A class representing a developer, inheriting from SlotsInspectorMixin and Employee.

    Attributes:
        framework (str): The framework the developer works with.
    """

    __slots__ = ("framework",)

    def __init__(self, name, age, salary, framework) -> None:
        """
        Initializes a Developer object.

        Args:
            name (str): The name of the developer.
            age (int): The age of the developer.
            salary (float): The salary of the developer.
            framework (str): The framework the developer works with.
        """
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        """
        Increases the salary of the developer by a given percentage and an optional bonus.

        Args:
            percent (float): The percentage to increase the salary by.
            bonus (float, optional): An additional bonus to add to the salary. Default is 0.
        """
        super().increase_salary(percent)
        self.salary += bonus


# Create instances of Tester and Developer
e = Tester("Abi", 23, 1200)
d = Developer("Bill", 44, 200, 'JS')

# Increase salary for Tester and Developer
e.increase_salary(50)
print(e.salary)

# Run tests for Tester
e.run_tests()

# Increase salary for Developer with bonus
d.increase_salary(50, 50)
print(d.salary)
print(d.name, d.framework)


class Test(object):
    """
    A simple test class.
    """
    pass


# Create an instance of Test
test = Test()
print(repr(test))

# Check if instances are of certain types
print(isinstance(e, Tester))
print(isinstance(d, Developer))

# Check if classes are subclasses of certain classes
print(issubclass(Developer, Employee))
print(issubclass(Employee, object))
print(issubclass(Developer, object))

# Create an instance of Employee and check slots
emp = Employee("Abi", 23, 1200)
print(emp.__slots__)

# Dynamically add an attribute to the Tester instance
e.new_attribute = 2
print(e.new_attribute)

# Check if Developer has slots
print(d.has_slots())

# Print method resolution order (MRO)
print(Developer.__mro__)
print(Tester.__mro__)
