"""
어떻게 풀지 몰라 답을 찾아봤음
머리만 잘 굴린다면 생각했던 것보다 쉽게 풀리는 문제였음

정렬을 한 뒤에 마지막에서 두번째 값을 제외한 모든 이전 값들을 묶으면
무조건 마지막에서 두번재 값을 얻게 됨
이 값보다 클 수 있는 경우는 모든 값을 다 더해서 평균을 내는 것 뿐이라 둘 중에 큰 것을 출력하면 됨
"""
N = int(input())
blocks = list(map(int, input().split()))

An_2 = sorted(blocks)[-2] if N > 2 else 0
print(max(sum(blocks)/N, An_2))