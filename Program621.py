def Display(No):
    
    for i in range(1,No+1):
        print("*",end="\t")
    

def main():

    print("Enter number : ")
    value = int(input())
    Display(value)
   
if __name__ == "__main__":
    main()