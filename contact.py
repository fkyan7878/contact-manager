class Contact:
    def __init__(self,name,number,email):
        self.name = name
        self.number = number
        self.email = email


    def to_dict(self):
        return {
            "name": self.name, 
            "number": self.number, 
            "email": self.email
        }