class Node:
    def __init__(self,No):
        self.data = No
        self.next = None

class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

    #8
########################################################################################## 
    
    def InsertFirst(self,No):
        newn = Node(No)

        if(self.first == None):  # LL is Empty
            self.first = newn

        else:              # LL contains  at least 1 node
            newn.next = self.first
            self.first = newn

        self.iCount = self.iCount +1    


########################################################################################## 

    def Display(self):
        pass
########################################################################################## 
    
    def Count(self):
        return self.iCount


########################################################################################## 

def main():
    print("Demonstration of Singly Linear Linked List")

    sobj = SinglyLL()

    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    iRet = sobj.Count()

    print(f"Number of Nodes in Linked List are : {iRet}")
    

if __name__ == "__main__":
    main()    