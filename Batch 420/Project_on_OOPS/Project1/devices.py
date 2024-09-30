class Electronics:
    body_type = 'HardWare'
    def __init__(self,voltage) -> None:
        self.voltage = voltage

class Brand:
    def __init__(self,name,origin):
        self.name = name
        self.origin = origin

class Camera:
    pass
class Storage:
    pass
class SmartPhone(Electronics):
    def __init__(self,price:float,brand:Brand,voltage):
        self.features = []
        # Electronics.__init__(self,voltage)
        super().__init__(voltage)
        self.price = price
        self.brand = brand
        self.features.append(Camera())
        self.features.append(Storage())


