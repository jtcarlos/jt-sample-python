""" Main file for using the 'mathlib' module """
from mathlib import physics

OBJECT_MASS = 9.13
OBJECT_VELOCITY = 2.26

KINETIC_ENERGY = physics.get_kinetic_energy(OBJECT_MASS, OBJECT_VELOCITY)

if __name__ == "__main__":
    print(f"Mass: {OBJECT_MASS}")
    print(f"Velocty: {OBJECT_VELOCITY}")
    print(f"Kinetic Energy: {KINETIC_ENERGY}")
