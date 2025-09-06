def CheckDivisible(No):
    if((No % 3 == 0) and ((No % 5 == 0))):
        return True
    else:
        return False


def main():
    print("Enter number : ")
    Value = int(input())
   
    bRet = CheckDivisible(Value)

    if(bRet == True):
        print(f"{Value} number is Divisible by 3 and 5")
    else:
        print(f"{Value} number is not Divisible by 3 and (or) 5")    


if __name__ == "__main__":
    main()