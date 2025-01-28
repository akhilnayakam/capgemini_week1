def second_largest(nums):
    largest = nums[0]
    second = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    for i in range(len(nums)):
        if nums[i] > second and nums[i] < largest:
            second = nums[i]
    return second

print("Enter the numbers in the list:", end="")
nums = list(map(int, input().split()))
print(f"Second Largest is:{second_largest(nums)}")