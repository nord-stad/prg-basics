###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600  # 1 km = 1000 m, 1 h = 3600 s
speed_ms_round = round(speed_ms, 2)  # rounded to 2 decimal places
print("Speed without rounding:", speed_kmh, "km/h =", speed_ms, "m/s")
print("Speed with rounding:", speed_kmh, "km/h =", speed_ms_round, "m/s")