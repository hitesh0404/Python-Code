class HardWare:
    def __init__(self,t) -> None:
        print("""Here inside Hardware""")
        self.t=t
class Electronics(HardWare):
    body_type = 'HardWare'
    def __init__(self,voltage,t) -> None:
        super().__init__(t)
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
        Electronics.__init__(self,voltage,5)
        self.price = price
        self.brand = brand
        self.features.append(Camera())
        self.features.append(Storage())