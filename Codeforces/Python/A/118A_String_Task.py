## By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

import sys

x = list(str(sys.stdin.readline()).strip())
vowels = ["a", "o", "y", "e", "u", "i"]
string_task = []
for i in x:
    char = i.lower()

    if char in vowels:
        pass
    else:
        string_task.append(".")
        string_task.append(char)
string_task_final = "".join(string_task)
print(string_task_final)