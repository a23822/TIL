def solution(clothes):
    
    temp = {}
    # [1] 값만 찾아서 카운트
    for item in clothes:
        parts = item[1]
        if parts in temp.keys():
            temp[parts] += 1
        else:
            temp[parts] = 1
    answer = 1
    # 이 값들에 1씩 더해서 곱한 뒤에 최종적으로 1을 빼서 출력한다.
    for val in temp.values():
        answer *= (val+1)
    return answer-1

"""
간결한 코딩들은 reduce를 쓰는 경향이 보임
"""
def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

"""
"""

from collections import Counter
from functools import reduce

def solution3(clothes):
    cloth_counter = Counter([ctype for _, ctype in clothes]) # <str, int>
    return reduce(lambda a, b: a + b + a * b, cloth_counter.values())
