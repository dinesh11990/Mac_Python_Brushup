#Get input for variable mark. If mark>35 print pass. Else print fail


Marks = int(input("Ënter the marks:"))
if (Marks > 35):
    print("Pass")
else:
    print("Fail")

#Get input for variable income. If income is greater than 7000 scholarship is available. Else not eligible for scholarship

Income=int(input("Income: "))

if(Income>7000):
    print("available")
else:
    print("Not available")

#Get input for a number and check whether it is divisible by both 3 and 5 or not. If yes then print, the number is divisible by 3 and 5
#else print the number is not divisible by 3 and 5

#Binary operator - AND, OR, NOT

Number = int(input("Enter the number:"))

if(Number%3==0 and Number%5==0):
    print("Divisible by 3 and 5")
else:
    print("Not Divisible by 3 and 5")