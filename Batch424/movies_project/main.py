from Genre import Genre
from Role import Role
def object_crud(class_name,object_list:list):
    if len(object_list)>0:
        print(f"availble {class_name.name} are")
        for i in object_list:
            print(i)
    print(class_name.operations_choice())
    ch = int(input())
    match ch:
        case 1:  
            same_genre = True
            while(same_genre):
                name = input("Enter name : ")
                if len(object_list) == 0:
                    same_genre = False
                found = False
                for i in object_list:
                    if i.name == name.upper():
                        print("it's already there in list")
                        found = True
                        break
                if not found:
                    break
                if not same_genre:
                    break
            object_list.append(class_name(name.upper()))                            
            print(f"New {class_name.name} Added successfully!")
    return object_list
def choice():
    return """
            Enter 1 : To Work with Genre
            Enter 2 : To work with Role
            Enter 0 : To Exit
    """

genre = []
role = []
if __name__ == "__main__":
    while(True):
        print(choice())
        ch = int(input("enter your Choice : "))
        match ch:
            case 1: 
                object_crud(Genre,genre)
            case 2: 
                object_crud(Role,role)
            case 0:
                print("Thanks")
                break
