# Rules:

# Object-Level Permission->
# User can see only their own profile
# Admin can see any profile

# Sensitive Data->
# password_hash
# api_key

# Never return:
# Allowed Response
# {
#     "id": 1,
#     "name": "Mou",
#     "email": "mou@gmail.com"
# }
# Return Error
# {
#     "success": False,
#     "error": "Permission denied"
# }


user = {
    "id": 1,
    "name": "Mou",
    "email": "mou@gmail.com",
    "password_hash": "abc123",
    "api_key": "secret-key",
    "is_admin": True
}

current_user = {
    "id": 2,
    "is_admin": False

}


def get_profile(
    user,
    current_user
):
    
    # edge cases
    if current_user is None:
        return {
            "success": False,
            "error": "Authentication required"
        }
    
    required_filed=["id","email","name"]

    for field in required_filed:
        if field not in user:
            return {
            "success": False,
            "error": "Authentication required"
        }

    if (user["id"]==current_user["id"]):
        return{
             "success": True,
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]

        }
    
    return{
        "success": False,
        "error": "Permission denied"
    }
    



    

        

    
    