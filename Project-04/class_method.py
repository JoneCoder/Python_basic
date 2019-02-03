class car:
    def __init__(self, name, manufacturer, color, year, power):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.release = year
        self.cc = power
        
    def default(self):
        print("Name:",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:",self.color)
        print("Release:",self.release)
        print("Engine power:",self.cc)

    def car_start(self):
        print("Name:",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:",self.color)
        print("Release:",self.release)
        print("Engine power:",self.cc)
        print("Starting the engine...")

    def brake(self):
        print("Name:",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:",self.color)
        print("Release:",self.release)
        print("Engine power:",self.cc)
        print("Car braked!")

    def drive(self):
        print("Name:",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:",self.color)
        print("Release:",self.release)
        print("Engine power:",self.cc)
        print("Driving start")

    def turn_left(self):
        print("Name:",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:",self.color)
        print("Release:",self.release)
        print("Engine power:",self.cc)
        print("Turn Left")

    def turn_right(self):
        print("Name:",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:",self.color)
        print("Release:",self.release)
        print("Engine power:",self.cc)
        print("Turn Right")

    def change_gear(self):
        print("Name:",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:",self.color)
        print("Release:",self.release)
        print("Engine power:",self.cc)
        print("Gear Changed")

if __name__ == "__main__":
    my_car = car("Teshla", "Teshla", "Red", "1994", "200cc")
    my_car.default()