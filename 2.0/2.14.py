#!/usr/bin/python

line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore" \
       "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
       "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum" \
       " dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui" \
       " officia deserunt mollit anim id est laborum."

words = line.split()

longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)

print("Longest word: " + longest)
print("Longest word letter count: " + str(len(longest)))
