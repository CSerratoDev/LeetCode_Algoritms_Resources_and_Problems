# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

a = input().lower()
b = input().lower()

if a < b:
    print("-1")
elif a > b:
    print("1")
else:
    print("0")

#Ternary version
a = input().lower()
b = input().lower()
print(-1 if a < b else 1 if a > b else 0)