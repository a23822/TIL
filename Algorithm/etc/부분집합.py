# 바이너리 카운팅

arr = [3,6,7,1,5,4]

n = len(arr) # 원소의 개수

for i in range(1<<n):
    for j in range(n+1): # 원소의 수만큼 비교함
        if i & (1<<j): # i 의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")
    print()
print()