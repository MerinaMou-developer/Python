from django.db import transaction


with transaction.atomic():

    room = Room.objects.select_for_update().get(
        id=room_id
    )

    if room.available_rooms <= 0:

        raise Exception(
            "No rooms available"
        )

    Booking.objects.create(
        room=room,
        user=request.user
    )

    room.available_rooms -= 1

    room.save()