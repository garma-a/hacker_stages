#manula way
sample_list = ["mohamed" , "abdo" , "garma"]
mx=0
result =""
for item in sample_list:
    if len(item)>mx:
        mx=len(item)
        result=item
print(result)
#python way
print(max(sample_list, key=len))
