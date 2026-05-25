


def find_conflicts(existing,new):
    for booking in existing:
        if booking["start"]<new["end"] and new["start"]<booking["end"]:
            return True
    return False




existing = [
    {"start": 9, "end": 11},
    {"start": 10, "end": 12},
]
new = {"start": 11, "end": 13}

print(find_conflicts(existing,new))