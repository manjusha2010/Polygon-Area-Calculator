class Rectangle():
        def __init__(self,width,height):
                self.wid=width
                self.hei=height
        def __str__(self):
                return "Rectangle(width="+str(self.wid)+", height="+str(self.hei)+")"
        def set_width(self,a):
                self.wid=a
        def set_height(self,b):
                self.hei=b
        def get_area(self):
                return self.wid*self.hei
        def get_perimeter(self):
                return 2*(self.wid+self.hei)
        def get_diagonal(self):
                return ((self.wid**2)+(self.hei**2))**0.5
        def get_picture(self):
                if self.hei>50 or self.wid>50:
                        return "Too big for picture"
                else:
                        for i in range(self.hei):
                                for j in range(self.wid):
                                        print("*",end="")
                                print()
                        return ""
        def get_amount_inside(self,arg):
                p=Rectangle.get_area(self)
                q=arg.get_area()
                return p//q
class Square(Rectangle):
        def __init__(self,side):
                self.wid=side
                self.hei=side
        def __str__(self):
                return "Square(side="+str(self.wid)+")"
        def set_side(self,s):
                self.wid=s
                self.hei=s
r=Rectangle(10,5)
print(r.get_area())
r.set_height(3)
print(r.get_perimeter())
print(r)
print(r.get_picture())
sq=Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

r.set_height(8)
r.set_width(16)
print(r.get_amount_inside(sq))
        
                
