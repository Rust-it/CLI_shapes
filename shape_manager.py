class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.next_id = 1

    def add_shape(self, shape):
        shape.id = self.next_id
        self.next_id += 1
        self.shapes.append(shape)
        return shape.id

    def delete_shape(self, shape_id):
        for i, shape in enumerate(self.shapes):
            if shape.id == shape_id:
                del self.shapes[i]
                return True
        return False
