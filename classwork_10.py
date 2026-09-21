from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self):
        return 2025 - self.joining_year

    @abstractmethod
    def get_role(self):
        pass

    def show_details(self):
        print(f"Name: {self.name}, Role: {self.get_role()}, "
              f"Years on platform: {self.years_on_platform()}")


class Customer(User):
    def get_role(self):
        return "Customer"


class Vendor(User):
    def get_role(self):
        return "Vendor"


customer = Customer("Rahul", 2020)
vendor = Vendor("Priya", 2018)

customer.show_details()
vendor.show_details()