time24 = input("Enter time (24-hour format): ")
hours, minutes = time24.split(":")

hours = int(hours)
if hours == 0:
    time12 = f"12:{minutes}am"
elif hours < 12:
    time12 = f"{hours}:{minutes}am"
elif hours == 12:
    time12 = f"12:{minutes}pm"
else:
    time12 = f"{hours - 12}:{minutes}pm"

print(f"Time in 12-hour format: {time12}")