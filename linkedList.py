class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.nodeCount=0

    def insertLast(self,value):
        newnode = Node(value)
        if self.head==None:
            self.head = newnode
            self.nodeCount+=1
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = newnode
            self.nodeCount+=1
    def insertFirst(self,value):
        newnode = Node(value)
        if self.head==None:
            self.head=newnode
            self.nodeCount+=1
        else:
            newnode.next = self.head
            self.head = newnode
            self.nodeCount+=1
    def displayList(self):
        if(self.head==None):
            print("List is empty!")
        else:
            temp = self.head
            while(temp!=None):
                print(temp.value,end="->")
                temp = temp.next
            print("X")
    def deleteFirst(self):
        if self.head==None:
            print("List is empty!")
        else:
            self.head = self.head.next
            self.nodeCount-=1
    def deleteLast(self):
        if self.head == None:
            print("List is empty!")
        elif self.head.next==None:
            self.head=None
            self.nodeCount-=1
        else:
            temp = self.head
            while(temp.next.next!=None):
                temp = temp.next
            temp.next = None
            self.nodeCount-=1
    def searchelement(self,element):
        if self.head == None:
            print("list is empty!")
        else:
            temp = self.head
            while temp!=None:
                if temp.value==element:
                    print("element is present in list!")
                    break
                temp = temp.next
            if temp==None:
                print("element is not present in linkedlist!")

if __name__=="__main__":
   mylist = LinkedList()
   print("inserting at last!")
   mylist.insertLast(10)
   mylist.displayList()
   print("delete last!")
   mylist.deleteLast()
   mylist.displayList()
   print("insert last!")
   mylist.insertLast(20)
   mylist.insertLast(30)
   mylist.displayList()
   print("delete Last!")
   mylist.deleteLast()
   mylist.displayList()
   print("inserting at first position!")
   mylist.insertFirst(9)
   mylist.insertFirst(8)
   mylist.insertFirst(7)
   mylist.displayList()
   print("deleting first node!")
   mylist.deleteFirst()
   mylist.displayList()
   print("deleting first node again!")
   mylist.deleteFirst()
   mylist.displayList()
   print("search for element 20 in linked-list")
   mylist.searchelement(20)
   print("search for element which is not present in linked-list")
   mylist.searchelement(40)
   print("node count: ",mylist.nodeCount)
