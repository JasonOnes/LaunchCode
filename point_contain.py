class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
        
class Rectangle(object):
    def __init__(self, low_left, width, length):
        self.low_left = low_left
        self.width = width
        self.length = length
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.length
    
    def __str__(self):
        return ("This is a {} by {} rectangle.".format(self.width, self.length))
        
    def area(self):
        area = self.width * self.length
        return area

    def contains(self, point):
        # if point.getX() < self.width and point.getY() < self.length:
        #     if point.getX() >= self.low_left.getX() and point.getY() >= self.low_left.getY():
        #         return True
        # else:
        #     return False
       x_low = self.low_left.getX()
       x_high = self.low_left.getX() + self.getWidth()
       y_low = self.low_left.getY()
       y_high = self.low_left.getY() + self.getHeight()
       print(x_low, x_high)
       print(y_low, y_high)
       if point.getX() >= x_low and point.getX() < x_high:
           if point.getY() >= y_low and point.getY() < y_high:
               return True
           else:
               return False 
       else:
           return False

if __name__ == "__main__":
    r = Rectangle(Point(0, 0), 10, 5)
    print(r)
    #print(r.contains(Point(-3, -3)))
    #print(r.low_left.getX())
    #print(r.low_left.getY())
    h = Point(3, 7)
    print(h.getX())
    print(h.getY())
    #print(r.x_low())
    print(r.contains(h))