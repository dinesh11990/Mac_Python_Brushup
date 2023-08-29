#Get input for five subjects marks. Add all of it, And find average. If average mark is less than 35. Print
#"Additional class is required" else print "you are good to go"

Phy = int(input("Enter the marks 1: "))
Math = int(input("Enter the marks 2: "))
Chemis = int(input("Enter the marks 3: "))
Zoo = int(input("Enter the marks 4: "))
Bot = int(input("Enter the marks 5: "))

Total=(Phy+Math+Chemis+Zoo+Bot) / 5

if(Total<35):
    print("Additional class is required")
else:
    print("You r good to go")