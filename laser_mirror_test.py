from laser_mirror import Position
import laser_mirror
import unittest
import numpy

class laser_mirror_test(unittest.TestCase):
    def test_distance(self):
        position1 = Position(0, 0)
        position2 = Position(0, 0)
        self.assertEqual(laser_mirror.distance(position1, position2), 0)
        
        position1 = Position(0, 0)
        position2 = Position(10, 0)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(0, 0)
        position2 = Position(0, 10)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(1, 0)
        position2 = Position(0, 1)
        self.assertAlmostEqual(laser_mirror.distance(position1, position2), numpy.sqrt(2))

        position1 = Position(0, 0)
        position2 = Position(-10, 0)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(0, 0)
        position2 = Position(0, -10)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(-5, 0)
        position2 = Position(5, 0)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(0, -5)
        position2 = Position(0, 5)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(5, 0)
        position2 = Position(-5, 0)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(0, 5)
        position2 = Position(0, -5)
        self.assertEqual(laser_mirror.distance(position1, position2), 10)

        position1 = Position(0, 3)
        position2 = Position(4, 0)
        self.assertEqual(laser_mirror.distance(position1, position2), 5)

        position1 = Position(3, 0)
        position2 = Position(0, 4)
        self.assertEqual(laser_mirror.distance(position1, position2), 5)
    
    def test_find_quarter(self):
        position1 = Position(10, 10)
        position2 = Position(10, 10)
        self.assertEqual(laser_mirror.find_quarter(position1, position2), 0)

        position2 = Position(11, 9)
        self.assertEqual(laser_mirror.find_quarter(position1, position2), 0)

        position2 = Position(9, 9)
        self.assertEqual(laser_mirror.find_quarter(position1, position2), 270)

        position2 = Position(9, 11)
        self.assertEqual(laser_mirror.find_quarter(position1, position2), 180)

        position2 = Position(11, 11)
        self.assertEqual(laser_mirror.find_quarter(position1, position2), 90)
    
    def test_angle_between_points(self):
        position1 = Position(10, 10)
        position2 = Position(15, 10)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 90)

        position1 = Position(10, 10)
        position2 = Position(5, 10)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 270)

        position1 = Position(10, 10)
        position2 = Position(10, 15)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 180)

        position1 = Position(10, 10)
        position2 = Position(10, 5)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 0)

        position1 = Position(10, 10)
        position2 = Position(11, 11)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 135)

        position1 = Position(0, 0)
        position2 = Position(0, 2)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 180)

        position1 = Position(0, 0)
        position2 = Position(2, 0)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 90)

        position1 = Position(2, 0)
        position2 = Position(2, 2)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 180)

        position1 = Position(2, 0)
        position2 = Position(0, 0)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 270)
        
        position1 = Position(2, 2)
        position2 = Position(2, 0)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 0)
        
        position1 = Position(2, 2)
        position2 = Position(0, 2)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 270)
        
        position1 = Position(0, 2)
        position2 = Position(0, 0)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 0)
        
        position1 = Position(0, 2)
        position2 = Position(2, 2)
        self.assertEqual(laser_mirror.angle_between_points(position1, position2), 90)
    
    def test_one_sided_mirror_angle(self):
        position1 = Position(2, 0)
        position2 = Position(0, 0)
        position3 = Position(0, 2)
        self.assertEqual(laser_mirror.one_sided_mirror_angle(position1, position2, position3), 135)
        
        position1 = Position(0, 0)
        position2 = Position(2, 0)
        position3 = Position(2, 2)
        self.assertEqual(laser_mirror.one_sided_mirror_angle(position1, position2, position3), 225)
        
        position1 = Position(0, 2)
        position2 = Position(2, 2)
        position3 = Position(2, 0)
        self.assertEqual(laser_mirror.one_sided_mirror_angle(position1, position2, position3), 315)
        
        position1 = Position(2, 2)
        position2 = Position(0, 2)
        position3 = Position(0, 0)
        self.assertEqual(laser_mirror.one_sided_mirror_angle(position1, position2, position3), 45)


if __name__ == '__main__':
    unittest.main()