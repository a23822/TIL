"""
효율성에서 시간초과
"""

def solution(n, works):
    answer = 0
    while n:
        if sum(works) == 0:
            return 0
        else:
            if max(works) != min(works):
                works[works.index(max(works))] -= 1
            else:
                works[0] -= 1
            n-=1
    for w in works:
        answer += w**2
    return answer

"""
진행 중
"""
def solution(n, works):
    answer = 0
    a = sum(works)-n
    if a< 0:
        return 0
    else:
        if a % len(works) == 0:
            return len(works) * (a/len(works))**2
        else:
            temp = a / len(works)
            