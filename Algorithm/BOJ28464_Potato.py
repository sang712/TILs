"""
정렬을 한 뒤에 중앙 지점을 기준으로 반을 나눠 합을 각각 출력하였음
"""
N = int(input())
potatoes = sorted(list(map(int, input().split())))

mid = N//2
print(sum(potatoes[:mid]), sum(potatoes[mid:]))