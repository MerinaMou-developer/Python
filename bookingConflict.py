def check_overlap(start1,end1,start2,end2):
    if start1<end2 and start2<end1:
        print("overleap")
    else:
        print("No overleap")


# Short way — one line e!
def check_overlap(start1, end1, start2, end2):
    return start1 < end2 and start2 < end1

check_overlap(10, 12, 11, 13) 
check_overlap(10, 11, 11, 13) 
check_overlap(9, 10, 10, 12)  