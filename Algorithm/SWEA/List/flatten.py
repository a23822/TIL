for i in range(10):
    n = int(input()) # 덤프 횟수
    box = [int(i) for i in input().split()] # 박스 분포

    while n:
        #가장 높은 곳에서 -1 가장 낮은 곳에 +1
        box[box.index(max(box))]-=1
        box[box.index(min(box))]+=1
        n-=1
        if max(box)-min(box) == 2:
            break

    print(f"#{i+1} {max(box)-min(box)}")