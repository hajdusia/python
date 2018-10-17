#!/usr/bin/python

line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore" \
       "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
       "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum" \
       " dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui" \
       " officia deserunt mollit anim id est laborum."

words = line.split()
first_letters = [word[0] for word in words]
last_letters = [word[-1] for word in words]

print("First letters: " + "".join(first_letters))
print("Last letters: " + "".join(last_letters))
