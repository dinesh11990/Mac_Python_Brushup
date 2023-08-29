#Get a input for score percentage. Only if the
#percentage is greater than 70, get input
#for his name, department and location.
#Then print you are eligible. If not print
#you are not eligible.

score = int(input("Enter the score %: "))

if(score>70):
    print("You're eligible! ")
    Name=input("Enter Name: ")
    Age=input("Enter Dept: ")
    print("You're eligible ")
else:
    print("You're not eligible ")

