def generate_pattern(n, reverse=False):
    if reverse:
        for i in range(1, n + 1):
            print("*" * (n - i + 1))
    else:
        for i in range(1, n + 1):
            print("*" * i)

def main():
    while True:
        n = input("Enter the number of rows for the pattern: ")
        if n.isdigit():
            n = int(n)
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    
    reverse_choice = input("Do you want the pattern in reverse? (yes/no): ").strip().lower()
    reverse = reverse_choice == "yes"
    generate_pattern(n, reverse)

main()
