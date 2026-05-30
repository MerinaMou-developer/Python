def validate_registration(data):
    if not data.get("username"):
        return "username is required"
    if not data.get("email"):
        return "email is required"
    password=data.get("password")
    if not password:
        return "password is required"
    if len(password)<8:
        return "password too short"
    
    age=data.get("age")

    if not isinstance(age,int):
        return "age must be a number"
    
    if age<18:
        return"must be adult"
    
    return "validation passed"



# Phase 1 : 
# if condition
# early return 
# isinstance() 
# .get() 
# len() 
# strip()
# try/except

def validate_registration(data):
    if not data:
        return "Data is required"
    
    name=data.get("name", "").strip()

    if not name:
        return "name is required"
    
    age=data.get("age")
    if not isinstance(age,int):
        return "age must be a number"
    
    if age<18:
        return "must be adult"
    
    password=data.get('password',"")
    if len(password)<8:
        return "password too short"
    
    return "validation passed"




user={
    "name":" ",
    "age":8,
    "password":"abcd1234"
}

print(validate_registration(user))


# phase 2
# Learn validations for: 
# email
#  password 
# phone
#  date
#  list ,price, quantity


from datetime import datetime

def validate_order(data):
    email=data.get("email","").strip()

    if not email:
        return "email is required"
    
    if '@' not in email:
        return "invalid email format"
    
    phone=data.get("phone","").strip()
    
    if not phone.isdigit():
        return "invalid phone format"
    
    quantity=data.get("quantity")
    if not isinstance(quantity,int):
        return "quantity must be integer"
    
    if quantity<1:
        return "quantity invalid"
    
    price=data.get("price")
    
    if price<=0:
        return "price invalid"
    
    delivery_data=data.get("delivery_date")
    try:
        datetime.strptime(delivery_data,"%Y-%m-%d")
    except ValueError:
        return "invalid delivery date format"
    
    return "validation passed"



# phase 3

# Complex validations:
# booking conflict
# duplicate email 
# permission checks
# API validation 
# serializer validation (DRF)

# duplicate email

def validate_email(email,users):
    for user in users:
        if user[email]==email:
            return "email already exists"
        
        return "email is valid"
    

# django version

# User.objects.filter(email=email).exists():
#            raise validationError("email already exists")


# Booking Conflict Detection

def check_booking_conflict(room_id,booking_date,bookings):
    for booking in bookings:
        if (booking["room"]==room_id and booking["date"]==booking_date):
            return "room is already booked"
        
        return "room is available"


# django version

# conflict=bookings.objects.filter(room=room_id,date=booking_date).exists()
# if conflict:
#     raise ValidationError"room is already booked")


bookings = [
    {
        "room": 101,
        "date": "2026-06-15"
    }
]


# permission checks

order={
    "id":1,
    "user_id":5
}

current_user={
    "id":7
}

def can_edit_order(current_user,order):

    if current_user["id"]!=order["user_id"]:
        return "Permission denied"
    return "Allowed"



# Serializer Validation (DRF)

# from rest_framework import serializers

# class UserSerializer(serializers.Serializer):
#     email=serializers.EmailField()
#     age=serializers.IntegerField()



class UserSerializer(serializers.Serializer):
    age=serializers.IntegerField()
    def validate_age(self,value):
        if value<18:
            raise serializers.ValidationError("Must be adult")
        return value
    

# Validate Email Uniqueness

def validate_email(self,value):
    if user.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email already Exists")
    
    return value


# Validate Email Uniqueness

def validate(self,data):
    if data["checkout"]<=data["checkin"]:
        raise serializers.ValidationError("Invalid booking Period")
    
    return data



# Interview Favorite Example

# Booking serializer.

class BookingSerializer(
    serializers.Serializer
):

    room_id = serializers.IntegerField()

    check_in = serializers.DateField()

    check_out = serializers.DateField()

    def validate(self, data):

        if (
            data["check_out"]
            <=
            data["check_in"]
        ):
            raise serializers.ValidationError(
                "Check out must be later"
            )

        return data



