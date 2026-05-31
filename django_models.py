from django import models

class Room(models.model):
    name=models.CharField(max_length=100)
    price=models.DelimalFiled(max_digit=8,delimal_places=2)
    is_active=models.BooleanField(default=True)


# ForeignKey — দুই table এর সম্পর্ক

class Booking(models.model):
    user=models.Foreignkey(User,on_delete=models.CASCADE)   #on_delete=models.CASCADE মানে — user delete হলে তার সব booking-ও delete হবে।
    room=models.foreignkey(room,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()



# Meta class — table এর behavior control করে

class Booking(models.model):
    created_at=models.DAteTimeFiled(auto_now_add=True)
    class Meta:
        ordering=["created_at"]   # নতুনটা আগে আসবে
        db_table="bookings"         # table এর নাম
        unique_together=['room','check_in']   # duplicate রোধ করে

              


# ORM Queries
# সব confirmed booking
Booking.objects.filter(status="confirmed")

# একজন user এর booking
Booking.objects.filter(user=request.user)

# নির্দিষ্ট booking খোঁজো, না পেলে 404
from django.shortcuts import get_obj_or_404
booking=get_object_or_404(Booking,pk=booking_id,user=request.user)

# Booking conflict detection

Booking.objects.filter(room_id=room_id,
                      status="confirmed",
                      check_in__lt=check_out,
                      check_out__gt=check_in).exists()