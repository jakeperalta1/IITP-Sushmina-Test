#asking input
m= int(input("Enter the month in the numeric form:"))
d= int(input("Enter the day in numeric form: "))
y= int(input("Enter the year as two numerical digits: "))




# giving Response
if (m>12):
    print("Error: Invalid Month Input")
    
elif(d>31):
    print("Error: Invalid Day Input")
    
elif(y>99):
    print("Error: Invalid Year Input")
    
else:
    print("The date is",m ,"/", d ,"/", y )
    print("Success: Congratulations! you entered the correct date.")