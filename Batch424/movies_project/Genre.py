class Genre:
    name = "Genre"
    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def operations_choice():
        return """
                Enter 1 : To add genre 
                Enter 2 : To view genre
                Enter 3 : To update genre
                Enter 4 : To remove genre
                """
    def __str__(self):
        return self.name