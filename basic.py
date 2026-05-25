# 1️⃣ Variable

name="ahsan"
age=25
is_active=True

# 2️⃣ Function

def greet(name):
    return f"Hello, {name}!"



print(greet("ahsan"))


# 3️⃣ If/Else



def check_age(age):
    if age >= 18:
        return "You are an adult."
    else:
        return "You are not an adult."

print(check_age(18))


# 4️⃣ List

fruits=["apple","orange","banana","grape"]

print(fruits[1])

for fruit in fruits:
    print(fruit)

fruits.append("mango")

print(len(fruits))


# 5️⃣ Dictionary

bookings=[
    {"name":"Mou","study":"CSE","age":26},
    {"name":"Jorina","study":"economy","age":24},
    {"name":"kamil","study":"science","age":26}
]


for booking in bookings:
    if(booking["age"]==26):
        print(booking["name"])


# 7️⃣ Filter with List Comprehension

bookings = [
    {"id": 1, "status": "confirmed"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "confirmed"},
]

confirmed=[]

for booking in bookings:
    if booking["status"]=="confirmed":
        confirmed.append(booking)

# short way
confirmed=[b for b in bookings if b["status"]=="confirmed"]


print(confirmed)


# 8️⃣ Try/Except — Error Handling

def get_booking(booking_id):
    try:
        booking=booking.objects.get(id=booking_id)
    except Exception as e:
        return {"error":str(e)}
    


def safe_divide(a,b):
    try:
        ans=a/b
        return ans
    except Exception as e:
        return "cannot divide by Zero"


print(safe_divide(10,2))
print(safe_divide(10,0))



def get_name(data):
    try:
        return data["name"]
    except KeyError:
        return "Name not found"

print(get_name({"name": "Ahsan"})) 
print(get_name({"age": 25}))




# 9️⃣ Class — Basic OOP

class Booking:
    def __init__(self,name,study,age):
        self.name=name
        self.study=study
        self.age=age
    def summery(self):
        return f"{self.name} is studying {self.study} and is {self.age} years old."

b=Booking("Mou","CSE",26)
print(b.summery())


# 🔟 DateTime

from datetime import datetime,timedelta

now=datetime.now()
print(now)
tomorrow=now+timedelta(days=1)
one_hour_later=now+timedelta(hours=1)

if now<tomorrow:
    print("Tomorrow is in the future")

