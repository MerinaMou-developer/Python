# Rules:

# User must be logged in
# Admin can edit
# Owner can edit
# Completed booking cannot be edited
# Return API-style response


booking = {
    "id": 1,
    "user_id": 5,
    "status": "confirmed"
}

current_user = {
    "id": 7,
    "is_admin": False
}

def edit_booking(
    booking,
    current_user
):

    # Authentication

    if current_user is None:
        return {
            "success": False,
            "error": "Authentication required"
        }

    # Edge Case

    if booking is None:
        return {
            "success": False,
            "error": "Booking not found"
        }

    # Business Rule

    if booking["status"] == "completed":
        return {
            "success": False,
            "error": "Completed booking cannot be edited"
        }

    # Authorization

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

    booking["status"] = "updated"

    return {
        "success": True,
        "message": "Booking edited successfully"
    }