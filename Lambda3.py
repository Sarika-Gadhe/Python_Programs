def CheckEven(No):
    return (No % 2 == 0)
    
no = int(input("Enter number : "))    
ret = CheckEven(no)

if ret == True:
    print("Number is even")

else:
    print("Number is odd")    
    


       