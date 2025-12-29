s = "infosys"
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Count of vowels in the string:", count)
