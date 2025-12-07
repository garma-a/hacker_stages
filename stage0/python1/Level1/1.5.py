string = "rekcah_repus"
string_list = list(string)

l , r = 0 , len(string)-1

while l<r:
    string_list[l] , string_list[r] = string_list[r] , string_list[l]
    l+=1
    r-=1

print("".join(string_list))







