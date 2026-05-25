def get_available_slots(all_slots,booked_slots):
    available_slots = []

    for slot in all_slots:
        if slot not in booked_slots:
            available_slots.append(slot)

        
    return available_slots




all_slots = [
    {"id": 1, "start": 9,  "end": 10},
    {"id": 2, "start": 10, "end": 11},
    {"id": 3, "start": 11, "end": 12},
    {"id": 4, "start": 12, "end": 13},
]

booked_slots = [
    {"id": 2, "start": 10, "end": 11},
    {"id": 4, "start": 12, "end": 13},
]


print(get_available_slots(all_slots,booked_slots))
