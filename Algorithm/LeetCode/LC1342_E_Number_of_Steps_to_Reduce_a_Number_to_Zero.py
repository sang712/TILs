'''
연산 회수를 줄였지만 구현 코드보다 빠르지는 않았음
비트연산으로도 풀 수 있는데 이는 2의 배수인지를 판단하기 때문임
2의 배수임을 확인하는 비트 연산은 (num&1==0) 이고
2로 나누는 비트 연산은 (num>>1) 임
비트 연산으로 풀어도 다음 코드보다 빠르거나 하지는 않음(오히려 66ms)
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # 64ms, 연산 회수를 줄인 코드
        if num == 0:
            return 0
        cnt = 0
        while num > 1:
            if num % 2 == 0:
                cnt += 1
            else:
                cnt += 2
            num //= 2
        return cnt+1
        
        # 60ms, 구현 코드
        # cnt = 0
        # while num > 0:
        #     if num % 2 == 0:
        #         num //= 2
        #     else:
        #         num -= 1
        #     cnt += 1
        # return cnt