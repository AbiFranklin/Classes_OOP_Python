from dataclasses import dataclass

# Long way to create class
# class Project:
#     def __init__(self, name, payment, client) -> None:
#         self.name = name
#         self.payment = payment
#         self.client = client
#
#     def __repr__(self) -> str:
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"

# The Project class represents a project with a name, payment, and client.
# It includes a method to notify the client about the project's progress.


@dataclass(slots=True)
class Project:
    """
    A class representing a project.

    Attributes:
        name (str): The name of the project.
        payment (int): The payment for the project.
        client (str): The client for the project.
    """
    name: str
    payment: int
    client: str

    def notify_client(self):
        """
        Notifies the client about the progress of the project.
        """
        print(
            f"Notifying {self.client} about the progress of the {self.name} ...")


class Employee:
    """
    A class representing an employee.

    Attributes:
        name (str): The name of the employee.
        age (int): The age of the employee.
        salary (float): The salary of the employee.
        project (Project): The project the employee is working on.
    """

    def __init__(self, name, age, salary, project) -> None:
        """
        Initializes an Employee object.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            salary (float): The salary of the employee.
            project (Project): The project the employee is working on.
        """
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


# Create an instance of Project
p = Project("Django App", 20000, "Globomantics")

# Create an instance of Employee
e = Employee("Abi", 39, 1000, p)

# Output the project details
print(e.project)

# Notify the client about the project progress
e.project.notify_client()
