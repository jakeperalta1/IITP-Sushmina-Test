
    
x= float(input("Please enter your salary in Germany:"))
y= input("Enter the country you want to migrate to:")



def calculation(x,y):

    if (x== "UK"):
        s= y*0.88
        
    elif (x== "Canada"):
        s=y*1.47
        
    elif (x=="Cambodia"):
        s=y*4434
    elif (x=="USA"):
        s=y*1.09
    else:
        print("invalid")
            
    return s
            
def salary(x,y,s):
    if (x=="UK" and s>35423):
            print("You'll be rich in UK with",s, "salary.")
    else:
            print("You'll be rich in UK with",s, "salary.")
        
    if (x=="USA" and s>56516):
            print("You'll be rich in USA with",s, "salary.")
    else:
            print("You'll be rich in USA with",s, "salary.")
        
    if(x=="Cambodia" and s>5649856):
            print("You'll be rich in Cambodia with",s, "salary.")
    else:
            print("You'll be rich in Cambodia with",s, "salary.")
        
            
    if (x=="Canada" and s>64000):
            print("You'll be rich in Canada with",s, "salary.")
    else:
            print("You'll be rich in Canada with",s, "salary.")
            
calculation(x,y)
s = salary(x,y)
        
        

        
        
        
        
        
        
            
            