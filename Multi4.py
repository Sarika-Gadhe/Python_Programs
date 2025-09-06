import threading

def Display():
    print("Inside Display")
        

def main():
    print("Inside main")
    T1 = threading.Thread(target=Display)                #display callback function
    T1.start()


if __name__ == "__main__":
    main()    