def CheckEven(No):
    if((No % 2)==0):
        return True
    
    else:
        return False
    
no = int(input("Enter number : "))    
ret = CheckEven(no)

if ret == True:
    print("Number is even")

else:
    print("Number is odd")    
    


       