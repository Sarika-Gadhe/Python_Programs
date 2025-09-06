 # input Rows :  5    col : 4

'''
  
 *  *  *  * 
 *  *  *  * 
 *  *  *  * 
 *  *  *  * 
 *  *  *  * 

'''


def Display(iRow , iCol):

  for i in range (1,iRow+1,1):      
    for j in range(1,iCol+1,1):              
      print("*",end="\t")
    print()  

  print()  


def main():
  print("Enter number of rows : ")
  iValue1 = int(input())
  
  print("Enter number of Columns : ")
  iValue2 = int(input())
  
  Display(iValue1,iValue2)

if __name__ == "__main__":
  main()    
