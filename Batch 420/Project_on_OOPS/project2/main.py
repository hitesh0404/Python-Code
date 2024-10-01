from user import User
import uuid
stop=False
while(stop!=True):
    data = input('''
            If You want to add user 
            press 1...
            if You want to exit 
            press 2...''')
    if data==1:
        user_id = uuid.uuid4()
        username = input('Enter UserName: ')
        first_name = input('Enter First Name: ')
        last_name  = input('Enter Last Name: ')
        age = input('Enter Age: ')
        password = input('Enter password: ')
        confirm_password = input('Confirm password: ')
        u =User(user_id,username,first_name,last_name,
                age,password,confirm_password)
    elif data==2:
        break
      