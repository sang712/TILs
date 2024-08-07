"""
연속한 같은 문자열의 수를 센 뒤에
그 수들을 나열했을 때 인접한 두 수 중 가장 작은 수를 계속해서 계산해 나가면서
그 수 중 가장 큰 수를 구하도록 하였음
그 뒤에 2를 곱해서 길이를 출력하였음
"""
N = int(input())
magnet = input()
polarity = [0]
ans = 0
cnt = 1
for i in range(1, N):
    if magnet[i] == magnet[i-1]:
        cnt += 1
    else:
        polarity.append(cnt)
        cnt = 1
        ans = max(ans, min(polarity[-1], polarity[-2]))
polarity.append(cnt)
ans = max(ans, min(polarity[-1], polarity[-2]))
print(2*ans)