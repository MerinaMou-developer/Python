
# arg
def total(*arg):
    return sum(arg)

def total_price(*prices):
    return sum(prices)

# kwarg
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


def create_user(**kwargs):
    return {
        "name": kwargs.get("name", "Unknown"),
        "email": kwargs.get("email", ""),
        "role": kwargs.get("role", "user"),
    }

print(total(3,8,9))

info(name="Mou",age=26)


print(total_price(100,500,1000))
print(create_user(name="MOu",email="merinamou3@gmail.com"))



# bad code
def process_booking(booking):
    if booking:
        if booking['status']=='confirmed':
            if booking['room']:
                return "ok"

print(process_booking({'room': 'A-1', 'status': 'confirmed'}))


# good code
def process_booking(booking):
    if not booking:
        return "No Booking Found"
    if booking['status']!='confirmed':
        return "booking Not confirmed"
    if not booking['room']:
        return "No room assigned"

print(process_booking({'room': 'A-1', 'status': 'confirmed'}))

booking2 = {
    "status": "pending",
    "room": "B-202"
}

print(process_booking(booking2))


booking3 = {
    "status": "confirmed",
    "room": ""
}

print(process_booking(booking3))

# TEST 4
booking4 = None

print(process_booking(booking4))