#Get input for variable mark. If mark>35 print pass. Else print fail

'''
Marks = int(input("Ënter the marks:"))
if (Marks > 35):
    print("Pass")
else:
    print("Fail")

'''

#Get input for variable income. If income is greater than 7000 scholarship is available. Else not eligible for scholarship

'''
Income=int(input("Income: "))

if(Income>7000):
    print("available")
else:
    print("Not available")

'''
#Get input for a number and check whether it is divisible by both 3 and 5 or not. If yes then print, the number is divisible by 3 and 5
#else print the number is not divisible by 3 and 5

#Binary operator - AND, OR, NOT

'''
Number = int(input("Enter the number:"))

if(Number%3==0 and Number%5==0):
    print("Divisible by 3 and 5")
else:
    print("Not Divisible by 3 and 5")

'''

#Get input for a number and find it is even or odd

'''

Number = int(input("Enter the number: "))

if(Number%2==0):
    print("Number is even")
else:
    print("Number is odd22")

'''
#Get input for score out of 100.
#If score is <35 = "Need to improve"
#If score is greater than 35 but < than 70="Ävg"
#If score is greater than 70 = "Good"

Score = int(input("Enter the score: "))

if(Score<35):
    print("Need to improve")
elif(Score>35 and Score<70):
    print("Avg Student")
elif(Score>70 and Score<100):
    print("Good Student")
else:
    print("Invalid Input")


