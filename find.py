# 顧客の検索 （コマンドFにて呼び出し）
# import logging
from config import Customer

# logger = logging.getLogger("app")


def find_user():
    name = input("User name > ")
    try:
        user = Customer.get(Customer.name == name)
        print(f"Name: {user.name} Age: {user.age}")
    except Customer.DoesNotExist:
        print(f"Sorry, {name} is not found")
    return
