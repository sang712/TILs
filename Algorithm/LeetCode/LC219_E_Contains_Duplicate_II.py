'''
조건에서 nums의 크기가 10^5이므로 O(N^2)으로 하면 시간복잡도 조건을 초과한다
따라서 O(N)으로 해결하는 방법을 찾아야 하는데
dictionary나 set을 이용하면 된다
현재 사용한 방법은 in으로 확인하고 있음에도 dictionary 타입이므로 시간복잡도에 영향이 없다
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checking = dict()
        for i, num in enumerate(nums):
            if num in checking and i - checking[num] <= k:
                return True
            checking[num] = i
        return False