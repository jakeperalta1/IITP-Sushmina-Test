
    
y= float(input("Please enter your salary in Germany:"))
x= input("Enter the country you want to migrate to:")



def calculation(x,y):
    s = 0
    if (x== "UK"):
        s= y*0.88
        
    elif (x== "Canada"):
        s=y*1.47
        
    elif (x=="Cambodia"):
        s=y*4434
    elif (x=="USA"):
        s=y*1.09
    else:
        print("invalid country: {}".format(x))
            
    return s
            
def salary(x,y, s):
    if x=="UK" :
        if (s>64000):
            print("You'll be rich in UK with",s, "salary.")
        else:
            print("You'll be poor in UK with",s, "salary.")
        
    if x=="USA" :
        if (s>64000):
            print("You'll be rich in USA with",s, "salary.")
        else:
            print("You'll be poor in USA with",s, "salary.")
    
    if x == "Cambodia":
        if(s>5649856):
                print("You'll be rich in Cambodia with",s, "salary.")
        else:
                print("You'll be poor in Cambodia with",s, "salary.")
        
            
    if x=="Canada" :
        if(s>64000):
            print("You'll be rich in Canada with",s, "salary.")
        else:
            print("You'll be poor in Canada with",s, "salary.")
            
s =calculation(x,y)
salary(x,y, s)
        
        

        
        
        
        
        
        
            
            