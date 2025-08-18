def name_validation(name):
    if not name.isascii():
        print("User name to be ascii")
        return False
    elif len(name) == 0:
        print("User name can't be blank")
        return False
    elif len(name) > 20:
        print("User name is too long(maximun is 20 characters)")
        return False
    else:
        return True


def age_validation(age):
    try:
        int_age = int(age)
    except Exception:
        print("Age is not positive integer")
        return False
    if int_age > 120:
        print("Age is grater than 120")
        return False
    elif int_age < 0:
        print("Age is less than 0")
        return False
    else:
        return True
