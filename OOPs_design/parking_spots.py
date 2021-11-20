from enum import Enum
from typing import List

'''
1.  
A car can be represented as <size> <color> <brand>. For example, "Small Silver BMW", "Large Black Nissan" are 
all valid car representations. All the allowed sizes are "Small", "Medium", and "Large". 

In this parking lot you are given the number of parking slots available at the start, labelled from 0 to n - 1. Your 
system must support these following commands: 

"park [spot] [car]": Attempt to park the car into the given spot. If the given spot is unavailable (because a car 
cannot park there, or there is already a car), the park will try to park at the next spot in order until it finds an 
available slots, or there are no more slots left (in which case the car leaves the parking lot). 
"remove [spot]": 
Remove the car parked at that spot. Do nothing if there are no car there. "print [spot]": Print the representation of 
the car at that spot, or "Empty" if that spot is empty. 
"print_free_spots": Print the number of slots free in the 
parking lot. Parameters n: The number of slots in the parking lot. instructions: A string matrix representing the 
instructions. 

Result 
A list of strings representing the printed output. 

2. 
In order to save space, there are new restrictions in place in terms of what cars are allowed to park at which 
spots. There is now a size restriction for each parking spots, from "Small", "Medium", or "Large". Only cars with 
less or equal size than the spot are allowed to park there. Remember if a car cannot park at a spot it will try to 
find the next available spot down the parking lot, if one exists. 

Parameters
spots: A list of strings representing the size of the parking spots from spot 0 to n - 1.
instructions: A string matrix representing the instructions.
Result
A list of strings representing the printed output.
'''


class CarSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


SIZE_STRING = {
    CarSize.SMALL: "Small",
    CarSize.MEDIUM: "Medium",
    CarSize.LARGE: "Large",
    }

SIZES = {e: n for n, e in SIZE_STRING.items()}


class Car:
    def __init__(self, size: str, color: str, brand: str):
        self.size = SIZES[size]
        self.color = color
        self.brand = brand

    def __str__(self) -> str:
        return f"{SIZE_STRING[self.size]} {self.color} {self.brand}"


class ParkingSpot:
    def __init__(self):
        self.parked_car = None

    def park(self, car: Car) -> bool:
        if self.parked_car:
            return False
        self.parked_car = car
        return True

    def leave(self) -> None:
        if self.parked_car:
            self.parked_car = None
            return True
        return False

    def __str__(self) -> str:
        if self.parked_car:
            return str(self.parked_car)
        return "Empty"


class ParkingLot:
    def __init__(self, size: int):
        self.parking_spots: list[ParkingSpot] = []
        self.__size = size
        self.__free_spots = size
        for _ in range(size):
            self.parking_spots.append(ParkingSpot())

    def free_spots(self) -> int:
        return self.__free_spots

    def park(self, index: int, car: Car) -> bool:
        for i in range(index, self.__size):
            if self.parking_spots[i].park(car):
                self.__free_spots -= 1
                return True
        return False

    def leave(self, index: int) -> None:
        if self.parking_spots[index].leave():
            self.__free_spots += 1


def parking_system(n: int, instructions: List[List[str]]) -> List[str]:
    output_lines = []
    parking_lot = ParkingLot(n)
    for instruction in instructions:
        operation, *args = instruction
        if operation == "park":
            slot, *car = args
            parking_lot.park(int(slot), Car(*car))
        elif operation == "remove":
            parking_lot.leave(int(args[0]))
        elif operation == "print":
            output_lines.append(str(parking_lot.parking_spots[int(args[0])]))
        elif operation == "print_free_spots":
            output_lines.append(str(parking_lot.free_spots()))
    return output_lines


if __name__ == '__main__':
    n = int(input())
    instructions = [input().split() for _ in range(int(input()))]
    res = parking_system(n, instructions)
    for line in res:
        print(line)
