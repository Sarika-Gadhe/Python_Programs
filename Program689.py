class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):                                  #like java - garbage collector
        print('Inside Destructor')

def main():
    print("Inside main")
    
    obj1 = Demo()
    obj2 = Demo()

    del obj1                          # del is use to delete the object implicitly
    del obj2

    print("End of main")
    
if __name__ == "__main__":
    main()    