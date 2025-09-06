def CountEvenOdd(Brr):

  iEven = 0

  for no in Brr:
   if(no % 2 == 0):
     iEven += 1
    

  return iEven, len(Brr)-iEven

def main():
  print("Enter the number of elements : ")
  iLength =  int(input())

  Arr = []

  print("please Enter the elements : ")

  for i in range(1,iLength+1):
    no = int(input())
    Arr.append(no)

  ERet,ORet = CountEvenOdd(Arr)
  print(f"Total Even elements is  : {ERet} and Total Odd elements is : {ORet}")   


if __name__ == "__main__":
  main()    