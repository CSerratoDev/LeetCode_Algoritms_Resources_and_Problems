# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

def solution(s):
    num = [int(c) for c in s if c.isdigit()]
    num.sort()
    return '+'.join(str(n) for n in num)
s = input()
print(solution(s))