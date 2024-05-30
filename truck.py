
    #  Truck class with attributes required for tracking during deliveries

class Truck:
    def __init__(self, load_capacity, mileage, speed, packages, location, delivery_time, departure_time):
        self.load_capacity = load_capacity
        self.mileage = mileage
        self.speed = speed
        self.packages = packages
        self.location = location
        self.delivery_time = delivery_time
        self.departure_time = departure_time

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