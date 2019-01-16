def solution(answers):
    """
    1번 수포자 :  12345 반복
    2번 수포자 :  21 23 24 25 반복
    3번 수포자 : 3311224455 반복
    """
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    info = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == supo1[i]:
            info[0] += 1
        if answers[i] == supo2[i]:
            info[1] += 1
        if answers[i] == supo3[i]:
            info[2] += 1
    res = []
    for i in range(len(info)):
        if info[i] == max(info):
            res.append(i+1)
    return res