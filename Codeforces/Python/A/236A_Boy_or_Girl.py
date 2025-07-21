# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

def solution(username: str) -> str:
    method = set(username)

    if len(method) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"
    
print(solution(input()))

# Another format with ternary

def solutionTernary(username: str) -> str:
    return "CHAT WITH HER!" if len(set(username)) % 2 == 0 else "IGNORE HIM!"

if __name__ == "__main__":
    print(solutionTernary(input()))