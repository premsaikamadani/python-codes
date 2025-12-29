arr = [8, 4, 6, 2, 9]
min_num = arr[0]
for num in arr:
    if num < min_num:
        min_num = num
print("Minimum number in the list:", min_num)