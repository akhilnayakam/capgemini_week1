def calculate_factorial(num):
    if num == 0 or num == 1:
        return 1
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def main():
    while True:
        num = int(input("Enter the input:"))
        if num >= 0:
            print(f"Factoraial of {num}:", calculate_factorial(num))
            break
        else:
            print("Wrong input, try again!")

main()
