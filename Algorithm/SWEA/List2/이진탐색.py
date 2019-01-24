tc = int(input())

def go(x, P):
    start = 1
    end = P
    cnt = 1
    while True:
        middle = int((start+end)/2)
        if middle < x:
            start = middle
        elif middle > x:
            end = middle
        else:
            return cnt
        
        cnt+=1

for t in range(tc):
    a = list(map(int, input().split()))
    P = a[0]
    pa = a[1]
    pb = a[2]
    a = go(pa, P)
    b = go(pb, P)
    winner = "A"
    if a > b:
        winner = "B"
    elif a == b:
        winner = "0"

        
    
    print('#{} {}'.format(t+1, winner))