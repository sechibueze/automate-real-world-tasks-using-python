#!/usr/bin/env python3
# Import the required modules
import re
import operator

# Initialize variables
error_messages = {}
user_statistics = {}
logfile =r"syslog.log"
pattern = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"

# Open the logfile
with open(logfile, "r") as logs:
    for line in logs:

        match = re.search(pattern, line)
        if match is None:
            continue

        # Say the logline is of INFO type
        if match.groups()[0].strip().upper() == "INFO":
            log_category = match.groups()[0].strip().upper()
            message = match.groups()[1]
            username = match.groups()[2][1:-1]

            # Update the user's entry in the data
            if username in user_statistics:
                user_data = user_statistics[username]
                user_data[log_category] += 1
            else:
                user_statistics[username] = {"INFO": 1, "ERROR": 0}

        # Say the logline is of ERROR type
        if match.groups()[0] == "ERROR":
            log_category = match.groups()[0].strip().upper()
            error_log_message = match.groups()[1]
            username = match.groups()[2][1:-1]
            error_messages[error_log_message] = error_messages.get(error_log_message, 0) + 1

            if username in user_statistics:
                user_statistics[username][log_category] += 1
            else:
                user_statistics[username] = {"INFO": 0, "ERROR": 1}


# Sort the data
sorted_user_statistics = [("Username", "INFO", "ERROR")]  + sorted(user_statistics.items())
sorted_error_messages = [("Error", "Count")] + sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)
print("User statist")
print("---------------------------")
print(sorted_user_statistics)
print("error messages")
print(sorted_error_messages)

with open("error_message.csv", "w") as error_file:
    for entry in sorted_error_messages:
        error_file.write("{}, {}\n".format(entry[0], entry[1]))

with open("user_statistics.csv", "w") as user_file:
    for line in sorted_user_statistics:
        if isinstance(line[1], dict):
            user_file.write("{}, {}, {}\n".format(line[0], line[1].get("INFO"), line[1].get("ERROR")))
        else:
            user_file.write("{}, {}, {}\n".format(line[0], line[1], line[2]))