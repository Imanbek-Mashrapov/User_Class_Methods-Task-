from user import User
from user_service import UserService
from user_util import UserUtil


if __name__ == "__main__":
    user1 = User(1, "Iman", "Mashrapov")
    user2 = User(2, "Aman", "Omurbekov")
    #user3 = User(3, "Argen", "Bakyt uulu")
    #user4 = User(4, "Kerim", "Erkinbekov")

    UserService.add_user(user1)
    UserService.add_user(user2)
    #UserService.add_user(user3)
    #UserService.add_user(user4)

    x = UserService.get_all_users()
    y = [user1, user2]

    print(x == y)


