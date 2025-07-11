# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

n = int(input())
s = input()

throw_stone = 0
for _ in range(n - 1):
    if s[_] == s[_ + 1]:
        throw_stone += 1
print(throw_stone)