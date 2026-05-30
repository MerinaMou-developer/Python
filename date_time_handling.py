# Interviewer সাধারণত ৫টা জিনিস check করে:

# 1. Date format validation
# 2. Future/Past date validation
# 3. Date comparison
# 4. Duration calculation
# 5. Time window validation


# 1. valid date
from datetime import datetime
try:
 datetime.strptime("2026-07-15","%Y-%m-%d")

except ValueError:
 print("invalid date")


# 2. Future date

booking_date=datetime.strptime("2026-08-15", "%Y-%m-%d")

today=datetime.today()
if booking_date.date() < today.date():
    print("Booking date cannot be in the past.")



#3. Date Comparison

# if check_out <= check_in:
#     return "Invalid booking period"


#4. Duration
# Booking cannot exceed 30 days

days=(check_out-check_in).days

if days>30:
  print("Booking cannot exceed 30 days")



# 5: Time Window
# Booking can be cancelled
# at least 1 hour before start.

from datetime import datetime, timedelta

difference = start_time - datetime.now()

if difference < timedelta(hours=1):
    return "Too late to cancel"

