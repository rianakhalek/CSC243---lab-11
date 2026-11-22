from Point import Point


class Rectangle:
    def __init__(self, p, q):
        assert isinstance(p, Point) and isinstance(q, Point) and p.x <= q.x and p.y <= q.y, "Bad input!"
        self.p = p
        self.q = q

    def __str__(self):
        return f"(p=({self.p.x}, {self.p.y}), q=({self.q.x}, {self.q.y}))"

    def get_width(self):
        return self.q.x - self.p.x

    def get_height(self):
        return self.q.y - self.p.y

    def area(self):
        return self.get_width() * self.get_height()

    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())

    def contains(self, pt):
        assert isinstance(pt, Point), "Bad Input!"
        return (self.p.x <= pt.x <= self.q.x) and (self.p.y <= pt.y <= self.q.y)