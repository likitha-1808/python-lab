class Rectangle:
    length=int(input("enter length"))
    breadth=int(input("enter breadth"))
    def area(self):
        area=self.length*self.breadth
        print(area)
r=Rectangle()
r.area()