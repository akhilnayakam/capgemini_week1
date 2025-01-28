def odd(nums):
    odd_list = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            odd_list.append(nums[i])

    return odd_list

def even(nums):
    even_list = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even_list.append(nums[i])

    return even_list

def main():
    print("Enter the list of numbers:", end="")
    nums = list(map(int, input().split()))
    print(f"Odd List:{odd(nums)}")
    print(f"Even List:{even(nums)}")

main()