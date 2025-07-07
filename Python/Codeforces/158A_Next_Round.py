# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity
sum = 0
first_line = list(map(int, input().split()))
second_line = list(map(int, input().split()))
n = first_line[0]
k = first_line[1] - 1
for _ in range(n):
    if second_line[_] >= second_line[k]:
        if second_line[_] > 0:
            sum += 1
print(sum)