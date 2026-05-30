def cancel_booking(booking,user):
    if booking["status"]=="completed":
        return "completed booking cannot be cancelled"
    
    if user["is_admin"]:
        return "booking cancelled"
    if booking["user_id"]==user["id"]:
        return "booking cancelled"
    
    return "permission denied"

booking = {
    "id": 10,
    "user_id": 5,
    "status": "pending"
}

user = {
    "id": 7,
    "is_admin": False
}