import sys

def main():
    print("Number of commandLine arguments are :",len(sys.argv))
    print("Datatype of argv is : ",type(sys.argv))
    
    print("List of commandLine arguments are : ")
    
    for i in range(1,len(sys.argv)):
        print(sys.argv[i])



if __name__ == "__main__":
    main()    