#import the Employee class definition from the Employee.py file
from Employee import Employee

def main():
    """
    the main program
    """
    print("Employee processing")
    print("")

    # create Employee objects
    # this code invokes the Employee class constructor (i.e., __init__(self, firstName, lastName, salary) )
    rick  = Employee( "Rick",  "DiPersio", 54000 )
    micki = Employee( "Micki", "DiPersio", 48000 )

    # print the starting salaries
    # here I am explicitly calling the __str__() method to get a string representation for the object
    print("Starting salaries:")
    print("  ",rick.__str__())
    print("  ",micki.__str__())
    print("")

    # give Rick DiPersio a 10% raise
    rick.salary = 1.1 * rick.salary

    # give Micki DiPersio a 10% raise
    micki.salary = 1.1 * micki.salary

    # print the salaries after the 10% raise
    # here Python implicitly calls the __str__() method to get a string representation for the object
    print("After a 10% raise:")
    print("  ",rick)
    print("  ",micki)

    # hold window open to allow user to view output
    print("")
    input("Press ENTER to continue ")
    
# call main()
if __name__ == "__main__":
    main()

