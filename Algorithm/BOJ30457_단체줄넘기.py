"""
조건에 따르면 키가 같은 사람은 최대 2사람만 줄에 설 수 있기 때문에
키 별로 최대 2사람씩 카운팅해서 더한뒤에 출력하였음
"""
N = int(input())
A = map(int, input().split())
counter = {}
for a in A:
    counter.setdefault(a, 0)
    if counter[a] < 2:
        counter[a] += 1
print(sum(counter.values()))
