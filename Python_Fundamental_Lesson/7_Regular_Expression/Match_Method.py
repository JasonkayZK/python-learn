import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausagespam")
if match:
	print(match)
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())


