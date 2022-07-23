mylist=list()
for k in range(14,36):
     mylist.append(k)
     print(mylist)
     for i in mylist:
         if(i%5==0):
             mylist.remove(i)
             print(mylist)
             oddlist=list()
             evenlist=list()
             for i in mylist:
                 if(i%2==0):
                     evenlist.append(i)
                     else:
                     oddlist.append(i)
                     print(evenlist)
                     print(oddlist)
                 
