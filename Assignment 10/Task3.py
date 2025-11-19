class Employee:
    """
    Represents an employee with name and salary.
    
    Attributes:
        _name (str): Employee's name (private)
        _salary (float): Employee's salary (private)
    """
    
    def __init__(self, name, salary):
        """
        Initialize an Employee instance.
        
        Args:
            name (str): Employee's name
            salary (float): Employee's initial salary
        """
        self._name = name
        self._salary = float(salary)
    
    def increase_salary(self, percentage):
        """
        Increase employee's salary by a given percentage.
        
        Args:
            percentage (float): Percentage increase (e.g., 10 for 10% increase)
        """
        if percentage < 0:
            raise ValueError("Percentage must be non-negative")
        self._salary = self._salary + (self._salary * percentage / 100)
    
    def display_info(self):
        """
        Display employee information in a formatted way.
        """
        print(f"Employee: {self._name}, Salary: ${self._salary:,.2f}")
    
    # Property getters for better encapsulation
    @property
    def name(self):
        """Get employee's name."""
        return self._name
    
    @property
    def salary(self):
        """Get employee's salary."""
        return self._salary
    
    @salary.setter
    def salary(self, value):
        """Set employee's salary."""
        if value < 0:
            raise ValueError("Salary must be non-negative")
        self._salary = float(value)

# Test the class
if __name__ == "__main__":
    # Create employee instances
    emp1 = Employee("John Doe", 50000)
    emp1.display_info()
    # Increase salary by 10%
    emp1.increase_salary(10)
    emp1.display_info()
    # Another employee
    emp2 = Employee("smeed joe", 70000)
    emp2.display_info()
    # Increase salary by 15%
    emp2.increase_salary(15)
    emp2.display_info()
    # Access properties
    print(f"\nAccessing properties:")
    print(f"{emp1.name} earns ${emp1.salary:,.2f}")
