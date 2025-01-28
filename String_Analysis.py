def analyze_string(s):
    vowels = "aeiouAEIOU"
    digits = "1234567890"
    special = "!@#$%^&*()<>?\"'"
    consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    vowel_count = consonant_count = digit_count = special_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in digits:
            digit_count += 1
        elif char in special:
            special_count += 1
        elif char in consonants:
            consonant_count += 1
    
    print("Number of Vowels:", vowel_count)
    print("Number of Consonants:", consonant_count)
    print("Number of Special Characters:", special_count)
    print("Number of Digits:", digit_count)

def reverse_string(s):
    return s[::-1]

def main():
    string = input("Enter the String:")
    analyze_string(string)
    print("Reversed String:", reverse_string(string))

main()