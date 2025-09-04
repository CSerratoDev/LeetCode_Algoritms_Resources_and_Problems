from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def readInts():
	return list(map(int, readLine().split()))

'''OPTION A'''
import os

def generar_palabras(alfabeto, n, palabra="", resultado=None):
    if resultado is None:
        resultado = []
    if len(palabra) <= n:
        if palabra.count("a") % 2 == 0 and palabra.count("b") % 2 == 0:
            resultado.append(palabra)
    if len(palabra) == n:
        return resultado
    for simbolo in alfabeto:
        generar_palabras(alfabeto, n, palabra + simbolo, resultado)
    return resultado
'''END OPTION A'''

'''OPTION B'''
def generate_palindromes(alphabet, n):
    results = [[] for _ in range(n + 1)]  # List of lists for each length

    def recursive(word):
        length = len(word) # length word
        if length > n: # condition
            return
        if length > 0 and word[0] == "a" in word and word.endswith("b"):
            results[length].append(word)
        print(f"Generating word: '{word}'") 
        for letter in alphabet:
            if word == "":
                recursive("ab")
                recursive("a" + letter + "b")
            else:
                new_word = "a" + letter + word + letter + "b"
                print(f"a + {letter} + {word} + {letter} + b => {new_word}")
                recursive(new_word)

    recursive("")
    for letter in alphabet:
        recursive(letter)
        
    return results
'''END OPTION B'''

'''TOOLS'''
def save_to_file(filename, palindrome_list):
    with open(filename, "w", encoding="utf-8") as f:
        for length, words in enumerate(palindrome_list):
            f.write(f"Length {length}: {', '.join(words)}\n")
    print(f"Palindromes saved in '{filename}'")


'''OPTION C'''
def es_palindromo(palabra):
    return palabra == palabra[::-1]

def parse_alphabet(s):
    s = s.strip()
    if not s:
        return []
    if "," in s or " " in s:
        return [p for chunk in s.split(",") for p in chunk.strip().split() if p]
    return list(s)

def generar_no_palindromos(alfabeto, n):
    by_len = {k: [] for k in range(n+1)}
    def rec(actual):
        if len(actual) > n:
            return
        if 0 < len(actual) <= n and not es_palindromo(actual):
            by_len[len(actual)].append(actual)
        if len(actual) < n:
            for letra in alfabeto:
                rec(actual + letra)
    rec("")
    return by_len


'''END OPTION C'''

def recursive_a():
    alfabeto = ["a", "b"]
    print("Length: ")
    n = readInt()
    palabras = generar_palabras(alfabeto, n)
    
    palabras.sort(key=lambda x: (len(x), x))
    
    print("Palabras generadas:")
    for p in palabras:
        print(f"Longitud {len(p)}: {p if p != '' else 'ε'}") 
    
    ruta = os.path.abspath("PalindromeA.txt")
    with open(ruta, "w") as f:
        for p in palabras:
            f.write(f"Longitud {len(p)}: {p if p != '' else 'ε'}\n")
    
    print("\nArchivo guardado en:", ruta)

def recursive_b():
    print("Alphabet: ")
    alphabet = readLine() #alphabet
    print("Length: ")
    n = readInt() #length
    palindromes = generate_palindromes(alphabet, n) #recursive
    return save_to_file("PalindromesB.txt", palindromes) #.txt

def recursive_c():
    print("Alphabet: ")
    alfabeto = parse_alphabet(readLine()) 
    print("Length: ")
    n = readInt()
    by_len = generar_no_palindromos(alfabeto, n)
    with open("NoPalindromeC.txt", "w", encoding="utf-8") as f:
        for L in range(n+1):
            if L == 0:
                print("Longitud 0: E")
                f.write("Longitud 0: E\n")
            else:
                palabras = sorted(by_len[L])
                linea = f"Longitud {L}: {' '.join(palabras)}"
                print(linea)
                f.write(linea + "\n")

def option(n):
    if n == 1:
        print("Exercise A")
        recursive_a()
        return True
    elif n == 2:
        print("Exercise B")
        recursive_b()
        return True
    elif n == 3:
        print("Exercise C")
        recursive_c()
        return True
    elif n == 4:
        print("See you")
        return False
    else:   
        return "Invalid option"

def main():
    user = True
    while user:
        print("Select an Exercise")
        print("Option 1: A")
        print("Option 2: B")
        print("Option 3: C")
        print("Option 4: Exit")
        n = readInt()
        user = option(n)
    print("Finish")
    
if __name__ == "__main__":
    main()

# Reglas 
# R1: {a,b}E Palindrome
# R2: ^ E Palindrome
# R3: Si xE Palindrome those
# a) axa E Palindrome
# b) bxb E Palindrome
# R4: Cualquier palabra solamente se genera con las reglas anteriores 