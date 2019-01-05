def solution(prices):
    answer = []
    index = len(prices)
    #기준을 잡는다.
    for i in range(index):
        cnt = 0 # 초 수 카운트
        for j in range(i+1,index):
            cnt += 1
            if prices[i] > prices[j]: # 떨어지는 순간 캐치
                break
        answer.append(cnt)
    return answer

"""
큐 활용한 다른사람의 풀이
"""

from collections import deque
def solution2(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer