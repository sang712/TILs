"""
미분개색기를 음차한 한자
미분해서 1을 대입하면 계수와 차수를 곱해서 모두 더한 값과 같기 때문에
그렇게 구하여 출력하였음
"""
N = int(input())
ans = 0
for _ in range(N):
    c, k = map(int, input().split())
    ans += c*k
print(ans)