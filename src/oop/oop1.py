# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # Base class
    pass

class FlightVehicle(Vehicle):
    # inherits from the Vehicle class
    pass

class Starship(FlightVehicle):
    # inherits from the FlightVehicle class
    pass

class Airplane(FlightVehicle):
    # inherits from the FlightVehicle class
    pass



class GroundVehicle(Vehicle):
    # inherits from the Vehicle class
    pass

class Car(GroundVehicle):
    # inherits from the GroundVehicle class
    pass

class Motorcycle(GroundVehicle):
     # inherits from the GroundVehicle class
    pass

