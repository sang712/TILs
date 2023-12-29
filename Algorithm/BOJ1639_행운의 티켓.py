"""
짝수 길이의 수를를 긴 것에서 짧은 순으로 순회하고
그리고 그것을 반으로 나눠 비교하는 방식으로 풀이하였음
"""
nums = list(map(int, input()))
ans = 0
for i in range(len(nums)//2, 0, -1):
    if ans >= i:
        break
    for j in range(len(nums) - i*2 + 1):
        left = sum(nums[0+j:i+j])
        right = sum(nums[i+j:i*2+j])
        if left == right:
            ans = i
            break
        
print(ans*2)