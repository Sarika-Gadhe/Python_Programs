def Display(No):
   
    i = 1

    while(i <= No):
        print("*",end="\t")
        i = i + 1

    print("")            # % = mac os
    

def main():

    print("Enter number : ")
    value = int(input())
    Display(value)
   
if __name__ == "__main__":
    main()