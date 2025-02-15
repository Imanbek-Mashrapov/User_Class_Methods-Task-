import unittest
from user_util import UserUtil
from user_service import UserService
from user import User
from datetime import datetime
import string


class TestUserUtil(unittest.TestCase):
    def setUp(self):
        UserService.users = {}
        self.user1 = User(UserUtil.generate_user_id(), 'Aaa', 'Bbb')
        self.user2 = User(UserUtil.generate_user_id(), 'Ccc', 'Ddd')
        self.user3 = User(UserUtil.generate_user_id(), 'Eee', 'Fff')
        UserService.add_user(self.user1)
        UserService.add_user(self.user2)
        UserService.add_user(self.user3)

    def test_generate_user_id(self):
        current_year = str(datetime.now().year)
        self.assertIsInstance(self.user1.user_id, str)  # is user_id string
        self.assertEqual(len(self.user1.user_id), 9)  # does length of user_id equal to 9
        self.assertEqual(self.user1.user_id[:2], current_year[2:])  # first two digits of id are current year
        self.assertNotEqual(self.user1.user_id, self.user2.user_id)  # users have unique id

    def test_generate_password(self):
        self.user1.password = UserUtil.generate_password(10)  # length of password is 10
        self.user2.password = UserUtil.generate_password()  # length of password is 8, by default
        self.user3.password = UserUtil.generate_password(12)  # length of password is 12

        for person in UserService.users.values():
            self.assertGreaterEqual(len(person.password), 8, "Someone's length of password is less than 8")  # is password greater than 8

        for person in UserService.users.values():  # check characters of password
            password = person.password
            self.assertTrue(any(char.islower() for char in password), "No lowercase letter")
            self.assertTrue(any(char.isupper() for char in password), "No uppercase letter")
            self.assertTrue(any(char.isdigit() for char in password), "No digit")
            self.assertTrue(any(char in string.punctuation for char in password), "No special character")

        self.assertEqual(len(self.user1.password), 10)
        self.assertEqual(len(self.user2.password), 8)
        self.assertEqual(len(self.user3.password), 12)

    def test_is_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password("A1b@strong"))  # Valid password
        self.assertFalse(UserUtil.is_strong_password("a1@strong"))  # No uppercase
        self.assertFalse(UserUtil.is_strong_password("A1@STRONG"))  # No lowercase
        self.assertFalse(UserUtil.is_strong_password("Ab@Strong"))  # No digit
        self.assertFalse(UserUtil.is_strong_password("A1bStrong"))  # No special char

    def test_genearte_email(self):
        self.assertEqual(UserUtil.generate_email('Iman', 'Mashrapov'), 'iman.mashrapov@gmail.com')
        self.assertEqual(UserUtil.generate_email('Aaa', 'Bbb', 'yahoo'), 'aaa.bbb@yahoo.com')
        self.assertEqual(UserUtil.generate_email('CCC', 'DDD'), 'ccc.ddd@gmail.com')

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@gmail.com"))
        self.assertFalse(UserUtil.validate_email("john.doegmail.com"))  # No @
        self.assertFalse(UserUtil.validate_email("johndoe@gmail.com"))  # No '.' in local part
        self.assertFalse(UserUtil.validate_email("john.doe@gmailcom"))  # No '.' in domain
        self.assertFalse(UserUtil.validate_email("john.doe@gmail.org"))  # No ending with '.com'
        self.assertFalse(UserUtil.validate_email("john123.doe@gmail.com"))


if __name__ == "__main__":
    unittest.main()
