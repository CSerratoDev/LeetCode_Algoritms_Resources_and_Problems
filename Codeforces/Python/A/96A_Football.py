# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

def dangerousPlay(players):
    count = 1
    for i in range(1, len(players)):
        if players[i] == players[i-1]:
            count += 1
            if count >= 7:
                return "YES"
        else:
            count = 1
    return "NO"
players = readLine()
print(dangerousPlay(players))
