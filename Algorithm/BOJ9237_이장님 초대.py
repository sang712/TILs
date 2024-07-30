"""
내림차순으로 정렬을 한 뒤, 나무가 자라는 시간을 반복하여 방문하면서
나무가 자라는 시간 + idx의 최댓값을 갱신하고
첫 날과 idx가 0으로 시작하는 것을 감안하여 2를 더해준 뒤 출력하였음
"""
N = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)

max_days = 0
for i in range(N):
    if max_days < i + trees[i]:
        max_days = i + trees[i]
print(max_days+2)