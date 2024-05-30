
# Package class with package attributes

class Package: 
    def __init__(self, ID='', address='', city='', state='', zip_code='', delivery_time='', weight='', date='', status=''):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_time = delivery_time
        self.weight = weight
        self.date = date
        self.status = status

    #  Provides a clear and readable string for debugging
    #  includes all attributes from Package object

    def __repr__(self):
        return (
            f"Package ID: {self.ID}, "
            f"Address: {self.address}, "
            f"City: {self.city}, "
            f"State: {self.state}, "
            f"Zip: {self.zip_code}, "
            f"Delivery Time: {self.delivery_time}, "
            f"Weight: {self.weight}, "
            f"Status: {self.status}, "
        )
