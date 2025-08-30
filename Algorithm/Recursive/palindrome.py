def generate_palindromes(alphabet, n):
    results = [[] for _ in range(n + 1)]  # List of lists for each length

    def recursive(word):
        length = len(word) # length word
        if length > n: # condition
            return 
        results[length].append(word) # Append to list
        print(f"Generating word: '{word}'") 
        for letter in alphabet: 
            new_word = letter + word + letter
            print(f"{letter} + {word} + {letter} => {new_word}")
            recursive(new_word)
    recursive("")
    for letter in alphabet:
        recursive(letter)

    return results

def save_to_file(filename, palindrome_list):
    with open(filename, "w", encoding="utf-8") as f:
        for length, words in enumerate(palindrome_list):
            f.write(f"Length {length}: {', '.join(words)}\n")
    print(f"Palindromes saved in '{filename}'")

if __name__ == "__main__":
    alphabet = input("Enter the alphabet: ").strip()
    n = int(input("Enter the maximum word length: "))
    
    palindromes = generate_palindromes(alphabet, n)
    save_to_file("Palindromes.txt", palindromes)

# Reglas 
# R1: {a,b}E Palindrome
# R2: ^ E Palindrome
# R3: Si xE Palindrome those
# a) axa E Palindrome
# b) bxb E Palindrome
# R4: Cualquier palabra solamente se genera con las reglas anteriores 