import re

# * Metacharacter
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")

# * Metacharacter (A better one)
pattern = r"(spam)*egg"

if re.match(pattern, "spambaconegg"):
    print("Match 1")
if re.match(pattern, "spamegg"):
    print("Match 2")
if re.match(pattern, "spamspamegg"):
    print("Match 3")
if re.match(pattern, "egg"):
    print("Match 4")


# + Metacharacter
pattern = r"(g)+"

if re.match(pattern, "g"):
    print("Match 1")
if re.match(pattern, "ggggg"):
    print("Match 2")
if re.match(pattern, "abc"):
    print("Match 3")

# ? Metacharacter
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")
if re.match(pattern, "icecream"):
    print("Match 2")
if re.match(pattern, "sausage"):
    print("Match 3")
if re.match(pattern, "ice--ice"):
    print("Match 4")

# { } Metacharacter
pattern = r"(9){1, 3}$"

if re.match(pattern, "9"):
    print("Match 1")
if re.match(pattern, "999"):
    print("Match 2")
if re.match(pattern, "9999"):
    print("Match 3")
if re.match(pattern, "99955"):
    print("Match 4")
