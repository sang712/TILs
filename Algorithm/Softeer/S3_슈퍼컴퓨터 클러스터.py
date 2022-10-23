'''
조건
1≤N≤105인 정수
1≤ai≤109인 정수
1≤B≤1018인 정수

풀이
답의 범위가 주어져 있고 주어진 값을 답 하나로 최적화하는 문제이므로 이분탐색을 떠올려야하는 문제
업그레이드 완료했을 때 만들 수 있는 성능은 최대 2*10^9 이므로
0부터 2000000000을 범위로 이분탐색을 하여 
해당 성능으로 업그레이드 할 때의 비용과 예산을 비교하여 답을 도출함
시간복잡도 O(N*log(B**0.5))이므로 최대 50만*9
'''
import sys
N, B = map(int, input().split())
A = list(map(int, input().split()))

def is_upgradable(performance):
    price = 0
    for a in A:
        price += (performance-a)**2 if performance - a > 0 else 0

    return True if price <= B else False
# 업그레이드해서 증가시킬 수 있는 최대 성능은 10^9이고,
# 최종적으로 업그레이드가 끝났을 때 가능한 성능은 (기존 성능 + 증가시킬 수 있는 최대 성능) = 2*10^9 이므로 다음 범위로 왼쪽 오른쪽을 지정함

left, right = 0, 2000000000
while right-left > 1:
    mid = (right+left)//2
    if is_upgradable(mid):
        left = mid
    else:
        right = mid
print(left)