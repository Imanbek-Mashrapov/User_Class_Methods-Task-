# User Management System

## Overview
#### This project is an object-oriented implementation of a user management system in Python. It includes three classes: User, UserService, and UserUtil, along with corresponding unit tests. The project demonstrates instance variables, class attributes/methods, and static methods.

## Features
#### User management with attributes: user_id, name, surname, email, password, and birthday.

#### User Utility methods for user ID and password generation, email validation, and email formatting.

#### User service for adding, updating, deleting, and retrieving users.

#### Unit tests to verify the correctness of the system.

## Classes and Methods

### 1. User Class

#### Instance Variables:

- #### user_id (int) – Unique identifier for the user.
- #### name (str) – First name of the user.
- #### surname (str) – Last name of the user.
- #### email (str) – Email of the user.
- #### password (str) – Password of the user.
- #### birthday (datetime) – Birthday of the user.

#### Methods:

- #### __init__(self, user_id, name, surname, birthday): Initializes user details.
- #### get_details(self): Returns a formatted string containing user details.
- #### get_age(self): Computes and returns the user’s age.
- ### __str__(self): Returns a formatted string when printing an object

### 2. UserService Class

#### Class Attribute:

- #### users – A dictionary to store all User objects (key=user_id, value=User object).

#### Class Methods:

- #### add_user(cls, user): Adds a User object to users.
- #### find_user(cls, user_id): Searches for a user by user_id and returns the user object if found.
- #### delete_user(cls, user_id): Removes a user from users by user_id.
- #### update_user(cls, user_id, user_update): Updates user attributes using user_update object arguments.
- #### get_number(cls): Returns the number of users in users.

### 3. UserUtil Class

#### Static Methods:

- #### generate_user_id(): Generates a unique 9-digit user_id (first two digits from the current year, remaining digits randomly generated).
- #### generate_password(): Generates a secure password (at least 8 characters, 1 uppercase, 1 lowercase, 1 digit, 1 special character).
- #### is_strong_password(password): Checks if the given password meets security requirements.
- #### generate_email(name, surname, domain): Generates an email address (name.surname@domain.com).
- #### validate_email(email): Checks if the given email follows a valid pattern.

## Unit Testing

#### Unit tests are included for all classes and their respective methods:

- #### TestUser: Tests for User class methods.
- #### TestUserService: Tests for UserService class methods.
- #### TestUserUtil: Tests for UserUtil class methods.

## Sample Input/Output

### Example 1: Creating a User

#### Input:
``` python
user1 = User(user_id=230121021, name="Iman", surname="Mashrapov>", 'iman.mashrapov@gmail.com'
print(user1.get_details())
```

#### Output:
``` ssh
User ID: 230121021 
Name: Iman
Surname: Mashrapov
Email: iman.mashrapov@gmail.com
Birthday: None
```

### Example 2: Adding user object to users dictionary
#### Input:
```python
user1 = User(230121021, "Iman", "Mashrapov")
UserService.add_user(user1)

for person in UserService.users.values():
    print(person)
```

#### Output:
```ssh
User ID: 230121021, Name: Iman, Surname: Mashrapov, Email: , Birthday: None
```

### Example 3: Generating email and password for users
#### Input:
```python
user1 = User(230121021, "Iman", "Mashrapov")
user1.email = UserUtil.generate_email(user1.name, user1.surname)
user1.password = UserUtil.generate_password(10)

print(user1.get_details())
print(f'User1 password: "{user1.password}"')
```

#### Output:
```ssh
User ID: 230121021, Name: Iman, Surname: Mashrapov, Email: iman.mashrapov@gmail.com, Birthday: None
User1 password: "Eou:WT.r5+
```

### Example 4: Generate user id:
#### Input:
```python
user1 = User(UserUtil.generate_user_id(), 'Aaa', 'Bbb')
print(user1)
```

#### Output:
```ssh
User ID: 254621665, Name: Aaa, Surname: Bbb, Email: , Birthday: None
```

### Example 5: Check if password is strong and validate email
#### Input:
```python
password1 = 'qwerty123'
password2 = 'Pkt197#uhg786!'

email1 = 'ronaldo7@gmail.com'
email2 = 'john.doe@gmail.com'

print(UserUtil.is_strong_password(password1))
print(UserUtil.is_strong_password(password2))
print(UserUtil.validate_email(email1))
print(UserUtil.validate_email(email2))
```

#### Output:
```ssh
False
True
False
True
```

## UML:
![user_management_uml.png](user_management_uml.png)



