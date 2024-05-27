# car.py
# car.py
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, weight, wheel_size, wheel_number):
        super().__init__(make, model, year, weight)
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
        self.is_driving = False

    def drive(self):
        self.is_driving = True

    def stop(self):
        if self.is_driving:
            self.is_driving = False
            self.trips_since_maintenance += 1
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

    def fill_up_tank(self):
        return "filling up!"

