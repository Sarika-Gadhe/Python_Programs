def Display(No):
   
    i = 1

    while(i <= No):
        print("*")
        i = i + 1
    

def main():

    print("Enter number : ")
    value = int(input())
    Display(value)
   
if __name__ == "__main__":
    main()