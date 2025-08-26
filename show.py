# 現在の顧客リストの表示 （コマンドSにて呼び出し）
# import logging
from config import Customer

# logger = logging.getLogger("app")


def show_list():
    user_list = Customer.select()
    for user in user_list:
        print(f"Name: {user.name} Age: {user.age}")
    return
