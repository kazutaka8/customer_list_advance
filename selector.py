# ユーザーからのコマンド受付(S,A,F,E,D,Q)
import show
import add
import find
import edit
import delete
# import logging

# logger = logging.getLogger("app")


def command_selector():
    while True:
        user_command = input("\nYour command > ").upper()
        if user_command == "S":
            show.show_list()
        elif user_command == "A":
            add.add_user()
        elif user_command == "F":
            find.find_user()
        elif user_command == "E":
            edit.edit_user()
        elif user_command == "D":
            delete.delete_user()
        elif user_command == "Q":
            print("Bye!")
            break
        else:
            print(f"{user_command}: command not found")
    return
