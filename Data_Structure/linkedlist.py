class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def InsertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def InsertAtFront(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def DeleteAtFront(self):
        if self.head.next is None:
            self.head=None
        else:
            temp=self.head
            self.head=temp.next
            temp=None
    def DeleteAtEnd(self):
        if self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                prev=temp
                temp=temp.next
            prev.next=None
            temp=None
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end=' '"\n")
            curr=curr.next
ll=LinkedList()
while True:
    print(" 1.InsertAtEnd\n 2.InsertAtFront\n 3.DeleteAtEnd\n 4.DeleteAtFront\n 5.Display\n 6.exit ")
    ch=int(input("Enter your choice "))
    match ch:
        case 1:ll.InsertAtEnd(int(input("Enter the number ")))
        case 2:ll.InsertAtFront(int(input("Enter the number ")))
        case 3:ll.DeleteAtEnd()
        case 4:ll.DeleteAtFront()
        case 5:ll.display()
        case 6:break                    