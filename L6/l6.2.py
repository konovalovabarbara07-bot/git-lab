class Vehicle:
    def __init__(self, make, model):
        self.make =make
        self.model = model
    def get_info(self):
        return f"Марка:{self.make}, Модель:{self.model}"
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make,model)
        self.fuel_type=fuel_type
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, тип топлива:{self.fuel_type}"
if __name__ == "__main__":
    vehicle =Vehicle("Hyundai", 'Creta')
    print(vehicle.get_info())
    car=Car("Toyota","Land Cruiser Prado","Дизель")
    print(car.get_info())
