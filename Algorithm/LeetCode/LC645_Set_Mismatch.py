'''
똑같은 코드이더라도 코드를 돌리는 시간에 따라서 문제푸는데에 걸리는 시간이 달라지는 것을 알게 되었음
내풀이 502ms, discuss 파이썬 1등 풀이 500ms 라서 이상했는데
5시간 정도 뒤에 다시 해보니
내풀이 295ms, 1등 풀이 194ms 였음

나는 set을 이용해서 원래 만들어졌어야 할 set을 만들었고
주어진 list를 돌면서 있는 것은 set에 빠진 부분을 정답 list에 넣었음
그 후에 주어진 list를 돌면서 만든 set을 원래의 set에서 빼고 그 결과를 정답 list에 넣음

파이썬 1등 풀이는 다 더했을 때의 결과를 따로 만들어놓고, 
주어진 list의 합과 주어진 list를 set으로 변환한 것의 합을 구해서
빼서 답을 도출하였음 
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        origin_s = set(i for i in range(1, n+1))
        s_having_error = set()
        for num in nums:
            if num in s_having_error:
                ans.append(num)
            else:
                s_having_error.add(num)
        ans.append(*(origin_s - s_having_error))
        return ans
        # n = len(nums)
        # true_sum = n*(n+1)//2
        # sum_with_error = sum(nums)
        # set_sum = sum(set(nums))
        # return [sum_with_error - set_sum, true_sum - set_sum]