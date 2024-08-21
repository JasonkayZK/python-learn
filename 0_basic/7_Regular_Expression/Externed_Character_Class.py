import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")
if re.search(pattern, "E3"):
    print("Match 2")
if re.search(pattern, "1ab"):
    print("Match 3")
