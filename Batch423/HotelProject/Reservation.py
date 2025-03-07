from datetime import datetime
from Guest import Guest
from Rooms import Room
class Reservation:
    def __init__(self,guest:Guest,check_in:datetime,check_out:datetime,rooms:list):
        self.guest = guest
        self.check_in = check_in
        self.check_out = check_out
        self.rooms = rooms
    def __str__(self):
        return f'{self.guest} booked {list(map(lambda x:x.__str__(),self.rooms))} from  {self.check_in} to {self.check_out} ' 