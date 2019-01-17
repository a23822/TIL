tc = int(input()) # 첫 줄에 테스트 케이스의 수 T가 주어짐

for i in range(tc):
    N = int(input()) # 각 케이스의 첫 줄에 양수의 개수가 주어짐
    a = list(map(int, input().split())) # N개의 양수 리스트
    
    print(f'#{i+1} {max(a)-min(a)}')