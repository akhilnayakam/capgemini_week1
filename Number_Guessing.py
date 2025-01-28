import random

def guess_number(num):
    for i in range(5):
        guess = int(input("Guess the number:"))
        if guess == num:
            print("Congratulations!, You are Successfully guessed the number bro!")
            break
        elif abs(guess - num) <= 10:
            print("You are very near bro!")
        elif abs(guess - num) > 10 and abs(guess - num) <= 20:
            print("You are near bro!")
        elif abs(guess - num) > 20 and abs(guess - num) <= 40:
            print("You are far bro")
        else:
            print("You are too far bro!")

def generate_random():
    num = random.randrange(1, 100)
    print(num)
    return num

def main():
    num = generate_random()
    print("You have five attempts to guess the number bro!")
    guess_number(num)
    
main()