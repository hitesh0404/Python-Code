class Guest:
    def __init__(self,id:int,name:str,contact:int):
        self.id = id
        self.name = name
        self.contact = contact
    def __str__(self):
        return f'{self.id}  {self.name} {self.contact}'
        