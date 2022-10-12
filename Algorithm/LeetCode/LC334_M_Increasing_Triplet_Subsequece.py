'''
리스트를 돌면서 가장 작은 수(first)와 그 다음으로 작은 수(second)를 갱신하는데, 
second를 갱신 한 후에 first가 새로운 수로 갱신될 수 있지만 목표는 second를 얻고
second보다 큰 수를 찾는 것이므로 상관 없음
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False