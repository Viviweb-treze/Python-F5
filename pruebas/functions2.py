import datetime
actual_year = datetime.date.today().year

# DATABASE
user1 = {"name": "Kareliz", "isAdmin": True, "bith": 1990, }
user2 = {"name": "Jose", "isAdmin": True, "bith": 2010, "parent": False}


# DEFINICION

def can_access(user):
    age = actual_year - user["bith"]
    print(age)
    if not user["isAdmin"] or age < 18:
        return False
    return True


def access_sys(user):
    if not can_access(user):
        print(user["name"] + " Acceso Denegado")
        return

    print(user["name"] + " Ha accedido al sistema ")
    print(user["name"] + " Ha accedido al sistema ")
    print(user["name"] + " Ha accedido al sistema ")
    print(user["name"] + " Ha accedido al sistema ")


# MAIN
access_sys(user1)
access_sys(user2)
