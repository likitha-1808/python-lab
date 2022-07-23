even_set={2,4,6,8}
odd_set={1,3,5,7,9}
print (odd_set.union(even_set))
s1=set([1,1,1,2,3,3,3])
s1.add(4)
s1.add("hello")
s1.add(-10)
s1.update(odd_set)
print(s1)
s1.remove('hello')
print(s1)
s1.discard(-10)
print(s1)
s1.issuperset(even_set)
