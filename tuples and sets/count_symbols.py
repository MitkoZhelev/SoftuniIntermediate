input_words = input("Enter words: ")
unique_letters = {}


for letter in input_words:
    if letter not in unique_letters:
        unique_letters[letter] = 0
    unique_letters[letter] += 1

print("\n".join(f"{key}: {value}" for key, value in sorted(unique_letters.items())))