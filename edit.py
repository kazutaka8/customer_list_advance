# 顧客の編集 （コマンドEにて呼び出し）
# import logging
from validation import name_validation, age_validation
from config import Customer


# logger = logging.getLogger("app")


def edit_user():
    name = input("User name > ")
    try:
        user = Customer.get(Customer.name == name)

        new_name = input(f"New user name({user.name}) >")
        if not name_validation(new_name):
            return

        new_age = input(f"New user age({user.age}) >")
        if not age_validation(new_age):
            return
        int_new_age = int(new_age)

        user.name = new_name
        user.age = int_new_age
        user.save()
        print(f"Update user: {user.name}")

    except Customer.DoesNotExist:
        print(f"Sorry, {name} is not found")

    return
