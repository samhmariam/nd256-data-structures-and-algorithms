"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Create a dictionary to store the total time spent on the phone for each telephone number
phone_times = {}

# Iterate over calls to calculate the total time spent on the phone for each number
for call in calls:
    if call[0] in phone_times:
        phone_times[call[0]] += int(call[3])
    else:
        phone_times[call[0]] = int(call[3])
    
    if call[1] in phone_times:
        phone_times[call[1]] += int(call[3])
    else:
        phone_times[call[1]] = int(call[3])

# Find the telephone number that spent the longest time on the phone
max_time = max(phone_times.values())
max_number = [number for number, time in phone_times.items() if time == max_time][0]

print(f"{max_number} spent the longest time, {max_time} seconds, on the phone during September 2016.")

