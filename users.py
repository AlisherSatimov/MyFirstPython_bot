class User:
    def __init__(self,user_id,user_name,user_contact,user_location):
        self.user_id = user_id
        self.user_name = user_name
        self.user_contact = user_contact
        self.user_location = user_location

    def get_info(self):
      info = f"{self.user_id}"
