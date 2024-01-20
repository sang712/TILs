"""
입력으로 주어진 알파벳의 각 개수를 세고
그 중에서 홀수 개수인 알파벳이 둘 이상이면 팰린드롬을 만들 수 없으므로 중간에 멈추고
그 외의 경우라면 알파벳을 오름차순으로 정렬해 앞에 붙이고, 내림차순으로 뒤에 붙이는데
만약 홀수 개수인 알파벳이 있었다면 그 중앙에 붙이도록 하였음
"""
counter = {}
for alpha in input():
    counter.setdefault(alpha, 0)
    counter[alpha] += 1

odd = None
for alpha in counter:
    if counter[alpha] % 2:
        if odd:
            print("I'm Sorry Hansoo")
            break
        odd = alpha
else:
    ans = []
    for alpha in sorted(list(counter.keys())):
        ans.extend([alpha] * (counter[alpha] // 2))
    if odd:
        ans.append(odd)
    for alpha in sorted(list(counter.keys()))[::-1]:
        ans.extend([alpha] * (counter[alpha] // 2))
    print(*ans, sep='')
        