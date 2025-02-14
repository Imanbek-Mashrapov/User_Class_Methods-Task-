import unittest
from user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Iman", "Mashrapov", 'iman.mashrapov@gmail.com', 'qwerty', '07.09.2005')

    def test_get_details(self):
        info = "User ID: 1, Name: Iman, Surname: Mashrapov, Email: iman.mashrapov@gmail.com, Birthday: 07.09.2005"
        self.assertEqual(self.user.get_details(), info)

    def test_get_age(self):
        exp_age = datetime.now().year - 2005
        self.assertEqual(self.user.get_age(), exp_age)


if __name__ == "__name__":
    unittest.main()
