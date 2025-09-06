no = 11                     #global

def fun():
    print("Inside  fun")
    x = 21                   #local
    print("Value of x is :",x)             #21
    print("Value of no is :",no)           #11

def sun():
    print("Inside sun")
    y = 51
    print("Value of y is:",y)             #51
    print("Value of no is :",no)            #11

def main():
    fun()
    sun()


if __name__=="__main__":
    main()    

