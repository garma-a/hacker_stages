sample_list  = [1,1,1,2,2,3,3,3,3,3]
print(list(set(sample_list)))   # one line solution

# the manual way
unique_list = []
for item in sample_list:
    if item not in unique_list:
        unique_list.append(item)
