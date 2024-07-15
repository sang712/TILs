"""
주어진 입력의 크기가 그렇게 크지 않아서 그냥 정렬하고 출력하였음
"""
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
print(A[K-1])