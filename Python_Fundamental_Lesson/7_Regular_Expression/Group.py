import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
	print("Match 1")
if re.match(pattern, "eggspamspamspamegg"):
	print("Match 2")
if re.match(pattern, "spam"):
	print("Match 3")

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
	print(match.group())
	print(match.group(0))
	print(match.group(1))
	print(match.group(2))
	print(match.groups())



