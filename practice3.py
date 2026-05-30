# Existing bookings:

# existing_bookings = [
#     {
#         "room": 101,
#         "check_in": "2026-07-10",
#         "check_out": "2026-07-15"
#     },
#     {
#         "room": 102,
#         "check_in": "2026-07-20",
#         "check_out": "2026-07-25"
#     }
# ]


# New booking request:

# new_booking = {
#     "room": 101,
#     "check_in": "2026-07-12",
#     "check_out": "2026-07-18",
#     "guests": 2
# }

# Rules
# Edge Cases

# Required fields:

# room
# check_in
# check_out
# guests

# Validate:

# guests must be integer
# guests must be greater than 0
# Date Validation

# Dates must be valid:

# YYYY-MM-DD
# Business Rules
# check_out must be after check_in
# check_in cannot be in the past
# Conflict Detection

# Room cannot already be booked.

# Example:

# Existing

# 10 Jul ---- 15 Jul

# New

# 12 Jul -------- 18 Jul

# Conflict.

# Use overlap logic.

# Response

# Success:

# {
#     "success": True,
#     "message": "Booking created"
# }

# Failure:

# {
#     "success": False,
#     "error": "..."
# }

from datetime import datetime


def create_booking(
    new_booking,
    existing_bookings
):
    
    # Edge cases

    required_fileds=["room","check_in","check_out","guests"]
    for field in required_fileds:
        if field not in new_booking:
            return{
                "success":False,
                "error":f"{field} is required"
            }
        
    
    # guest validation
    guests=new_booking["guests"]
    if not  isinstance(guests,int) or guests<=0:
        return{
            "success":False,
            "error":"guests must be a positive integer"
        }    
    
    # Date validate
    try:
        check_in_date=datetime.strptime(new_booking["check_in"],"%Y-%m-%d")
        check_out_date = datetime.strptime(
            new_booking["check_out"],
            "%Y-%m-%d"
        )
    except ValueError:
        return {
            "success": False,
            "error": "Invalid date format. Use YYYY-MM-DD"
        }
    # Business rules

    if check_out_date <= check_in_date:
        return {
            "success": False,
            "error": "Check-out must be after check-in"
        }
    
     # Conflict detection

    for booking in existing_bookings:
        if booking["room"]!=new_booking["room"]:
            continue

        existing_check_in=datetime.strptime(booking["check_in"],"%Y-%m-%d")
        existing_check_out = datetime.strptime(
            booking["check_out"],
            "%Y-%m-%d"
        )

        has_overlap=check_in_date<existing_check_out and existing_check_in<check_out_date
        if has_overlap:
            return{
                 "success": False,
                "error": "Room already booked for the selected dates"

            }
        
        # main logic
        existing_bookings.append(new_booking)

        # response
        return{
            "success":True,
            "message":"Booking created"
        }


existing_bookings = [
    {
        "room": 101,
        "check_in": "2026-07-10",
        "check_out": "2026-07-15"
    },
    {
        "room": 102,
        "check_in": "2026-07-20",
        "check_out": "2026-07-25"
    }
]

new_booking = {
    "room": 101,
    "check_in": "2026-07-12",
    "check_out": "2026-07-18",
    "guests": 2
}

result = create_booking(
    new_booking,
    existing_bookings
)

print(result)














