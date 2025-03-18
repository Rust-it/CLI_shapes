class Shape:
    def __init__(self, shape_id):
        self.id = shape_id

    def __str__(self):
        return f"ID {self.id}: "

class Point(Shape):
    def __init__(self, shape_id, x, y):
        super().__init__(shape_id)
        self.x = x
        self.y = y

    def __str__(self):
        return super().__str__() + f"Точка ({self.x}, {self.y})"

class Line(Shape):
    def __init__(self, shape_id, x1, y1, x2, y2):
        super().__init__(shape_id)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return super().__str__() + f"Отрезок от ({self.x1}, {self.y1}) до ({self.x2}, {self.y2})"

class Circle(Shape):
    def __init__(self, shape_id, cx, cy, radius):
        super().__init__(shape_id)
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def __str__(self):
        return super().__str__() + f"Круг с центром в ({self.cx}, {self.cy}) и радиусом {self.radius}"

class Square(Shape):
    def __init__(self, shape_id, x, y, side):
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return super().__str__() + f"Квадрат в ({self.x}, {self.y}) со стороной {self.side}"
