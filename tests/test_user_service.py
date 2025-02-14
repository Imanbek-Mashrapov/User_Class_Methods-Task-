import unittest
from user_service import UserService
from user import User


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Iman", "Mashrapov", 'iman.mashrapov@gmail.com', 'qwerty', '07.09.2005')

    def test_add_user(self):
        UserService.add_user(self.user)
        self.assertIn(self.user, UserService.users.values())

    def test_find_user(self):
        UserService.add_user(self.user)
        self.assertIn(self.user.user_id, UserService.users.keys())

    def test_delete_user(self):
        UserService.add_user(self.user)
        UserService.delete_user(self.user.user_id)
        self.assertNotIn(self.user, UserService.users)

    def test_update_user(self):
        UserService.add_user(self.user)
        new_user = User(1, "Aman", "Mashrapov", 'aman.mashrapov@gmail.com', 'qwerty', '01.09.2003')
        UserService.update_user(self.user.user_id, new_user)
        self.assertEqual(new_user, UserService.users[self.user.user_id])

    def test_get_number(self):
        UserService.users = {}
        user1 = User(1, 'Aaa', 'Bbb')
        user2 = User(2, 'Ccc', 'Ddd')
        user3 = User(3, 'Eee', 'Fff')
        UserService.add_user(user1)
        UserService.add_user(user2)
        UserService.add_user(user3)
        number = len(UserService.users)
        expect_number = UserService.get_number()
        self.assertEqual(number, expect_number)

    def test_get_all_users(self):
        UserService.users = {}
        user1 = User(1, 'Aaa', 'Bbb')
        user2 = User(2, 'Ccc', 'Ddd')
        user3 = User(3, 'Eee', 'Fff')
        UserService.add_user(user1)
        UserService.add_user(user2)
        UserService.add_user(user3)
        lst_users = [user1, user2, user3]
        expect_lst = UserService.get_all_users()
        self.assertEqual(lst_users, expect_lst)

if __name__ == "__main__":
    unittest.main()

