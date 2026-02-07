from typing import List
from models.ParkingFloor import parking_floor
from models.ParkingSpot import parking_spot
from models.EntryGate import entry_gate
from models.ExitGate import exit_gate

class parking_lot:
    def __init__(
            self,
            name : str,
            address : str,
            parking_floors : List[parking_floor],
            entry_gates : List[entry_gate],
            exit_gates : List[exit_gate]
    ):
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.entry_gates = entry_gates
        self.exit_gates = exit_gates

    @classmethod
    def builder(cls):
        return cls.Builder()
    
    class Builder:
        def __init__(self):
            self.name = None
            self.address = None
            self.parking_floors = []
            self.entry_gates = []
            self.exit_gates = []

        def name(self,name : str):
            self._name = name # _name for making the name behave like protected, not actually like java but conceptually as python trusts their developers.
            return self # for executing chaining returns or calls.
        
        def address(self, address : str):
            self._address = address
            return self
        
        def with_floors(self, floor_count : int, capacity_per_floor: int):
            
            for floor in range(1,floor_count + 1):
                spots = [
                    parking_spot(spot)
                    for spot in range(1,capacity_per_floor+1)
                    ]
                
                floor = parking_floor(
                    floor_number = floor,
                    parkingSpots = spots
                )

                self.parking_floors.append(floor)

            return self

        def add_entry_gate(self, gate_number : int):
            self._entry_gates.append(entry_gate(gate_number))
            return self
    
        def add_exit_gate(self, gate_number : int):
            self._exit_gates.append(exit_gate(gate_number))
            return self
        
        def build(self):
            return parking_lot(
                name = self._name,
                address = self._address,
                parking_floors = self._parking_floors,
                entry_gates = self._entry_gates,
                exit_gates = self._exit_gates
            )
            

