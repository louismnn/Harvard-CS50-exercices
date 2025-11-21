email = input("What's your email? ").strip()
# strip() is use to remove some character, default remove whitespce

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
# This code have lots of problem because it's easy to cheat

username, domain = email.split("@")
# split() is to split
if username and domain.endswith(".com"):
# endwith() is the end of the string
    print("Valid")
else:
    print("Invalid")

# library "re" is good to replace, use, change patterns
import re

# re.search(pattern, string, flags=0)
if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

# But the problem is that we want @, something to the right, something to the left and 
# the thing to the right need to finish by .com
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

# ^ matches the start of the string
# $ matches the end of the string or just before 
# the newline at the end of the string

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# [] set of characters
# [^] complementing the set
if re.search(r"^[^@]+@+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


if re.search(r"^[a-zA-Z0-9_]+@+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace character
# \w word character … as well as numbers and the underscore
# \W not a word character

if re.search(r"^w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")