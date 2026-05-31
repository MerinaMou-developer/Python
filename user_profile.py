
# Rules:

# User must be logged in
# Admin can edit
# Owner can edit
# Others cannot edit
# Sensitive data must not be returned
# password_hash
# api_key
# Return API-style response


profile = {
    "id": 5,
    "name": "Mou",
    "email": "mou@gmail.com",
    "phone": "+880123456789",
    "password_hash": "abc123xyz",
    "api_key": "secret-api-key"
}

current_user = {
    "id": 7,
    "is_admin": False
}

def view_profile(
    profile,
    current_user
):
    # authentication
    if current_user is None:
        return{
            "success":False,
            "error":"Authentication required"
        }
    
    # edge cases
    if profile is None:
        return{
            "success":False,
            "error":"profile not found"
        }
    required_fileds=["id","email"]
    for required in required_fileds:
        if required not in profile:
            return{
                "success":False,
                "error":f"{required} is missing"
            }

    # owner and admin can view
    # Authorization

    owner=(current_user["id"]==profile["id"])
    admin=(current_user["is_admin"])

    if not (owner or admin):
        return{
            "success":False,
            "error":"Access Denied"
        }

     # Secure API Response
    # Never return password_hash or api_key

    safe_profile={
        "id":profile["id"],
        "name":profile["name"],
        "email":profile["email"],
        "phone":profile["phone"]
    }

    return{
        "success":True,
        "profile":safe_profile
    }


result = view_profile(
    profile,
    current_user
)

print(result)