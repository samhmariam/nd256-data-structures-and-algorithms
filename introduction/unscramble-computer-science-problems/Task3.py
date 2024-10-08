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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
# Find all of the area codes and mobile prefixes called by people in Bangalore
# Create a set to store the codes
codes = set()

# Iterate over calls to find the codes
for call in calls:
    if call[0].startswith('(080)'):
        if call[1].startswith('(0'):
            # Fixed line number
            code = call[1].split(')')[0][1:]
            codes.add(code)
        elif call[1].startswith(('7', '8', '9')):
            # Mobile number
            code = call[1][:4]
            codes.add(code)
        elif call[1].startswith('140'):
            # Telemarketer number
            codes.add('140')

# Print the list of codes in lexicographic order
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes):
    print(code)

# Part B
# Calculate the percentage of calls from fixed lines in Bangalore to other fixed lines in Bangalore
total_calls = 0
bangalore_calls = 0

# Iterate over calls to count the total and Bangalore calls
for call in calls:
    if call[0].startswith('(080)'):
        total_calls += 1
        if call[1].startswith('(080)'):
            bangalore_calls += 1

# Calculate the percentage
percentage = (bangalore_calls / total_calls) * 100

# Print the percentage of calls to other fixed lines in Bangalore
print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

