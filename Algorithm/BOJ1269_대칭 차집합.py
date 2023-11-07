"""
계산 방법은
n(AnB) = n(A) + n(B) - n(AUB) 이니까
n(AUB) - 2*n(AnB)하면 문제가 원하는 개수가 나옴
정리해서 바로 출력하였음
"""
len_A, len_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A.update(B)
print(2*len(A) - (len_A + len_B))