#Make a mini calculator
#Get input for 2 numbers a and b
#Get input from user whether to add/
#/sub/mul/div

a=int(input("Enter the value A: "))
b=int(input("Enter the value B: "))

user=input("Enter the operation add/sub/mul/div: ")

if(user=="add"):
    print("Ans is: ",a+b)

elif(user=="sub"):
    print("Ans is: ",a-b)

elif(user=="mul"):
    print("Ans is: ",a*b)

elif(user=="div"):
    print("Ans is: ",a/b)
else:
    print("Invalid")
