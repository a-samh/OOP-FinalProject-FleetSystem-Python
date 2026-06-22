from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

class Car(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float):
        super().__init__(plate_number, brand, year, base_daily_rate)

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * 1.15

    def get_vehicle_type(self) -> str:
        return "Car"

    def perform_maintenance(self) -> None:
        print("\nCar maintenance is starting...")
        print("Engine Oil -> checked!")
        print("Battery -> checked!")
        print("Air Filter -> checked!")
        print("Tire Pressure -> adjusted!")
        print("Lights and Signals -> checked!")
        print("Brakes -> checked!")
        print("The car has been serviced and is fully ready!")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f"{self.get_vehicle_type()} Reserved Successfully!")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"The Car Returned after {actual_days} days, Successfully!")

    def calculate_insurance_premium(self) -> float:
        return self.calculate_daily_cost() * 0.5

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2010

