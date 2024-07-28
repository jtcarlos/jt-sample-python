""" Unit test file for package 'mathlib' """
import unittest

from mathlib import basic
from mathlib import physics

class MathlibUnitTest(unittest.TestCase):
    """ Unit test class for package 'mathlib' """

    # Unit tests for module 'basic'
    def test_addition(self):
        """ Unit test 'basic.add' functionality """
        self.assertEqual(basic.add(1, 2), 3)
        self.assertEqual(basic.add(-10, 5), -5)
        self.assertEqual(basic.add(201.2, 82.3), 283.5)

    def test_subtraction(self):
        """ Unit test 'basic.subtract' functionality """
        self.assertEqual(basic.subtract(10, 5), 5)
        self.assertEqual(basic.subtract(-10, -5), -5)
        self.assertEqual(basic.subtract(32, 10.5), 21.5)

    def test_multiplication(self):
        """ Unit test 'basic.multiplication' functionality """
        self.assertEqual(basic.multiply(3, 3), 9)
        self.assertEqual(basic.multiply(2.5, 2), 5.0)
        self.assertEqual(basic.multiply(10, -3), -30)

    def test_division(self):
        """ Unit test 'basic.division' functionality """
        self.assertEqual(basic.divide(3, 3), 1)
        self.assertEqual(basic.divide(10, 0), None)
        self.assertEqual(basic.divide(90, -10), -9)

    def test_mean(self):
        """ Unit test 'basic.mean' functionality """
        self.assertEqual(basic.mean([3, 3, 3]), 3.0)
        self.assertEqual(basic.mean([10, 5, 5]), 6.67)
        self.assertEqual(basic.mean([21, -10, 5.3]), 5.43)

    # Unit tests for module 'physics'
    def test_get_speed(self):
        """ Unit test 'physics.get_speed' functionality """
        self.assertEqual(physics.get_speed(6, 2), 3)
        self.assertEqual(physics.get_speed(10, 5), 2)
        self.assertEqual(physics.get_speed(50, 10), 5)

    def test_get_acceleration(self):
        """ Unit test 'physics.get_acceleration' functionality """
        self.assertEqual(physics.get_acceleration(10, 20, 5), 2)
        self.assertEqual(physics.get_acceleration(32, 21, 1), -11)
        self.assertEqual(physics.get_acceleration(10, 100, 5.2), 17.31)

    def test_get_density(self):
        """ Unit test 'physics.get_density' functionality """
        self.assertEqual(physics.get_density(8900, 1), 8900)
        self.assertEqual(physics.get_density(12.5, 5.7), 2.19)
        self.assertEqual(physics.get_density(231, 52), 4.44)

    def test_get_kinetic_energy(self):
        """ Unit test 'physics.get_kinetic_energy' functionality """
        self.assertEqual(physics.get_kinetic_energy(12, 3), 54)
        self.assertEqual(physics.get_kinetic_energy(13.17, 26.3), 4554.78)
        self.assertEqual(physics.get_kinetic_energy(3, 20), 600)


# Run the unit test
if __name__ == "__main__":
    unittest.main() 
