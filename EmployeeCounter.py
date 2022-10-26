#the program created an Emplyee details and also count

class Employee:
    i=0
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        Employee.i +=1

#methods creation for to count number of employee and to print employee details
    def displaycount(self):
        print('Total number of Emplyee is:' + str(Employee.i))

    def displayDetails(self):
        print('Name: ', self.name , 'Email:', self.email, 'Age: ', self.age)

#Creating an instance of the Class Object Employee
emp_1 = Employee('Waheed', 'flexy@h.com', '35')
emp_1.displayDetails()
emp_1.displaycount()

emp_2 = Employee('Ibrahim', 'aib@gmail.com', 30)
emp_2.displaycount()
emp_2.displayDetails( )

emp_3 = Employee('abidemi', 'abi@mail.com', '30')
emp_3.displaycount()
emp_3.displayDetails()

emp_4 = Employee('Jummy', 'jummy@mail.com', '25')
emp_4.displaycount()
emp_4.displayDetails()

emp_3 = Employee('Shakiru', 'shakiru@mail.com', '34')
emp_3.displaycount()
emp_3.displayDetails()


