string = input("enter string : ")
l , r = 0 , len(string) - 1
while l < r:
    if string[l] != string[r]:
        print("Not Palindrome")
        exit(0)
    l += 1
    r -= 1
print("Palindrome")

