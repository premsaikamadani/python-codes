arr = [3, 5, 9, 10, 12, 7]
count = 0
for num in arr:
    if num % 3 == 0:
        count = count + 1

print("Count of numbers divisible by 3:", count)