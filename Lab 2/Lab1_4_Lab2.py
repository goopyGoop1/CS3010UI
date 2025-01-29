#CS3010 Lab 1 Chad Norris-White
import os.path
import random
class Car:
    def __init__(self, brand=" ", make=" ", HP=0, CC=0):
        self.brand = brand
        self.make = make
        self.HP = HP
        self.CC = CC

    # Getters
    def get_brand(self):
        return self.brand

    def get_make(self):
        return self.make

    def get_HP(self):
        return self.HP

    def get_CC(self):
        return self.CC

    # Setters
    def set_brand(self, brand):
        self.brand = brand

    def set_make(self, make):
        self.make = make

    def set_HP(self, HP):
        self.HP = HP

    def set_CC(self, CC):
        self.CC = CC

    # Get details
    def get_details(self):
        return f"{self.brand} - {self.make}\n{self.HP}HP ({self.CC}cc)"


class Garage:

    plates1 = []

    def __init__(self):
        self.stored = []  # List to store Car objects
        self.plates1 = ['abc123', 'def456', 'hij789', 'klm987', 
                        'nop654', 'qrs321', 'tuv258', 'wxy941']
        
    def load_cars(self, filename):
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Extract car details from the line
                    parts = line.split(", ")
                    brand = parts[0].split(": ")[1]
                    make = parts[1].split(": ")[1]
                    horsepower = int(parts[2].split(": ")[1])
                    cc = int(parts[3].split(": ")[1])

                    # Create a Car object and add to the list
                    car = Car(brand, make, horsepower, cc)
                    self.stored.append(car)

    def make_register(self):
        register = {}
        plates  =self.plates1.copy()

        for car in self.stored:
            if not plates:
                print("No plates available")
                break
            
            pick_plate = random.choice(plates)
            plates.remove(pick_plate)    

            register[pick_plate] = car

        return register   

    def list_all(self):
        print("Listing all cars in the garage:")
        for car in self.stored:
            print(car.get_details())

    def cars_with_cc_above(self, threshold):
        return [car for car in self.stored if car.get_CC() > threshold]


def main():
    # Create a Garage object
    garage = Garage()

    # Load cars from file
    garage.load_cars("cars.txt")

    # List all cars
    register = garage.make_register()

    # Filter and display cars with CC > 800
    print("\nRegister of Cars:")
    for plate, car in register.items():
        print(f"{plate}: {car.get_details()}")


if __name__ == "__main__":
    main()
