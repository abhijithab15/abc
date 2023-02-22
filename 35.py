class rectangle:
    def __init__(self,l,b):
        self.len=l
        self.bre=b
    def area(self):
        area1=self.len*self.bre
        return area1
    def __lt__(self, obj):
        if(self.area() < obj.area()):
            return "the area of rectangle 1 is less than rectangle2"
        else:
            return "the area of rectangle 2 is less than rectangle1"

print('RECTANGLE 1')
l=int(input("enter the length1"))
b=int(input("enter the breadth1"))
obj1=rectangle(l,b)
print('the area is:')
print(obj1.area())

print('RECTANGLE 2')
l=int(input("enter the length2"))
b=int(input("enter the breadth2"))
obj2=rectangle(l,b)
print('the area is:')
print(obj2.area())

print('now compare the rectangle')
print(obj1 < obj2)