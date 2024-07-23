import unittest
import math
from main.shapes import Circle, Triangle, Rectangle

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(Circle(1).area(), math.pi)
        self.assertAlmostEqual(Circle(0).area(), 0)
        self.assertAlmostEqual(Circle(2.5).area(), math.pi * 2.5**2)
        with self.assertRaises(ValueError):
            Circle(-1)
    
    def test_triangle_area(self):
        self.assertAlmostEqual(Triangle(3, 4, 5).area(), 6)
        self.assertAlmostEqual(Triangle(7, 10, 5).area(), 16.24807680927192)
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_triangle_is_right(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_triangle())
        self.assertFalse(Triangle(5, 5, 5).is_right_triangle())
        self.assertFalse(Triangle(7, 10, 5).is_right_triangle())

    def test_rectangle_area(self):
        self.assertAlmostEqual(Rectangle(3, 4).area(), 12)
        self.assertAlmostEqual(Rectangle(7, 5).area(), 35)
        with self.assertRaises(ValueError):
            Rectangle(-3, 4)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

if __name__ == '__main__':
    unittest.main()
