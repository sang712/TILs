"""
각 숫자 별로 K번 만큼 사용하는 거면 문제가 더 어려웠을 것이고 그렇게 생각하고 풀다가
문제를 다시 읽고 풀이 방식을 선회하였음
dp를 각 숫자에 필요한 총 숫자의 개수를 set 자료 구조에 넣은 형태로 갖도록 함
그 후에 수를 하나씩 늘려가면서 해당 숫자에서 주어진 숫자를 뺀 수를 dp에서 확인한 후에
해당 수 + 1이 K보다 작거나 같으면 다음 dp에 넣는 방식으로 dp를 완성하고
dp에 넣을 set가 비어있다면 멈추고 답을 출력하도록 하였음
"""
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
K = int(input())

dp = [{0, }]
target = 1
while True:
    dp_target = set()
    for num in nums:
        if target - num >= 0:
            for k_of_target in list(dp[target - num]):
                if k_of_target < K:
                    dp_target.add(k_of_target + 1)
        else:
            break
    if dp_target:
        dp.append(dp_target)
        target += 1
    else:
        break
    
print('jjaksoon' if target % 2 else 'holsoon', end=' ')
print(f'win at {target}')