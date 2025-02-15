from user import User
from user_service import UserService
from user_util import UserUtil


if __name__ == "__main__":
    # create some user objects
    user1 = User(UserUtil.generate_user_id(), "Iman", "Mashrapov")
    user2 = User(UserUtil.generate_user_id(), "Aman", "Omurbekov")
    user3 = User(UserUtil.generate_user_id(), "Argen", "Bakyt uulu")
    user4 = User(UserUtil.generate_user_id(), "Kerim", "Erkinbekov")

    # adding user objects to users dictionary
    UserService.add_user(user1)
    UserService.add_user(user2)
    UserService.add_user(user3)
    UserService.add_user(user4)

    # generating email for each user
    user1.email = UserUtil.generate_email(user1.name, user1.surname, 'alatoo.edu.kg')
    user2.email = UserUtil.generate_email(user2.name, user2.surname, 'alatoo.edu.kg')
    user3.email = UserUtil.generate_email(user3.name, user3.surname, 'alatoo.edu.kg')
    user4.email = UserUtil.generate_email(user4.name, user4.surname, 'alatoo.edu.kg')

    # generate passwords for users
    user1.password = UserUtil.generate_password()
    user2.password = UserUtil.generate_password()
    user3.password = UserUtil.generate_password()
    user4.password = UserUtil.generate_password()

    # printing users
    for person in UserService.users.values():
        print(person)
        print(f"User's password is strong: {UserUtil.is_strong_password(person.password)}")

    print(type(user1.user_id))


