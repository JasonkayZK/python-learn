import re

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")
if re.search(pattern, "AbCd123"):
    print("Match 2")
if re.search(pattern, "THISISALL"):
    print("Match 3")
