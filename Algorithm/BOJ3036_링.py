"""
첫 링과 각 링의 비율을 기약분수형태로 나타내기 위해 두 링의 반지름의 최대공약수를 구하였고
반지름을 최대공약수로 나눈 뒤 저장하여 출력하였음
"""
def gcd(num1, num2):
    if num1 == 0: return num2
    return gcd(num2%num1, num1)

N = int(input())
rings = list(map(int, input().split()))
ans = []
first_ring = rings[0]
for ring in rings[1:]:
    gc_ring = gcd(first_ring, ring)
    ans.append(f'{first_ring//gc_ring}/{ring//gc_ring}')
print(*ans, sep='\n')