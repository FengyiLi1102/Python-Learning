import time

min = 60
hour = 60 * min
day = 24 * hour

current_time = time.time()

day_to_epoch = int(current_time // day)
left_time = current_time % day
hours = int(left_time //hour)
left_time = left_time % hour
mins = int(left_time // min)
seconds = int(left_time % min)

print('Time is ', day_to_epoch, ' days ', hours, ' hours ', mins, ' minutes and ', seconds, ' seconds to the epoch.')