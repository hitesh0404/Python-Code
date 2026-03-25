from Hotel import Hotel
from Guest import Guest
from Rooms import Room,RoomCategory
from Reservation import Reservation
def create_hotel():
    global hotels
    # name = input("Enter the Name :")
    # location = input("Enter the Location :")
    # rating = input("Enter the Rating :")
    name,location,rating = input("Enter the Name Location and rating seprated by ,  :").split(',')
    rating = int(rating)
    hotels.append(Hotel(name=name,location=location,rating=rating))
def create_guest():
    global guests
    print("Enter the ID Name and Contact seprated by ,  :")
    id,name,contact= input().split(',')
    id=int(id)
    guests.append(Guest(id=id,name=name,contact=contact))
def show_hotels():
    if len(hotels) == 0:
        print("Create Hotel First")
        create_hotel()
    for index,hotel in enumerate(hotels):
        print(index,hotel)

def create_category(hotel_id=-1):
    if hotel_id==-1:
        show_hotels()
        hotel_id = int(input("Enter Hotel ID"))
    name = input('Enter Category Name ')
    hotels[hotel_id].category.append(RoomCategory(name))

def show_category(hotel_id=-1):
    if hotel_id == -1:
        show_hotels()
        hotel_id = int(input("Enter the Hotel ID"))
    if len(hotels[hotel_id].category)==0:
        create_category(hotel_id)
    for index,cat in enumerate(hotels[hotel_id].category):
        print(index,cat)

def create_room():
    show_hotels()
    hotel_id = int(input("Enter the Hotel ID"))
    show_category(hotel_id=hotel_id)
    category = int(input('Enter category ID'))
    number,capacity  = input("Enter The Room Number and Capacity seperated by ,  :").split(',') 
    new_room = Room(number=number,category=hotels[hotel_id].category[category],capacity=int(capacity))
    hotels[hotel_id].rooms.append(new_room)
def show_rooms():
    show_hotels()
    hotel_id = int(input("Enter Hotel ID"))
    for index,room in enumerate(hotels[hotel_id].rooms):
        print(index,room)
def choice():
    print(
        '''
    Press 1 to create Hotel
    Press 2 to create Room
    Press 3 to create Guest
    Press 4 to show Hotels
    Press 5 to show Guests
    Press 6 to show Rooms
    Press 7 to show Room Category
    Press 8 to Create Room Category
    Press 0 to Exit
        '''
    )
num = -1
hotels = []
guests = []
while(num!=0):
    choice()
    num = int(input())
    match(num):
        case 1:
            create_hotel()
        case 2:
            create_room()
        case 3:
            create_guest()
        
        case 4:
            # print(list(map(lambda x:x.__str__() ,hotels)))
            for h in hotels:
                print(h)
        case 5:
            for g in guests:
                print(g)
        case 6:
            show_rooms()
        case 7:
            show_category()
        case 8: 
            create_category()
        case 0:
            break