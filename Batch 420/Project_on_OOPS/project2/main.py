from user import User
import uuid
stop=False
while(stop!=True):
    data = int(input('''
            If You want to add user 
            press 1...
            if You want to exit 
            press 2...
            if You want to print all the availble user
            press 3...
            if You want to add post
            press 4...
                     
            '''        ))
    if data==1:
        user_id = uuid.uuid4()
        username = input('Enter UserName: ')
        first_name = input('Enter First Name: ')
        last_name  = input('Enter Last Name: ')
        age = input('Enter Age: ')
        password = input('Enter password: ')
        confirm_password = input('Confirm password: ')
        if password!=confirm_password:
            print('mismatch password')
        else:
            u =User(user_id,username,first_name,last_name,
                age,password)
    elif data==2:
        break
    elif data ==3 :
        for i in User.all_user:
            print(i)
    elif data ==4 :
        post_id =uuid.uuid4()
        username = input('enter username')
        for i in User.all_user:
            if i.username == username:
                title = input('enter post title')
                data = input('enter post data')
                i.create_post(post_id,title,data)

      