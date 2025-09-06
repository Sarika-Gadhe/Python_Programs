def CheckEvenOdd(No):
    if(No % 2 == 0):
        return True
    else:
        return False


def main():
    print("Enter number : ")
    Value = int(input())
   
    bRet = CheckEvenOdd(Value)

    if(bRet == True):
        print(f"{Value} number is Even")
    else:
        print(f"{Value} number is Odd")    


if __name__ == "__main__":
    main()