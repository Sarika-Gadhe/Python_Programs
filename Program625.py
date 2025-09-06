#Input : 721
# 1  2  7

def SumDigits(No):
    
    iDigit = 0
    iSum = 0

    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10
    return iSum  
    
   

def main():

    print("Enter number : ")
    value = int(input())
    iRet = SumDigits(value)

    print(f"Addition of digit is {iRet}")
   
if __name__ == "__main__":
    main()