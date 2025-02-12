from datetime import datetime


class User:
    def __init__(self, user_id, name, surname, email='', password='', birthday=None):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = datetime.strptime(birthday, "%d.%m.%Y")

    def get_details(self):
        return f"User ID: {self.user_id}, Full name: {self.name} {self.surname}, Email: {self.email}, Birthday: {self.birthday}"

    def get_age(self):
        age = datetime.now().year - self.birthday.year
        return





