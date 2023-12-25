"""
그냥 무작정 모든 경우를 리스트에 저장하려고 하니 메모리 초과가 나서
재귀함수를 구현하여 풀이하였음

풀이는 똑같은데 함수를 구현해서 푼 것과
dp 리스트를 두고 풀이한 것과는 20배 차이남
"""
N, red, green, blue = map(int, input().split())

f = [1]
for i in range(1, 11):
    f.append(f[-1] * i)

def decorate(r, g, b, comb, i):
    if i == N + 1:
        global ans
        ans += comb
        return
    if r+i <= red:
        decorate(r+i, g, b, comb, i+1)
    if g+i <= green:
        decorate(r, g+i, b, comb, i+1)
    if b+i <= blue:
        decorate(r, g, b+i, comb, i+1)
    if i % 2 == 0:
        num = i//2
        next_comb = comb * f[i] // f[num] // f[num]
        if r+num <= red and g+num <= green:
            decorate(r+num, g+num, b, next_comb, i+1)
        if g+num <= green and b+num <= blue:
            decorate(r, g+num, b+num, next_comb, i+1)
        if b+num <= blue and r+num <= red:
            decorate(r+num, g, b+num, next_comb, i+1)
    if i % 3 == 0:
        num = i//3
        next_comb = comb * f[i] // f[num] // f[num] // f[num]
        if r+num <= red and g+num <= green and b+num <= blue:
            decorate(r+num, g+num, b+num, next_comb, i+1)

ans = 0
decorate(0, 0, 0, 1, 1)
print(ans)

'''
# 사용한 장난감의 개수를 키 값으로 사용한 경우 52ms걸림
# factorial을 import해서 사용함
N,R,G,B=map(int,input().split())
dp=[{} for _ in range(N+1)]
dp[0][(0,0,0)]=1
    
for i in range(1,N+1):
    for xr,xg,xb in dp[i-1].keys():
        nr,ng,nb=R-xr,G-xg,B-xb
        cnt=dp[i-1][(xr,xg,xb)]
        if i%3==0 and i//3<=min([nr,ng,nb]):
            c=cnt*(factorial(i))//(factorial(i//3)**3)
            if (xr+i//3,xg+i//3,xb+i//3) not in dp[i]:
                dp[i][(xr+i//3,xg+i//3,xb+i//3)]=c
            else:
                dp[i][(xr+i//3,xg+i//3,xb+i//3)]+=c
        if i%2==0:
            c=cnt*(factorial(i))//(factorial(i//2)**2)
            if i//2<=min([nr,ng]):
                if (xr+i//2,xg+i//2,xb) not in dp[i]:
                    dp[i][(xr+i//2,xg+i//2,xb)]=c
                else:
                    dp[i][(xr+i//2,xg+i//2,xb)]+=c
            if i//2<=min([nr,nb]):
                if (xr+i//2,xg,xb+i//2) not in dp[i]:
                    dp[i][(xr+i//2,xg,xb+i//2)]=c
                else:
                    dp[i][(xr+i//2,xg,xb+i//2)]+=c
            if i//2<=min([ng,nb]):
                if (xr,xg+i//2,xb+i//2) not in dp[i]:
                    dp[i][(xr,xg+i//2,xb+i//2)]=c
                else:
                    dp[i][(xr,xg+i//2,xb+i//2)]+=c

        if i<=nr:
            if (xr+i,xg,xb) not in dp[i]:
                dp[i][(xr+i,xg,xb)]=cnt
            else:
                dp[i][(xr+i,xg,xb)]+=cnt
        if i<=ng:
            if (xr,xg+i,xb) not in dp[i]:
                dp[i][(xr,xg+i,xb)]=cnt
            else:
                dp[i][(xr,xg+i,xb)]+=cnt
        if i<=nb:
            if (xr,xg,xb+i) not in dp[i]:
                dp[i][(xr,xg,xb+i)]=cnt
            else:
                dp[i][(xr,xg,xb+i)]+=cnt
res=sum([i for i in dp[N].values()])
print(res)
'''