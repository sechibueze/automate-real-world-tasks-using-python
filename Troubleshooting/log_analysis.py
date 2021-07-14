import re
import operator
# Regex
log_line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
pattern = r"ticky: INFO: ([\w ]*) "
result = re.search(pattern, log_line)
# print('Result ', result)

# Sorting
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
# Sort by key name of Dict
# sorted_fruit = sorted(fruit.items())
# Use operator to sort by key
# sorted_fruit = sorted(fruit.items(), key=operator.itemgetter(0))

# Use operator to sort by values
sorted_fruit = sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)

print('Fruits has been sorted')
print(sorted_fruit)