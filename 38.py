class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self,head):
        self.head=head                     
    def insertbegin(self,node):                           
        node.next=self.head
        self.head=node
        print(node.data,"inserted succesfully at the beginning")
    def insertatpos(self,node,pos):
        if pos==1:
            node.next=self.head.next
            self.head=node
        else:
            prev=self.head
            for i in range(1,pos-1):
                prev=prev.next
            node.next=prev.next              
            prev.next=node
        print(node.data,"inserted succesfully at %d position"%(pos))
    def insertatend(self,node):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=node
        print(node.data,"is inserted succesfully at the end")
    def display(self):
        temp=self.head
        if temp.data is None:
            print("list is empty")
        else:
            while temp.next is not None:
                print(temp.data,"-->",end=" ")
                temp=temp.next
            print(temp.data)
               
n1=node(20)
l1=linkedlist(n1)
l1.insertbegin(node(10))
l1.insertatpos(node(5),2)
l1.insertbegin(node(30))
l1.insertatend(node(40))
l1.display()
l1.insertatpos(node(22),1)
l1.display()
l1.insertatpos(node(21),3)
l1.display()
l1.insertatpos(node(55),5)
l1.insertatpos(node(25),1)
l1.display()


