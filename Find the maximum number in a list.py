nums = [10, 3, 25, 7]
#Step 1: Restate (Speak this in interview)
#“We need to find the largest number from a list of integers.”

#Step 2: Think in English
# Assume the first number is the maximum
# Compare it with every other number
# If a number is bigger, update max
# Return max

# Step 3: Tools Needed
# variable
# for loop
# if conditio


def find_max(nums):
    max_num = nums[0]

    for n in nums:
        if n > max_num:
            max_num = n

    return max_num
