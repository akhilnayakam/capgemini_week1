def count_words(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word: 
        words.append(current_word)

    word_counts = {}
    for word in words:
        word = word.lower() 
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def main():
    sentence = input("Enter a sentence: ")
    word_counts = count_words(sentence)
    
    print("Word occurrences:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

main()
