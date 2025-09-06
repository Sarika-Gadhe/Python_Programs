def CalculatePercentge(Obtained, Total = 500):
    output = ((Obtained / Total)*100)
    return output

def main():
        
    print("Enter Obtained marks :")
    value2 = int(input())
    
    result = CalculatePercentge(value2)          # Default arguments

    print("Perecntage is :",result)

if __name__ == "__main__":
    main()      


    