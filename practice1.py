# cancel booking

# Rules:

# Object Permission
# Owner can cancel
# Admin can cancel
# Others cannot
# Business Rule
# Completed booking cannot be cancelled

booking = {
    "id": 1,
    "user_id": 5,
    "status": "confirmed"
}

current_user = {
    "id": 7,
    "is_admin": False
}


def cancel_booking(
    booking,
    current_user
):

    # Edge Cases

    if booking is None:
        return {
            "success": False,
            "error": "Booking not found"
        }

    if current_user is None:
        return {
            "success": False,
            "error": "Authentication required"
        }

    # Business Rule

    if booking["status"] == "completed":
        return {
            "success": False,
            "error": "Completed booking cannot be cancelled"
        }

    # Permission Check

    is_owner = (
        booking["user_id"]
        ==
        current_user["id"]
    )

    is_admin = (
        current_user["is_admin"]
    )

    if not (is_owner or is_admin):
        return {
            "success": False,
            "error": "Permission denied"
        }

    # Main Logic

    booking["status"] = "cancelled"

    # Response

    return {
        "success": True,
        "message": "Booking cancelled"
    }