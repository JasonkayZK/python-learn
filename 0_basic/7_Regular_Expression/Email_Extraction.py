import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

str1 = "Please contact info@sololearn.com for assistance.\n"
str2 = "Please contact 271226192@qq.com for more infomation."

match = re.search(pattern, str1)
if match:
    print(match.group())

match = re.search(pattern, str2)
if match:
    print(match.group())

str = str1 + str2
print(str)
match = list(re.findall(pattern, str))
if match:
    for str in match:
        print(str[0] + "@" + str[1] + str[2])
