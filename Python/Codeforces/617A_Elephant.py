# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity

x = int(input())
step = [5, 4, 3, 2, 1]
step_count = 0

for i in step:
    step_count += x // i
    x = x % i

print(step_count)

#Most optimal version
x = int(input())
steps = x // 5
if x % 5 != 0:
    steps += 1
print(steps)