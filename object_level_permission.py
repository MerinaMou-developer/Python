
# A user can edit only their own booking.

booking = {
    "id": 10,
    "user_id": 5
}

user = {
    "id": 7
}

def can_edit_booking(booking,user):
    return booking["user_id"]==user["id"]


# Users can delete only their own reviews.

review = {
    "id": 1,
    "user_id": 100
}

def can_delete_review(user, review):

    return review["user_id"] == user["id"]



# Admin can edit any order.
# Customers can edit only their own orders.

def can_edit_order(user,order):
    if user["is_admin"]:
        return True
    
    return order["user_id"]==user["id"]



# Users can view only invoices belonging to their company.

# A user can edit only their own booking.

booking = {
    "id": 10,
    "user_id": 5
}

user = {
    "id": 7
}

def can_edit_booking(booking,user):
    return booking["user_id"]==user["id"]


# Users can delete only their own reviews.

review = {
    "id": 1,
    "user_id": 100
}

def can_delete_review(user, review):

    return review["user_id"] == user["id"]



# Admin can edit any order.
# Customers can edit only their own orders.

def can_edit_order(user,order):
    if user["is_admin"]:
        return True
    
    return order["user_id"]==user["id"]



# Users can view only invoices belonging to their company.
user = {
    "company_id": 20
}

invoice = {
    "company_id": 10
}

def can_view_invoice(user,invoice):
    return (user["company_id"]==invoice["company_id"])



# DRF Version

from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self,request,view,obj):
        return obj.user_id==request.user.id