import sys
input = sys.stdin.readline

N = int(input())

ans = 0
for _ in range(N):
    time, duration = input().split()
    hour, minute = map(int, time.split(':'))
    duration = int(duration)
    over_oclock = False
    if duration + minute > 60:
        over_oclock = True
        duration2 = duration + minute - 60
        duration = 60 - minute
        
    if 7 <= hour < 19:
        ans += duration * 10
    else:
        ans += duration * 5
    
    if over_oclock:
        hour += 1
        if 7 <= hour < 19:
            ans += duration2 * 10
        else:
            ans += duration2 * 5
print(ans)