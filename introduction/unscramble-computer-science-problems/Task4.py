"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create sets to store numbers that make outgoing calls but never send texts, receive texts or receive incoming calls
outgoing_calls = set()
incoming_calls = set()
outgoing_texts = set()
incoming_texts = set()

# Iterate over calls and texts to extract numbers that make outgoing calls, receive incoming calls, send texts, and receive texts
for call in calls:
    outgoing_calls.add(call[0])
    incoming_calls.add(call[1])

for text in texts:
    outgoing_texts.add(text[0])
    incoming_texts.add(text[1])

# Find numbers that make outgoing calls but never send texts, receive texts or receive incoming calls
telemarketers = outgoing_calls - (incoming_calls | outgoing_texts | incoming_texts)

# Print the list of possible telemarketers in lexicographic order
print("These numbers could be telemarketers: ")
for number in sorted(telemarketers):
    print(number)






