from datetime import datetime
    #  Truck class with attributes required for tracking during deliveries

class Truck:
    def __init__(self, load_capacity, mileage, speed, packages, location, departure_offset, ID):
        self.load_capacity = load_capacity
        self.mileage = mileage
        self.speed = speed
        self.packages = packages
        self.location = location
        self.departure_time = datetime(2024, 6, 1, 8, 0, 0) + departure_offset
        self.ID = ID

    def __repr__(self):
        return (
            f"Load Capacity: {self.load_capacity}, "
            f"Mileage: {self.mileage}, "
            f"Speed: {self.speed}, "
            f"Packages: {self.packages}, "
            f"Location: {self.location}, "
            f"Delivery Time: {self.delivery_time}, "
            f"Departure Time: {self.departure_time}, "
        )