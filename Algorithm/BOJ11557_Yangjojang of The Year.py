"""
문제에서 요구한 사항을 dict 자료구조를 이용하여 구현하였음
dict의 내장함수인 setdefault를 이용하여 술의 양을 더해주었고
dict를 items 함수를 이용해 키 밸류쌍으로 뽑아낸 뒤
sorted 함수를 이용해 정렬하여 마지막값을 출력하였음
"""
import sys
input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    consumed_alcohol = dict()
    for _ in range(N):
        uni, amount = input().split()
        consumed_alcohol.setdefault(uni, 0)
        consumed_alcohol[uni] += int(amount)
    print(sorted(consumed_alcohol.items(), key=lambda x: x[1])[-1][0])