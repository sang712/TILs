"""
입력 정보를 받아서 금, 은, 동 순으로 정렬하였고
for문으로 정렬된 정보 리스트를 돌면서
딕셔너리 자료 구조에 나라와 등수를 키와 아이템으로 저장하였음
이 때 for문의 index를 이용하여 직전 나라와 전부 같다면 직전 나라와 같은 등수를,
그게 아니라면 index + 1을 등수로 갖게끔하여 요구조건을 만족하도록 하였음
"""
import sys
input = sys.stdin.readline

records = []

N, K = map(int, input().split())
for _ in range(N):
    records.append(list(map(int, input().split())))
    
records.sort(key=lambda x: (-x[1], -x[2], -x[3]))

countries = {records[0][0]: 1}
for i in range(1, N):
    prev_country, prev_gold, prev_silver, prev_bronze = records[i - 1]
    curr_country, curr_gold, curr_silver, curr_bronze = records[i]
    if prev_gold == curr_gold and prev_silver == curr_silver and prev_bronze == curr_bronze:
        countries[curr_country] = countries[prev_country]
    else:
        countries[curr_country] = i + 1
print(countries[K])