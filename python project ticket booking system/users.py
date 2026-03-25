class UserManager:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        
        for user in self.users:
            if user['username'] == username:
                print("User already exists.")
                return None
        new_user = {'username': username, 'password': password}
        self.users.append(new_user)
        return new_user

    def login(self, username, password):
        
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return user
        print("Invalid credentials.")
        return None
