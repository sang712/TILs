N, S = map(int, input().split())
nums = list(map(int, input().split()))

def subsequence(index, sumation, n):
    result = 0
    if index < N:
        result += subsequence(index + 1, sumation, n)
        sumation += nums[index]
        if sumation == S:
            result += 1
        result += subsequence(index + 1, sumation, n+1)
    return result
print(subsequence(0, 0, 0))