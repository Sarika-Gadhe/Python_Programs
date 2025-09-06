def Addition(No):
    
    iSum = 0
    for i in range(1,No+1):
        iSum = iSum + i

    return iSum

def main():

    print("Enter number : ")
    value = int(input())
    iRet =  Addition(value)

    print(f"Addition is : {iRet}")
   
if __name__ == "__main__":
    main()