#string = "P@ssw0rd"
string="password"
listStr = list(string)

for idx in range(0,len(listStr)):
    if listStr[idx].lower() in "aeiou":
        listStr[idx] = "*"
print("".join(listStr))







