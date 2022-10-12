'''
가장 둘레가 긴 삼각형을 얻는 것이므로 주어진 변의 list를 정렬해주었으며
조합을 사용할 필요 없이 연속된 3개씩 한 번에 선택하여 움직이며 비교해도 무방하므로
다음과 같이 코딩함
1) for, else 구문은 딱히 이유가 없으면 사용하지 않는 것이 더 빠르게 작업된다
2) for문을 돌릴 list가 정렬이 필요하고 역순으로 돌려야한다면 그냥 역순으로 정렬해서
for문을 정방향으로 돌리는 것이 더 빠르다
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''471ms, 첫 작성 코드'''
        # nums.sort(reverse=True)
        # a, b = nums[:2]
        # c = 0
        # for num in nums[2:]:
        #     c = num
        #     if b + c > a:
        #         return a + b + c
        #     else:
        #         a, b = b, c
        # else:
        #     return 0
        
        '''438ms, 수정 코드'''
        # nums.sort(reverse=True)
        # a, b = nums[:2]
        # c = 0
        # for num in nums[2:]:
        #     c = num
        #     if b + c > a:
        #         return a + b + c
        #     else:
        #         a, b = b, c
        # return 0
        
        '''196ms 코드'''
        nums.sort(reverse=True)
        for i in range(0, len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i+1] + nums[i+2] + nums[i]
        return 0
    
        '''208ms, 정답 코드,'''
        # nums.sort()
        # for i in range(len(nums)-3, -1, -1):
        #     if nums[i] + nums[i+1] > nums[i+2]:
        #         return nums[i] + nums[i+1] + nums[i+2]
        # return 0