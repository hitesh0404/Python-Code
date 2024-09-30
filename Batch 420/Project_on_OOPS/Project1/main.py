from devices import *


samsung = Brand('samsung','Korea')
apple = Brand('Apple','US')
micromax = Brand('Micromax','India')
jio = Brand('Relience Jio','India')

iphone16 = SmartPhone(160000.00,apple,0.5)
print(iphone16.voltage,iphone16.brand.name,iphone16.price,iphone16.brand.origin)
