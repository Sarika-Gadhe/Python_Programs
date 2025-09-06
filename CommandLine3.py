import sys

def main():
    print("Number of commandLine arguments are :",len(sys.argv))
    print("Datatype of argv is : ",type(sys.argv))
    
    print("List of commandLine arguments are : ")
    
    for no in sys.argv:
        print(no)



if __name__ == "__main__":
    main()    