class RoomCategory:
    def __init__(self,category:str):
        self.category = category
    def __str__(self):
        return self.category
class Room:
    def __init__(self,number:int,category:RoomCategory,capacity:int):
        self.number = number
        self.category = category
        self.capacity = capacity
    def __str__(self):
        return f'{self.number} is {self.category} room of capacity {self.capacity}'