from models.user import User

# print("Hello Word")

# user = {
#     'name': 'John',
#     'birth': 1980
# }
# user2 = {
#     'name': 'Helena',
#     'birth': 1995
# }
# user3 = {
#     'name': 'Sandra',
#     'birth': 1978
# }

# users = [user, user2, user3]

# for user in users:
#     print(user['name'], user['birth'])


# print(user['birth'], user2['birth'], user3 ['birth'])

# print(user.name, user2.birth)


user1 = User("Dani", 1980)
user2 = User("Maria", 1985)


users = [user1, user2]

for user in users:
    print(user.name, user.birth, user.is_adult(), user.get_age())
