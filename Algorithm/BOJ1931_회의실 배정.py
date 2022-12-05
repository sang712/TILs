'''
아이디어가 생각이 나지 않아서 유형을 참고하였는데도 방법이 떠오르지 않아 검색하였음
그리디와 정렬이라는데 어떻게 정렬하면 그리디를 적용할 수 있을까 고민해도 잘 생각이 나지 않았음

그렇게 검색을 하고 결과를 보니 이렇게 쉬운 걸 왜 못 떠올렸을까 싶음
방법만 체크하고 직접 구현해보려고 함

끝나는 시간을 기준으로 오름차순으로 우선 정렬하고 시작하는 시간을 기준으로 오름차순 정렬하여 이용하였음
끝나는 시간을 우선으로 정렬해야 시작시간과 꼬이지 않고 그리디하게 체크를 할 수 있음
'''
import sys
input = sys.stdin.readline

N = int(input())
I = [tuple(map(int, input().split())) for _ in range(N)]

I.sort(key = lambda x: (x[1], x[0]))

end_time = 0
cnt = 0
for start, end in I:
    if start >= end_time:
        end_time = end
        cnt += 1
print(cnt)