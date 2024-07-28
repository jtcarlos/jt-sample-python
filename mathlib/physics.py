""" Module for basic physics computation """

def get_speed(distance, time):
    """ Computes the speed given the distance and time """
    return round(distance / time, 2)

def get_acceleration(initial, final, time):
    """ Computes the acceleration given the initial velocity, last velocity and time taken """
    return round((final - initial) / time, 2)

def get_density(mass, volume):
    """ Computes the densitiy given the mass and volume """
    return round(mass / volume, 2)

def get_kinetic_energy(mass, velocity):
    """ Computes the kinetic energy given the object's mass and velocity """
    return round(0.5 * (mass * (velocity ** 2)), 2)
