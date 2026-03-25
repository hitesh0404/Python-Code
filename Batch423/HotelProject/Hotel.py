class Hotel:
    def __init__(self,name:str,location:str,rating:float):
        self.name = name
        self.location = location
        self.rating = rating
        self.category = []
        self.rooms = []
    def __str__(self):
        return f'{self.name} located at {self.location}'
        