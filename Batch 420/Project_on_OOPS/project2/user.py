class User:
    def __init__(self,user_id,username,first_name,last_name,age,password,confirm_password) -> None:
        if password!=confirm_password:
            print('mismatch password')
            return 'error: password is not matching'
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
    
    def post(self,post_title,post_data):
        pass

    def like(self,post_id):
        pass

