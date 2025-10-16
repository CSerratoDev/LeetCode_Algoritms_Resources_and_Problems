"""
El propósito de un autómata finito es procesar una cadena símbolo del alfabeto por símbolo del alfabeto hasta consumir toda la cadena;
dependiendo en qué estado se encuentra se determina si la cadena se acepta.
"""

from sys import stdin

def readLine():
    return stdin.readline().strip()

def readArray():
    return readLine().split()

def readTransitions():
    transitions = {}

    while True:
        response = input("Enter another transition? (y/n): ").strip().lower()
        
        if response == "y":
            print("Enter new transition: ")
            data = readLine() #Lee la transicion
                
            if ":" not in data or "," not in data:
                print("Invalid format. Use: q1, a : q2")
                continue

            left, right = data.split(":") #Separa por clave (izq) y valor (der)
            state, symbol = [x.strip() for x in left.split(",")] #Limpia espacios y divide la parte izquierda en dos valores
            new_state = right.strip() #limpia el valor derecho

            transitions[(state, symbol)] = new_state 
            print(f"Added transition: δ:({state}, {symbol})-> {new_state}")
        elif response == "n":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 'y' or 'n'.")
    return transitions

def main():
    print("Deterministic Finite Automaton")
    print(f"Enter the states, example: q1 q2 q3")
    states = readArray()
    print(f"Enter the alphabet, example: a b")
    alphabet = readArray()
    print(f"Enter the initial state, example: q0")
    start_state = readArray()
    print(f"Enter the final state, example: q4")
    final_state = readArray()
    print(f"Enter transitions, example: q1, a : q2")
    transitions = readTransitions()
    print("States: ", states)
    print("Alphabet: ", alphabet)
    print("Start State: ", start_state)
    print("Final State: ", final_state)
    print("Transitions: ", transitions)

if __name__ == '__main__':
    main()