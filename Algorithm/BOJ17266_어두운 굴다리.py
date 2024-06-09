N = int(input())
M = int(input())
xs = list(map(int, input().split()))

def install_streetlamp(h):    
    if xs[0] - h > 0 or xs[-1] + h < N:
        return False
    
    left, right = xs[0] - h, xs[0] + h
    for x in xs:
        if x-h <= right:
            right = x+h
        else:
            return False
    return True

left, right = 0, N
ans = N
while left <= right:
    mid = (left + right) // 2
    if install_streetlamp(mid):
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)