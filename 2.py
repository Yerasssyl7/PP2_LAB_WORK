import re

s = input()

pattern = r"^ab{2,3}$"
if re.fullmatch(pattern, s):
    print("Match found")
else:
    print("No match")