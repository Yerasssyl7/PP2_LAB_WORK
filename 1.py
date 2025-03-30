import re

s = input()

pattern = r"^ab*$"

if re.fullmatch(pattern, s):
    print("Match found")
else:
    print("No match")