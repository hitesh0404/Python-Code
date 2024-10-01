class Post:
    def __init__(self,id,title,data) -> None:
        self.id = id
        self.title  = title
        self.data = data

class User:
    all_user = []
    def __init__(self,user_id,username,first_name,last_name,age,password) -> None:
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        User.blood_color
        User.all_user.append(self)
        self.posts = []
    def create_post(self,post_id,post_title,post_data):
        post_obj = Post(post_id,post_title,post_data)
        self.posts.append(post_obj)

   
    def like(self,post_id):
        pass

    def __str__(self) -> str:
        return f'{self.user_id} {self.first_name} {self.last_name}'
    
