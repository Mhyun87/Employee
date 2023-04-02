class Employee:
    """
    Employee class definition
    """

    def __init__(self, firstName, lastName, salary=0.00):
        """
        constructs an Employee object
        note that if no salary is provided, it defaults to 0
        """
        # store the Employee firstName
        self.firstName = firstName
        
        # store the Employee lastName
        self.lastName = lastName
        
        # store the Employee salary
        self.salary = salary

    def __str__(self):
        """
        returns the string representation of an Employee object
        the string should include:
            the first name followed by a space
            the last name followed by a space
            the salary with a leading $ and 2 fractional digits for cents
        """
        # Employee firstName
        s  = "firstName: " + self.firstName
        
        s += ", "
        
        # Employee lastName
        s  = "lastName: " + self.lastName
        
        s += ", "
        
        # Employee salary with a leading $ and 2 fractional digits for cents
        s += "salary: " + str("$%.2f" % self.salary)
        
        return s
        
