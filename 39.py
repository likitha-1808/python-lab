class queue:
    def __init__(self,max):
        self.q=list()
        self.max=max
    def enqueue(self,ele):
        if(len(self.q)>=self.max):
            print("queue is full")
        else:
            self.q.append(ele)
            print("\n"f"{ele} inserted succesfully")
    def dequeue(self):
        if(len(self.q)<=0):
            print("no element to delete in queue")
        else:
            ele=self.q.pop()
            print("\n"f"{ele} deleted succesfully")
    def display(self):
         if(len(self.q)<=0):
            print("queue is empty")
         else:
             for i in self.q:
                 print(i,end=' ')
q=queue(5)
q.display()
q.enqueue(25)
q.display()
q.enqueue("dairy milk")
q.display()
q.enqueue(6)
q.display()
q.dequeue()
q.display()

