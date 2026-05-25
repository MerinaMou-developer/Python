

def validate_booking(booking):
    if "title" not in booking:
       return "Title is required!"
    if len(booking["title"]) > 50:
        return "length must be less than 50 chars"
    if "seats" not in booking:
        return "Seats is required!"
    if not isinstance(booking["seats"], int):
        return "Seats must be a number"
    
    if booking["seats"] < 1 or booking["seats"] > 10:
        return "Seats must be between 1 and 10!"
    
    return "booking is valid!"


print(validate_booking({"title": "Meeting", "seats": 5}))
# → "Booking is valid!"

print(validate_booking({"seats": 5}))
# → "Title is required!"

print(validate_booking({"title": "Meeting", "seats": "abc"}))
# → "Seats must be a number!"

print(validate_booking({"title": "Meeting", "seats": 15}))
# → "Seats must be between 1 and 10!"