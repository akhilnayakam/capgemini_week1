def is_Prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    while True:
        lower = int(input("Enter the lower limit:"))
        upper = int(input("Enter the upper limit:"))
        if (lower > 0 and upper > 0) and lower < upper:
            while lower <= upper:
                if is_Prime(lower):
                    print(lower)
                lower += 1
            break
        else:
            print("Wrong input!, Enter valid input")
        
main()
