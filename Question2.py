RED = "red"
BLUE = "blue"
YELLOW ="yellow"

x= input("Enter the first primary color :")
y= input("Enter the second primary color: ")

if (x=="red") and (y=="blue"):
    print("purple")

elif (x=="red")and (y=="yellow"):
    print("orange")

elif (x=="blue")and (y=="red"):
    print("purple")

elif (x=="blue")and (y=="yellow"):
    print("green")

elif (x=="yellow") and (y=="red"):
    print("orange")

elif(x=="yellow") and (y=="blue"):
    print("green")

elif(x!="red"):
    print("Invalid color1")

elif (y!= "red"):
    print("Error:Invalid Color2")

elif (x!= "blue"):
    print("Error: Invalid Color1")
    
elif (y!= "blue"):
    print("Error:Invalid Color2")
    
elif (x!= "yellow"):
    print("Error: Invalid Color1")



elif (y!= "yellow"):
    print("Error:Invalid Color2")

elif x==y:
    print("Error: The two colors you entered are same")
    
else:
    print(".")
    