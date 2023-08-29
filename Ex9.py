#Get the input for salary and age.
#If salary greater than or equal to 20000 or age less than or equal to 25, get input for required loan amount. If not print you
#are not eligible for loan.
#If required loan amount is less than or equal to 50000 print you are eligible for loan. If it is greater than 50000 print maximum
#loan amount is 50000.

Salary = int(input("Enter the Salary: "))
Age = int(input("Enter the age: "))

if(Salary>=20000 or Age<=25):
    loan = int(input("Loan: "))
    if(loan>50000):
        print("Maxium loan amount is 50000")
    else:
        print("Eligible")
else:
    print("Not Eligible for loan")
