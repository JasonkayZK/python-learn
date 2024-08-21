import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")
if re.search(pattern, "qwertyuiop"):
    print("Match 2")
if re.search(pattern, "rhythm myths"):
    print("Match 3")
