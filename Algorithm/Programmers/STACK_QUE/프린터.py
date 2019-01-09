"""
location 관련해서 계속 실패함
"""


def solution(priorities, location):
    answer = 0
    printing = []
    temp = 0
    while len(priorities) != 1:
        #print("location값은 {} 이다.".format(location))
        # 맨 앞에꺼 뽑는다
        p = priorities.pop(0)
        
        if p >= max(priorities):
            printing.append(p)
            temp+=1
        else: #중요도가 더 높은 문서가 한 개라도 존재할때
            priorities.append(p)    
        print(temp)
    printing.append(priorities[0])
    print(priorities)
    
    print(printing)
    print(location)
    
    return answer

    """
    해결함
    index를 따로 구하는 배열을 만들면 됨
    """
    def solution2(priorities, location):
    answer = 0
    printing = []
    before = []
    after = []
    for i in range(len(priorities)):
        before.append(i)
    
    while len(priorities) != 1:
        #print("location값은 {} 이다.".format(location))
        # 맨 앞에꺼 뽑는다
        p = priorities.pop(0)
        p2 = before.pop(0)
        if p >= max(priorities):
            printing.append(p)
            after.append(p2)
        else: #중요도가 더 높은 문서가 한 개라도 존재할때
            priorities.append(p)
            before.append(p2)
    printing.append(priorities[0])
    after.append(before[0])
    
    answer = after.index(location) + 1
    return answer


    """
    다른사람풀이
    심플함
    """

    def solution3(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans

"""
콜렉션활용
"""
import collections

def solution4(priorities, location):
    pri = collections.deque(priorities)
    loc = [0 for i in range(len(pri))]
    loc[location] += 1
    loc = collections.deque(loc)
    count = 0
    while sum(loc) != 0:
        if pri[0] == max(pri):
            pri.popleft()
            loc.popleft()
            count += 1
        else:
            a = pri.popleft()
            b = loc.popleft()
            pri.append(a)
            loc.append(b)
    return count