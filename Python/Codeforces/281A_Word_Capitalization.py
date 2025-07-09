# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

def solution(a):
    letter_capitalized = a[0].capitalize()
    new_word = letter_capitalized + a[1:]
    return new_word
a = input()
print(solution(a))

# Another more streamlined solution

a = input()
print(a[0].upper() + a[1:])