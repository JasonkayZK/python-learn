import re
pattern = r"gr(a|e)y"

if re.match(pattern, "gray"):
	print("Match 1")
if re.match(pattern, "grey"):
	print("Match 2")
if re.match(pattern, "griy"):
	print("Match 3")

