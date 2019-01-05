"""
미완성
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
    # 배포 배열에 하나씩 넣기
    temp = 1
    for i in range(index):
        if i == 0:
            answer.append(1)
        else:
            for j in range(temp, index):
                if complete[i] > complete[j]:
                    
    return answer