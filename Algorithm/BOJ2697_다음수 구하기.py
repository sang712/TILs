"""
뒤에서부터 숫자를 하나씩 떼어 스택 자료 구조에 넣고
기존 숫자의 마지막 수와 스택의 마지막 숫자를 비교해서 기존 숫자의 마지막 수가 작으면
스택의 그 마지막 숫자를 넣고 스택을 정렬한 뒤
해당 숫자보다 큰 수 중 가장 작은 수를 찾아 기존 숫자의 마지막에 배치함
그 후에 기존 수와 정렬된 스택의 수를 합쳐 반환하는 방식으로 풀이하였음
"""
import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    num = list(input().strip())
    stack = []
    for i in range(len(num)):
        stack.append(num.pop())
        if num:
            if num[-1] >= stack[-1]:
                continue
            else:
                lastnum = num[-1]
                stack.append(num.pop())
                stack.sort()
                for i in range(len(stack)):
                    if lastnum < stack[i]:
                        num.append(stack.pop(i))
                        break
                num += stack
                ans.append(''.join(num))
                break
    else:
        ans.append('BIGGEST')
print(*ans, sep='\n')