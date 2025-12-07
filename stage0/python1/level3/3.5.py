numbers = [3,5,1,2,4]
for i in range(0,len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)







