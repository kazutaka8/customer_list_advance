# 顧客の削除 （コマンドDにて呼び出し）
# import logging
from config import Customer


# logger = logging.getLogger("app")


def delete_user():
    name = input("User name > ")
    try:
        user = Customer.get(Customer.name == name)
        user.delete_instance()
        print(f"User {name} is deleted")
    except Customer.DoesNotExist:
        print(f"Sorry, {name} is not found")
    return
