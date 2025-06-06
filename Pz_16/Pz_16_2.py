#Создайте класс "Фигура", который содержит метод расчета площади фигуры.
#Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
#"Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area() не реализован!")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


square = Square(5)
print(f"Площадь квадрата со стороной {square.side}: {square.calculate_area()}")

rectangle = Rectangle(4, 6)
print(f"Площадь прямоугольника {rectangle.length}x{rectangle.width}: {rectangle.calculate_area()}")