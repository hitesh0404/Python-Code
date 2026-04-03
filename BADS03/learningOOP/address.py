class Address:
    def __init__(self,title, address_line_one, address_line_two, pincode):
        self.title = title
        self.address_line_one = address_line_one
        self.address_line_two = address_line_two
        self.pincode = pincode
    
    def __str__(self):
        return f""" 
                title : {self.title}
                {self.address_line_one}
                {self.address_line_two}
                {self.pincode}
                """
        