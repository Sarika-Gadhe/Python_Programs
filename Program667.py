def StrUpr(data):

  i = 0
  output = ""

  for ch in data:
    if(ch >= 'a' and ch <='z'):
      output = output+ chr(ord(ch)-32)        #for ascii - ord 
    else:
      output = output + ch         
  
  return output
  
      
  
  
def main():
  print("Enter String : ")
  str = input()
  
  iRet = StrUpr(str)

  print(f"Updated String in {str} is : {iRet}")
  




if __name__ == "__main__":
  main()    

