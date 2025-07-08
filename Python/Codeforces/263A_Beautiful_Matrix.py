# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity

def solution():
    matrix = [[], [], [], [], []]

    for i in range(5):
        row = list(map(int, input().rstrip().split()))
        matrix[i] = row

    location_1 = []
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                location_1 = [i, j]
                
    point_x = 2
    point_y = 2

    ans = abs(location_1[0] - point_x) + abs(location_1[1] - point_y)
    print(ans)
solution()