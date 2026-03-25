class Role:
    name = "Role"
    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def operations_choice():
        return """
                Enter 1 : To add role 
                Enter 2 : To view role
                Enter 3 : To update role
                Enter 4 : To remove role
                """
    def __str__(self):
        return self.name