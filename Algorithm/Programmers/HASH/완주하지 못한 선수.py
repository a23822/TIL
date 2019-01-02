def solution(participant, completion):
    # 이름이 키, 명 수가 값인 딕셔너리 생성
    part = dict()
    comp = dict()
    for people in participant:
        part[people] = 0
        comp[people] = 0
    
    # 사람수에 맞게 카운트
    for people in participant:
        part[people] += 1
    
    # completion 에도 반복
    for people in completion:
        comp[people] += 1
    
    # 값을 비교해서 1이 더 적은 키를 구함 
    for people in part:
        if part[people] != comp[people]:
            res = people
            
    return res

# 카운터 객체개념
import collections


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# ZIP 개념

def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
