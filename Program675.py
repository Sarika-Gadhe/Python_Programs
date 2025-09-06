 # input : HELLO
'''
  H  E  L  L  O
  H  E  L  L  O
  H  E  L  L  O
  H  E  L  L  O
  H  E  L  L  O

'''


def Display(Data):

  for i in range(len(Data)):      #row
    for ch in Data:              # column
      print(ch,end="\t")
    print()  

  print()  


def main():
  print("Enter String : ")
  str = input()
  
  Display(str)

if __name__ == "__main__":
  main()    
