"""
각 층에 플랫폼 정보를 넣을 수 있도록 빈 리스트로 초기화 하고, 입력값을 받을 때마다 해당 층에 추가하였음
그리고 층을 반복문으로 돌면서 
플랫폼 왼쪽이 낮은 층의 플랫폼의 왼쪽보다 크거나 같고 오른쪽보다 작으면 층의 차이만큼 카운팅을 하고
마찬가지로 플랫폼 오른쪽이 낮은 층의 플랫폼의 왼쪽보다 크고 오른쪽보다 작거나 같으면 층의 차이만큼 카운팅 했음
위 두 조건을 만족하지 않는 경우 그냥 해당 플랫폼의 층 수를 카운팅하도록 함

입력 조건이 10000인 줄 모르고 100으로 착각해 인덱스 에러가 났었는데
10000으로 고쳐서 정답 처리됨
10000인 줄 알았으면 이렇게 리스트를 초기화 하지 않았을 것, 시간도 60ms라 다른 답의 44ms에 못 미침
"""
N = int(input())
platforms = [[] for _ in range(10000+1)]

for _ in range(N):
    height, left, right = map(int, input().split())
    platforms[height].append((left, right))
cnt = 0
for idx, level in enumerate(platforms):
    for platform in level:
        left, right = platform
        for i in range(idx-1, -1, -1):
            reached = False
            for ground in platforms[i]:
                if ground[0] <= left < ground[1]:
                    reached = True
            if reached:
                cnt += idx - i
                break
        else:
            cnt += idx
        for i in range(idx-1, -1, -1):
            reached = False
            for ground in platforms[i]:
                if ground[0] < right <= ground[1]:
                    reached = True
            if reached:
                cnt += idx - i
                break
        else:
            cnt += idx
print(cnt)