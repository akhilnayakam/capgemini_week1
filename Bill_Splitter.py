def bill_split(bill, count, tip):
    total = bill + (tip/100 * bill)
    return total / count

def main():
    bill_amount = int(input("Enter the bill amount:"))
    count_of_people = int(input("Enter the count of people:"))
    tip_percentage = int(input("Enter the Tip Percentage:"))
    print(f"Each person's amount:{bill_split(bill_amount, count_of_people, tip_percentage)}")

main()

