# 顧客の追加 （コマンドAにて呼び出し）
# 重複を許可しないように修正
# import logging
from validation import name_validation, age_validation
from config import Customer


# logger = logging.getLogger("app")


def create_user(name, age):
    user = Customer(name=name, age=age)
    user.save()


def add_user():
    name = input("New user name > ")
    if not name_validation(name):
        return

    age = input("New user age > ")
    if not age_validation(age):
        return
    int_age = int(age)

    if Customer.select().where(Customer.name == name).exists():
        print(f"Duplicated user name {name}")
        return

    create_user(name, int_age)
    print(f"Add new user: {name}")
    return
