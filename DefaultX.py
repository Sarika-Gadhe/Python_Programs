def CalculatePercentge(Obtained = 400, Total = 500):
    output = ((Obtained / Total)*100)
    return output

def main():
    
    result = CalculatePercentge(350,450)          # Default arguments
    print("Perecntage is :",result)
    
    result = CalculatePercentge(350)          # Default arguments
    print("Perecntage is :",result)
    
    result = CalculatePercentge()          # Default arguments
    print("Perecntage is :",result)

if __name__ == "__main__":
    main()      


    