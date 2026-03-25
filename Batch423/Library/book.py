from publisher import Publisher
class Book:
    def __init__(self,title:str,author:list,publisher:Publisher,price:float,is_available:bool,edition:int,language:str):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.is_available = is_available
        self.edition = edition
        self.language = language
    def __str__(self):
        return f'{self.title} by {list(map(lambda x:x.__str__() ,self.author))}\nfrom {self.publisher}\n{self.price}$'