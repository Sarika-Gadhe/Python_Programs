
def Replace(data):
  
  iCount = 0
  
  output = ""         #empty string
  for ch in data:
    if(ch == 'a'):
      output.append('_')        # Error
    else:
      output.append(ch)          
  
  return output
      
  
  
def main():
  print("Enter String : ")
  str = input()

  strX = Replace(str)

  print(f"Updated String is {strX}")
  




if __name__ == "__main__":
  main()    

