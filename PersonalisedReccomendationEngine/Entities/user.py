class User:
    user_id = 0
    phome_number = ""
    email = ""
    address = ""
    first_name = ""
    last_name = ""

    def __init__(self, user_id, phone_number, email, address, first_name, last_name):
        self.user_id = user_id
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.first_name = first_name
        self.last_name = last_name

    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_email(self):
        return self.email   
    
    def get_phone_number(self):
        return self.phone_number