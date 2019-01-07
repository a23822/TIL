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


"""
다른사람풀이
"""

def solution2(bridge_length, weight, truck_weights):
    ing = [0]*bridge_length
    cnt = 0
    while ing:
        cnt += 1
        ing.pop(0)#트럭이 지나감
        if truck_weights:
            if sum(ing)+truck_weights[0]<=weight:#다리에 있는 트럭의 무게와 대기 중인 트럭의 무게가 제한 무게보다 작거나 같다면
                ing.append(truck_weights.pop(0))#다리에 트럭 올림
            else:
                ing.append(0)#중량 초과면 트럭 안올림
    return cnt

"""
정통파??
"""

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution3(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()


"""
FIFO
"""

def solution4(bridge_length, max_weight, truck_weights):
    # FIFO 문제.
    bridge = [0]*bridge_length
    curr_weight = 0
    ans = 0
    while len(truck_weights) > 0:
        ans += 1
        ar = bridge.pop(0)
        curr_weight -= ar
        if curr_weight + truck_weights[0] > max_weight:
            bridge.append(0)            
        else:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            curr_weight += truck
    while curr_weight > 0:
        ans += 1
        ar = bridge.pop(0)
        curr_weight -= ar
    return ans