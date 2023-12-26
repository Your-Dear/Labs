class Car:
    def __init__(self, tank_capacity, fuel_consumption, average_speed):
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.average_speed = average_speed

    def calculate_distance(self):
        return self.tank_capacity / self.fuel_consumption

    def fuel_ratio(self, cargo_weight=None, passengers_count=None):
        if cargo_weight is not None and passengers_count is not None:
            return (cargo_weight + passengers_count) / (self.calculate_distance() / 250)
        else:
            return None
    
    def __add__(self, other):
        if isinstance(other, Car):
            combined_tank_capacity = self.tank_capacity + other.tank_capacity
            combined_fuel_consumption = (self.fuel_consumption + other.fuel_consumption) / 2
            combined_average_speed = (self.average_speed + other.average_speed) / 2

            return Car(combined_tank_capacity, combined_fuel_consumption, combined_average_speed)
        else:
            raise TypeError("Unsupported operand type. Can only add Car instances.")


class Truck(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, cargo_capacity):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.cargo_capacity = cargo_capacity

    def additional_method(self):
        pass


class Bus(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, passenger_capacity):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.passenger_capacity = passenger_capacity

    def additional_method(self):
        pass


# Пример использования
car = Car(tank_capacity=60, fuel_consumption=10, average_speed=80)
print(f"Distance: {car.calculate_distance()} km")
print(f"Fuel ratio: {car.fuel_ratio(500, 10)}")

truck = Truck(tank_capacity=150, fuel_consumption=15, average_speed=60, cargo_capacity=5000)
print(f"Truck distance: {truck.calculate_distance()} km")
print(f"Truck fuel ratio: {truck.fuel_ratio(3000, 1)}")

bus = Bus(tank_capacity=100, fuel_consumption=12, average_speed=70, passenger_capacity=30)
print(f"Bus distance: {bus.calculate_distance()} km")
print(f"Bus fuel ratio: {bus.fuel_ratio(passengers_count=20)}")


# Пример использования перегруженного оператора сложения
car1 = Car(tank_capacity=60, fuel_consumption=10, average_speed=80)
car2 = Car(tank_capacity=70, fuel_consumption=12, average_speed=75)

new_car = car1 + car2
print(f"New Car: Tank Capacity - {new_car.tank_capacity}, Fuel Consumption - {new_car.fuel_consumption}, Average Speed - {new_car.average_speed}")
