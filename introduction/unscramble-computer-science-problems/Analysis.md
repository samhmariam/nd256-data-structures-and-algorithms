## Task0

**Description**: The problem iterates over a list to print the first and last record. i
**Approach**: Iterated through the list a single time.

**Complexity Analysis**:
- **Algorithm**: Iterate over a list.
- **Big O Notation**: The code runs in constant time $O(1)$ .
- **Justification**: The code only accesses the first and last elements of the texts and calls lists. 


## Task1

**Description**: The problem involves reading the records from texts and calls, extracting unique telephone numbers, and counting the total number of unique telephone numbers. Finally, it prints the count of unique telephone numbers in the specified format.
**Approach**: The code uses a set to store unique numbers and iterates over all the records to extract and add numbers to the set. 

**Complexity Analysis**:
- **Algorithm**: The code reads the records from texts and calls, extracts unique telephone numbers, and counts the total number of unique telephone numbers. 
- **Big O Notation**: The time complexity of this code id $O(n)$ where $n$ is the total number of records in texts and calls.
- **Justification**: The code is efficient in finding the count of unique telephone numbers in the records by using a set to store unique numbers and avoiding duplicates. The time complexity of the code is proportional to the number of records and unique telephone numbers in the input data.

## Task2

**Description**: The problem calculates the total time spent on the phone for each telephone number, and finds the number that spent the longest time on the phone. 
**Approach**: It uses a dictionary to store the total time for each number and then finds the number with the maximum time spent on the phone.

**Complexity Analysis**:
- **Algorithm**:It uses a dictionary to store the total time for each number and then finds the number with the maximum time spent on the phone.
- **Big O Notation**: The time complexity of this code is $O(n)$ where $n$ the total number of calls in the input data.
- **Justification**: The code is efficient in finding the telephone number that spent the longest time on the phone during the period by iterating over the calls and keeping track of the total time for each number. 

## Task3

**Description**: The problem reads the records from calls, identifies the area codes and mobile prefixes called by people in Bangalore, and calculates the percentage of calls made to other fixed lines in Bangalore. 
**Approach**: It uses sets to store the unique codes and counts the total and Bangalore calls to calculate the percentage.

**Complexity Analysis**:
- **Algorithm**:  The code iterates over all the calls to find the area codes and mobile prefixes called by people in Bangalore and count the calls made to other fixed lines in Bangalore.
- **Big O Notation**: The time complexity of this code is $O(n + m log m)$ where $n$ is the total number of calls in the input data and $m$ is the number of unique codes extracted.
- **Justification**: The code efficiently finds the area codes and mobile prefixes called by people in Bangalore by iterating over the calls and filtering the numbers based on the specified criteria.

## Task4

**Description**: The problem reads the records from calls and texts, extracts numbers that make outgoing calls, receive incoming calls, send texts, and receive texts, and finds the numbers that could be telemarketers based on the criteria provided. 
**Approach**: It uses sets to store the numbers and perform set operations to identify the possible telemarketers.

**Complexity Analysis**:
- **Algorithm**: The code iterates over all the calls and texts to extract the numbers that make outgoing calls, receive incoming calls, send texts, and receive texts
- **Big O Notation**: The time complexity of this code is $O(n + m + t log t)$ where $n$ is the number of is the number of calls, $m$ is the number of texts in the input data and $t$ is the number of telemarketers identified.
- **Justification**: The code efficiently identifies the numbers that could be telemarketers by filtering the numbers based on the specified criteria and performing set operations to find the numbers that make outgoing calls but never send texts, receive texts, or receive incoming calls.

