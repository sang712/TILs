"""
참이 0개이다 라는 명제가 들어있고 다른 모든 명제들이 거짓이라면
모순이 되기 때문에 
0부터 50까지 셀 수 있는 리스트로 문제를 푸는 것이 좋고
그렇지 않고 나처럼 Counter를 사용했다면
break로 벗어나지 않았을 때 0이 포함되었다면 -1
0이 포함되지 않았다면 0을 출력하는 것이 맞음
"""
import collections

N = int(input())
nums = collections.Counter(map(int, input().split()))

for num, num_of_num in sorted(nums.items(), key=lambda x: -x[0]):
    if num == num_of_num:
        print(num)
        break
else:
    if 0 in nums:
        print(-1)
    else:
        print(0)