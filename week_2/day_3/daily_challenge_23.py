""" Daily Challenge - Circle

Instructions
The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
The user can query the circle for either its radius or diameter. """

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, new):
        self.radius = new / 2
        return new

    
    @property
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def __str__(self):
        return f"The radius of the circle is {self.radius}"
    
    def __add__(self, other):
        new = Circle(self.radius + other.radius)
        return new
    
    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

c1 = Circle(10)
c2 = Circle(30)
c3 = Circle(1)

print(c3)

c2.diameter = 10
print(c2.radius)

print(c1.__gt__(c2))
print(c1.__eq__(c3))
print(c1.__lt__(c2))

circles = [c1, c2, c3]
circles_sorted = sorted(circles)
for c in circles_sorted:
    print(c)


    

