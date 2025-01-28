def generate_multiplication_table(number, start, end):
    print(f"\nMultiplication Table for {number} (from {start} to {end}):")
    for i in range(start, end + 1):
        print(f"{number} x {i} = {number * i}")

def main():
    print("Welcome to the Multiplication Table Generator!")
    
    number = int(input("Enter the number for which you want the multiplication table: "))
    
    start = int(input("Enter the starting range: "))
    end = int(input("Enter the ending range: "))
    
    if start > end:
        print("Invalid range. The starting range must be less than or equal to the ending range.")
    else:
        generate_multiplication_table(number, start, end)

main()
