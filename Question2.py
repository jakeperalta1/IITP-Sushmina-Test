RED = "red"
BLUE = "blue"
YELLOW ="yellow"

x= input("Enter the first primary color :")
y= input("Enter the second primary color: ")

if x!= RED:
    print("Error: Invalid Color1")

elif y!= RED:
    print("Error:Invalid Color2")

elif x!=BLUE:
    print("Error: Invalid Color1")
    
elif y!=BLUE:
    print("Error:Invalid Color2")
    
elif x!=YELLOW:
    print("Error: Invalid Color1")



elif y!= YELLOW:
    print("Error:Invalid Color2")

elif x==y:
    print("Error: The two colors you entered are same")
    
elif x==RED and y==BLUE:
    print ("purple")
elif x==RED and y==YELLOW:
    print("orange")
elif x==BLUE and y==RED:
    print("purple")
elif x==BLUE and y==YELLOW:
    print("green")
elif x==YELLOW and y==RED:
    print("orange")
elif x==YELLOW and y==BLUE:
    print("green")

    
    

