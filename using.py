from main.shapes import Circle, Triangle, Rectangle

# Площадь круга радиусом 5
circle = Circle(5)
print(circle.area())

# Площадь треугольника со сторонами 3, 4 и 5
triangle = Triangle(3, 4, 5)
print(triangle.area())

# Проверка, является ли треугольник прямоугольным
print(triangle.is_right_triangle())

# Площадь прямоугольника с шириной 7 и высотой 5
rectangle = Rectangle(7, 5)
print(rectangle.area())