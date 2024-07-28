""" Main file for using the 'mathlib' module """
from mathlib import physics

OBJECT_MASS = 9.13
OBJECT_VELOCITY = 2.26

KINETIC_ENERGY = physics.get_kinetic_energy(OBJECT_MASS, OBJECT_VELOCITY)

if __name__ == "__main__":
    print(f"The kinetic energy of a {OBJECT_MASS}kg item going at a velocity of {OBJECT_VELOCITY}m/s is {KINETIC_ENERGY}J")
