"""
피보나치를 빠르게 구하는 방법 중 행렬곱을 이용해 도출한 결과를 한 번 더 일반화하여 만든 공식인데
(fn+2) = (1 1)(fn+1)  임을 이용해서 두 개의 행렬식을 합쳐서 한 번에 표현하면
(fn+1)   (1 0)( fn )

(fn+1  fn) = (1 1)( fn  fn-1) 이고 이 것을 n-2가 0일 때까지 전개를 하면 
(fn  fn-1)   (1 0)(fn-1 fn-2)

(fn+1  fn) = (1 1)^n  이 됨 왜냐하면 ( fn  fn-1) 머시기도 결국 (1 1) 곱하기 머시기 이고
(fn  fn-1)   (1 0)                  (fn-1 fn-2)              (1 0)
이 행렬은 n은 0일 때와 같기 때문

여기서 나아가서
f2n-1 = fn^2 + fn-1^2 이고
fn = (fn-1 + fn+1)fn 이고 (fn-1 + fn+1)fn = (2fn-1 + fn)fn 임

이 문제는 가장 마지막 부분을 이용해 풀었음

추가로 음수로 가도 절댓값만 같으면 결과도 같은 절댓값을 갖는데 
대신 짝수면 음수 결과, 음수면 짝수 결과가 나옴

+) 문제를 푸시하려고 커밋메시지를 작성하면서 문제 카테고리를 봤는데 DP가 있었음
DP로도 풀리는 문제인가 하고 봤더니 더 짧은 구현으로 풀이가 되고 시간도 별로 차이가 안 나서 신기했음
위의 풀이 112ms, DP풀이 272ms 다른 풀이는 몇천 ms씩 되는 거 같은데 생각보다 괜찮은 것 같음
결론: 피보나치는 n이 백만 이하면 dp로 풀어도 된다~
"""
fibo = {-1: 1, 0: 0, 1: 1, 2: 1}
def f(num):
    if num in fibo:
        return fibo[num]
    if num > 0:
        m = num//2
        if num % 2:
            fibo[num] = f(m+1)**2 + f(m)**2
        else:
            fm = f(m)
            fm_1 = f(m-1)
            fibo[num] = (fm+fm_1) * fm + fm_1*fm
    else:
        if abs(num) % 2:
            return f(abs(num))
        else:
            return -f(abs(num))
    return fibo[num]
n = int(input())
ans = f(n)
print(-1 if ans < 0 else 0 if ans == 0 else 1)
print(abs(ans) % 1_000_000_000)

# n = int(input())
# fibo = [0, 1, 1]
# for i in range(2, abs(n)):
#     fibo.append((fibo[i]+fibo[i-1])%1_000_000_000)
# print(1 if n > 0 else 0 if n == 0 else 1 if abs(n)%2 else -1)
# print(fibo[abs(n)])