'''
요세푸스 문제
구현으로 풀었고 요세푸스 문제 2, 3은 시간복잡도를 고려하거나 수학적인 방법으로 개선하여 풀어야 함
'''
N, K = map(int, input().split())
table = [i for i in range(1, N+1)]
length = N
ans = "<"
eliminate = K-1
while table:
    ans += str(table.pop(eliminate))
    length -= 1
    if length > 0:
        eliminate = (eliminate + K-1) % length
        ans += ", "
print(ans + '>')