from enum import Enum
from abc import ABC, abstractmethod


class VehicleSize(Enum):
    Large = 1
    Compact = 2
    Motorcycle = 3


class Vehicle(ABC):
    def __init__(self):
        """
        Vehicle constructor.
        """
        self.parking_spots = []
        self.license_plate = None
        self.spots_needed = 0
        self.size = None

    def park_in_spot(self, spot):
        """
        Park vehicle in this spot (among others, potentially).
        """
        self.parking_spots.append(spot)

    def clear_spots(self):
        """
        Remove car from spot, and notify spot that it's gone.
        """
        pass

    @abstractmethod
    def can_fit_in_spot(self) -> bool:
        """
        Checks if the spot is big enough for the vehicle (and is available).
        This compares the SIZE only. It does not check if it has enough spots.
        """
        pass


class Bus(Vehicle):
    def __init__(self):
        """
        Bus constructor.
        """
        super().__init__()
        self.spots_needed = 5
        self.size = VehicleSize.Large

    def can_fit_in_spot(self, spot) -> bool:
        """
        Checks if the spot is a Large. Doesn't check num of spots.
        """
        pass


class Car(Vehicle):
    def __init__(self):
        """
        Car constructor.
        """
        super().__init__()
        self.spots_needed = 1
        self.size = VehicleSize.Compact

    def can_fit_in_spot(self, spot) -> bool:
        """
        Checks if the spot is a Compact or Large.
        """
        pass


class Motorcycle(Vehicle):
    def __init__(self):
        """
        Motorcycle constructor.
        """
        super().__init__()
        self.spots_needed = 1
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self, spot) -> bool:
        """
        Checks if the spot is a Compact or Large.
        """
        pass


class ParkingLot:
    def __init__(self):
        """
        Parking Lot constructor.
        """
        self.levels = []
        self.NUM_LEVELS = 5

    def park_vehicle(self):
        """
        Park the vehicle in a spot (or multiple spots). Return false if failed.
        """
        pass


class Level:
    def __init__(self, flr: int, number_spots: int):
        """
        Level constructor.
        """
        self.floor = flr
        self.spots = []
        self.available_spots = 0  # number of free spots
        self.SPOTS_PER_ROW = 10

    def park_vehicle(self, v: Vehicle) -> bool:
        """
        Find a place to park this vehicle. Return false if failed.
        """
        pass

    def park_starting_at_spot(self, v: Vehicle) -> bool:
        """
        Park a vehicle starting at the spot spot_number and continuing until
        spots_needed.
        """
        pass

    def find_available_spots(self, v: Vehicle) -> int:
        """
        Find a spot to park this vehicle. Return index of spot, or -1 on
        failure.
        """
        pass

    def spot_freed(self):
        """
        When a car was removed from the spot, increment available_spots.
        """
        pass


class ParkingSpot:
    def __init__(self, lvl: Level, r: int, n: int, s: VehicleSize):
        """
        Parking Spot constructor.
        """
        self.level = lvl
        self.row = r
        self.spot_number = n
        self.spot_size = s
        self.vehicle = None

    def is_available(self) -> bool:
        """
        Determines if parking spot is available for a car to park.
        """
        return self.vehicle == None

    def can_fit_vehicle(self, v: Vehicle) -> bool:
        """
        Check if the spot is big enough and is available.
        """
        pass

    def park(self, v: Vehicle):
        """
        Park vehicle in this spot.
        """
        pass

    def remove_vehicle(self):
        """
        Remove vehicle from this spot.
        """
        pass
