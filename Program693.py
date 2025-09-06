class Arithmatic:
    def __init__(self,A = 0,B = 0):  
        self.No1 = A
        self.No2 = B

    def Display(self):
        print("Value of No1 is : ",self.No1)    
        print("Value of No2 is : ",self.No2)  

    def Addition(self):
        return self.No1 + self.No2 
         
    def Subtraction(self):
        return self.No1 - self.No2      

def main():
    print("Inside main")
    
    obj1 = Arithmatic(11,10)
    
    iRet = obj1.Addition()
    print(f"Addition is : {iRet}")

    iRet = obj1.Subtraction()
    print(f"Subtraction is : {iRet}")
    

if __name__ == "__main__":
    main()    