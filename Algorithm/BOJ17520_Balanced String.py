"""
직접 구현을 하다가 규칙성을 발견해서
해당 규칙으로 한줄코드를 만들었음
"""
"""
n = int(input())
bs = [(1, 1)]
for i in range(n-1):
    z, o = bs[-1]
    if i % 2:
        bs.append((((o+z)%16769023), (o+z)%16769023))
    else:
        bs.append((o%16769023, z%16769023))
print(sum(bs[-1]))
"""
n = int(input())
print(2**((n-1)//2+1)%16769023)
