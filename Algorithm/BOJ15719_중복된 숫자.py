"""
입력의 개수가 1000만개라 readline으로 읽어오면 메모리(256mb)초과가 남
해서 여러 시행착오를 겪었는데
하나는 입력을 split, map, int 함수로 엮어서 받아들이려니 이 부분이 문제가 되었고
이부분을 해결하고 나니 숫자로 변환하는 과정에서 시간초과가 나서
아예 그냥 str자체에서 하나하나 보면서 숫자를 온전하게 만들고 그 후에 숫자로 변환하는 과정을 통해 풀이함
python은 전혀 통과하지 못해 pypy3로 진행하였음

+) 추가로 비트연산으로 진행하는 방법이 있어 해당 방법으로 풀이해 보았는데
오히려 메모리도 추가로 소모되고 시간도 전혀 단축되지 않아서 python3 도전은 다음에 하는 것으로..
"""
import sys

# pypy3 통과 코드, 덧셈을 이용한 방법, 2876ms 소요
N = int(input())
sum_target = N * (N - 1) // 2 # range를 사용하면 72ms가 더 소요됨

nums = sys.stdin.readline()

sum_current = 0
temp = ''
for num in nums:
    if num.isdigit():
        temp += num
    else:
        sum_current += int(temp)
        temp = ''
        
print(sum_current - sum_target)


# pypy3 통과 코드, 비트연산으로 메모리를 조금 더 감소시키는 것을 의도한 방법, 3744ms 소요
# 의도와는 다르게 메모리 감소도 시간 감소도 전혀 되지 않음
"""
N = int(input())
counter = [0] * (N // 32 + 1) # 32비트로 저장 (비트는 임의로 설정 가능)

nums = sys.stdin.readline()
temp = ''
for num in nums:
    if num.isdigit():
        temp += num
    else:
        temp = int(temp)
        if counter[temp // 32] & (1 << temp % 32):
            print(temp)
            break
        counter[temp // 32] |= 1 << temp % 32
        temp = ''
"""