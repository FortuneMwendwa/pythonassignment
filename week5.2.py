class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water...")


class Animal:
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print("🐕 Running on the ground...")


class Bird(Animal):
    def move(self):
        print("🐦 Flying through the air...")

vehicles = [Car(), Plane(), Boat()]
animals = [Dog(), Bird()]

print("=== Vehicles ===")
for v in vehicles:
    v.move()

print("\n=== Animals ===")
for a in animals:
    a.move()
