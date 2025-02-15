from datetime import datetime


class User:
    def __init__(self, user_id, name, surname, email='', password='', birthday=None):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Birthday: {self.birthday}"

    def get_age(self):
        if self.birthday:
            birth_year = datetime.strptime(self.birthday, '%d.%m.%Y')
            age = datetime.now().year - birth_year.year
            return age
        return None

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Birthday: {self.birthday}"
