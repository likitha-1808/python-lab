class circle:
    def area(self,r):
        print("area is",22/7*r*r)
    def perimeter(self,r):
        print("perimeter is",2*22/7*r)
c=circle()
r=int(input("enter radius"))
c.area(r)
c.perimeter(r)
