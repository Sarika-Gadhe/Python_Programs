def CalculatePercentge(Total,Obtained):
    output = ((Obtained / Total)*100)
    return output

def main():
    print("Enter total marks :")
    value1 = int(input())

    print("Enter Obtained marks :")
    value2 = int(input())
    
    result = CalculatePercentge(value1,value2)          # positional arguments

    print("Perecntage is :",result)

if __name__ == "__main__":
    main()      


    