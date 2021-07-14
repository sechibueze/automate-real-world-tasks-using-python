#!/usr/bin/env python3
# Import required modules
import operator
import re
import csv

# Initialize variables
error_messages = {}
user_stats = {}
user_error = {}

# Set patterns for getting data
username_pattern = r'\([a-zA-Z.]*\)$'
error_line_pattern = r"ticky: ERROR ([\w \']*) "

# Parse the log file
logs = open('./syslog.log', 'r')
for line in logs.readlines():
    if re.search(error_line_pattern, line.strip()):
        # This line has error
        error_message = re.search(error_line_pattern, line).group().split('ERROR ')[1].strip()
        # Populaate the errors in the dictionary
        if error_message in error_messages:
            error_messages[error_message] = error_messages.get(error_message) + 1
        else:
            error_messages[error_message] = 1
        # Get user wiyth error
        group = re.search(username_pattern, line).group()
        username = group[1:-1]
        if username in user_error:
            user_error[username] = user_error.get(username) + 1
        else:
            user_error[username] = 1
    else:
        if re.search(username_pattern, line):
            group = re.search(username_pattern, line).group()
            username = group[1:-1]
            # print(group , " => ", username)
            if username in user_stats:
                user_stats[username] = user_stats.get(username) + 1
            else:
                user_stats[username] = 1

i = set(user_stats.keys())
e=set(user_error.keys())
z = e-i
d=dict.fromkeys(z, 0)
user_stats.update(d)



# Sort the errors and user_stats by value from most to less
# print(user_stats)
user_stats = sorted(user_stats.items(), key=operator.itemgetter(0), reverse=False)
user_error = sorted(user_error.items(), key=operator.itemgetter(0), reverse=False)
error_messages = sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)


print(user_stats)
print(user_error)

# Add headings to the list
error_messages.insert(0, ("Errors", "Count"))
# user_stats.insert(0, ("Username", "INFO"))
# user_error.insert(0, ("Username", "ERROR"))

#

result = [["Username", "INFO", "ERROR"]]
rec = dict(user_stats)
print('u err', rec)
for row in user_error:
    username = row[0]
    error_count = row[1]
    info_count = rec[username]
    data_row = [username, info_count, error_count]
    result.append(data_row)

print('res ', result)
with open('user_statistics.csv', 'w', newline='') as usage_file:
    writer = csv.writer(usage_file)
    writer.writerows(result)

# Write to file

with open('error_message.csv', 'w', newline='') as error_file:
    writer = csv.writer(error_file)
    writer.writerows(error_messages)
