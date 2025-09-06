#Input : 721
# 1  2  7

def DisplayDigits(No):
    
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        No = No // 10
        print(iDigit)
    
   

def main():

    print("Enter number : ")
    value = int(input())
    DisplayDigits(value)
   
if __name__ == "__main__":
    main()