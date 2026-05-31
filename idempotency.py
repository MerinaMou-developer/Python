# Write a function:

# create_booking(
#     booking_id,
#     idempotency_key
# )

# Requirements:

# 1. Same booking should not be created twice.
# 2. If the same idempotency key is received again,
#    return duplicate request error.
# 3. Return API-style response.


processed_key=set()

def create_order(user_id,idempotency_key):
    if idempotency_key in processed_key:
        return{
            "success":False,
            "error":"duplicate request already processed"
        }
    processed_key.add(idempotency_key)
    return{
        "success":True,
        "message":"order created"
    }


create_order(
    1,
    "abc123"
)



