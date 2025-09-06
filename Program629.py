def CountDigitX(iNo):

    iDigit = 0
    iCount4 = 0
    iCount5 = 0
    iCount7 = 0

    while(iNo != 0):
        iDigit = iNo % 10
        if(iDigit == 4):
            iCount4+=1
        elif(iDigit == 5):
            iCount5+=1
        elif(iDigit == 7):
            iCount7+=1        
        iNo = iNo // 10
        
    return iCount4,iCount5,iCount7


def main():
    print("Enter number : ")
    iValue = int(input())
    
    iRet4,iRet5,iRet7 = CountDigitX(iValue)

    print(f"frequency of 4 is {iRet4} , of 5 is {iRet5}, of 7 is {iRet7}")
   

   


if __name__ == "__main__":
    main()    