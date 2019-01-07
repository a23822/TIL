"""
시간 초과  92.3/100
"""

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    answer = 0
    waiting = truck_weights
    onBridge = [] # 다리 위
    ing = {} # 진행 중
    finish = []
    onWeight = 0
    i = 0
    while len(finish) != len(truck_weights):
        cnt += 1
        #건너야할 차가 있을 경우
        if i < len(truck_weights):
            #무게가 초과가 안될시
            if onWeight+truck_weights[i] <= weight:
                #차 진입
                onBridge.append(truck_weights[i])
                ing[i] = 0
                onWeight += truck_weights[i]
                i += 1
                
        #차 주행
        for c in ing.keys():
            ing[c] += 1
            if ing[c] == bridge_length:
                finish.append(truck_weights[c])
                onWeight -= truck_weights[c]
                onBridge.pop(0)
        
        
        # print("경과시간은 {}".format(cnt))
        # print("i값은 {}".format(i))
        # print("다리 위 무게는 {}".format(onWeight))
        # print("다리를 지난 트럭은 {}".format(finish))
        # print("현재상황은 {}".format(ing))
        # print("다리를 건너는 트럭은 {}".format(onBridge))
    return cnt+1