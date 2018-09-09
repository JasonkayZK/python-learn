import re

pattern = r"spam"

print(re.match(pattern, "spam123"))

if re.match(pattern, "spamspamspam"):
	print("Match")
else:
	print("No match")


