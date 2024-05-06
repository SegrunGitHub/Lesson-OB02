
class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)

    def remove_user(self, user_id):
        for u in self.__user_list:
            if u.get_user_id() == user_id:
                self.__user_list.remove(u)
                break

    def get_user_list(self):
        return self.__user_list


# Пример использования
user1 = User(1, 'Alice')
user2 = User(2, 'Bob')

admin = Admin(0, 'Admin')
admin.add_user(user1)
admin.add_user(user2)

print("User list:")
for user in admin.get_user_list():
    print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

admin.remove_user(1)

print("\nAfter removing user 1:")
for user in admin.get_user_list():
    print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
