def get_input():
    salary = float(input("Enter the salary:"))
    age = int(input("Enter the age:"))
    credit_score = int(input("Enter the credit score:"))
    return (salary, age, credit_score)

def check_loan_eligibility(salary, age, credit_score):
    reasons = []
    eligible = True

    if salary < 20000:
        reasons.append("Salary is below the minimum requirement of 20,000.")
        eligible = False
    if age < 21 or age > 60:
        reasons.append("Age is outside the eligible range (21-60 years).")
        eligible = False
    if credit_score < 650:
        reasons.append("Credit score is below the minimum requirement of 650.")
        eligible = False

    if eligible:
        print("\nLoan Approved: You meet all the eligibility criteria.")
    else:
        print("\nLoan Rejected: Reasons for rejection:")
        for reason in reasons:
            print(f"- {reason}")

def main():
    print("Welcome to the Bank Loan Eligibility Checker!")
    
    (salary, age, credit_score) = get_input()
    
    check_loan_eligibility(salary, age, credit_score)

main()
