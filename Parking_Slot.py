class ParkingLot:
    def __init__(self, floors, slots_per_floor):
        self.parking_lot = self.initialize_parking(floors, slots_per_floor)

    def initialize_parking(self, floors, slots_per_floor):
        parking_lot = {}
        for floor in range(1, floors + 1):
            parking_lot[floor] = {}
            for slot in range(1, slots_per_floor + 1):
                parking_lot[floor][slot] = None
        return parking_lot

    def find_nearest_slot(self):
        for floor, slots in self.parking_lot.items():
            for slot, car in slots.items():
                if car is None:
                    return floor, slot
        return None, None

    def park_car(self, car_number, car_color):
        floor, slot = self.find_nearest_slot()
        if floor is None:
            print("No available slots for parking.")
            return False

        self.parking_lot[floor][slot] = {'number': car_number, 'color': car_color}
        print(f"Car {car_number} ({car_color}) parked at Floor {floor}, Slot {slot}.")
        return True

    def find_car(self, search_by, value):
        for floor, slots in self.parking_lot.items():
            for slot, car in slots.items():
                if car:
                    if (search_by == "number" and car['number'] == value) or \
                       (search_by == "color" and car['color'] == value) or \
                       (search_by == "slot" and slot == value):
                        print(f"Car found at Floor {floor}, Slot {slot}: {car}")
                        return floor, slot
        print(f"Car with {search_by} '{value}' not found.")
        return None, None

    def exit_car(self, floor, slot):
        if floor in self.parking_lot and slot in self.parking_lot[floor]:
            if self.parking_lot[floor][slot] is not None:
                car = self.parking_lot[floor][slot]
                self.parking_lot[floor][slot] = None
                print(f"Car {car['number']} ({car['color']}) exited from Floor {floor}, Slot {slot}.")
                return True
            else:
                print(f"Slot {slot} on Floor {floor} is already empty.")
                return False
        print("Invalid floor or slot.")
        return False

    def show_parking_status(self):
        print("\nParking Lot Status:")
        for floor, slots in self.parking_lot.items():
            print(f"Floor {floor}: ", end="")
            for slot, car in slots.items():
                if car is None:
                    print("[Empty]", end=" ")
                else:
                    print(f"[Car: {car['number']}, Color: {car['color']}]", end=" ")
            print()

if __name__ == "__main__":
    floors = int(input("Enter the number of floors: "))
    slots_per_floor = int(input("Enter the number of slots per floor: "))

    parking_lot = ParkingLot(floors, slots_per_floor)

    while True:
        print("\n1. Park a Car")
        print("2. Find a Car")
        print("3. Exit a Car")
        print("4. Show Parking Status")
        print("5. Exit Program")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            car_number = input("Enter car number: ")
            car_color = input("Enter car color: ")
            parking_lot.park_car(car_number, car_color)

        elif choice == 2:
            print("Search by:")
            print("1. Car Number")
            print("2. Car Color")
            print("3. Slot Number")
            search_option = int(input("Enter your choice: "))

            if search_option == 1:
                value = input("Enter car number: ")
                parking_lot.find_car("number", value)
            elif search_option == 2:
                value = input("Enter car color: ")
                parking_lot.find_car("color", value)
            elif search_option == 3:
                value = int(input("Enter slot number: "))
                parking_lot.find_car("slot", value)
            else:
                print("Invalid search option.")

        elif choice == 3:
            floor = int(input("Enter floor number: "))
            slot = int(input("Enter slot number: "))
            parking_lot.exit_car(floor, slot)

        elif choice == 4:
            parking_lot.show_parking_status()

        elif choice == 5:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
