def is_palindrome(inputt):
    left, right = 0, len(inputt) - 1
    while left <= right:
        if inputt[left] != inputt[right]:
            return False
        left += 1
        right -= 1
    return True

def get_input_and_check():
    limit = int(input("Enter the limit:"))
    i = 0
    while limit != 0:
        s = input(f"Enter the input{i+1}:")
        if is_palindrome(s):
            print("Palindrome")
        else:
            print("Not Palindrome")
        limit -= 1
        i += 1

def main():
    get_input_and_check()

main()