def login_required(func):
        def wrapper(user):
            if not user["is_logged_in"]:
                return "please login first"
            return func(user)
        return wrapper
    


@login_required
def Booking(user):
    return "Here is your Booking"

user1={"name":"Mou","is_logged_in":True}
user2={"name":"Alice","is_logged_in":False}

print(Booking(user1))
print(Booking(user2))