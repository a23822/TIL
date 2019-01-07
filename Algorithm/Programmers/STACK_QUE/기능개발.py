"""
런타임 에러  30/100
"""

def solution(progresses, speeds):
    answer = []
    
    # 각 작업마다 걸리는 시간을 구해 배열 생성
    complete = []
    index = len(speeds)
    for i in range(index):
        cDay_mok = (100 - progresses[i])%speeds[i]
        if cDay_mok == 0:
            cDay = int((100 - progresses[i])/speeds[i])
        else:
            cDay = int((100 - progresses[i])/speeds[i]) + 1
        complete.append(cDay)
    print(complete)
    # 배포 배열에 하나씩 넣기
    temp = 0
    for i in range(index):
        if i == 0:
            answer.append(1)
        else:
            if complete[i] <= complete[temp]:
                answer[temp] += 1   ###
            else:
                answer.append(1)
                temp = i        
                    
    return answer



"""
통과 , 
"""

def solution2(progresses, speeds):
    answer = []
    
    # 각 작업마다 걸리는 시간을 구해 배열 생성
    complete = []
    index = len(speeds)
    for i in range(index):
        cDay_mok = (100 - progresses[i])%speeds[i]
        if cDay_mok == 0:
            cDay = int((100 - progresses[i])/speeds[i])
        else:
            cDay = int((100 - progresses[i])/speeds[i]) + 1
        complete.append(cDay)
    # 배포 배열에 하나씩 넣기
    temp = 0
    for i in range(index):
        if i == 0:
            answer.append(1)
        else:
            if complete[i] <= complete[temp]:
                answer[-1] += 1  # 이 부분을 잘못 판단했었음.
            else:
                answer.append(1)
                temp = i        
                    
    return answer


"""
다른사람풀이
ZIP 활용
"""

def solution3(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

"""
다른사람풀이
Math ceil 이용
"""

from math import ceil

def solution4(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList
