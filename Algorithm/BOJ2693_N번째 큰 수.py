import sys
input = sys.stdin.readline

for t in range(int(input())):
    nums = list(map(int, input().split()))
    nums.sort()

    print(nums[-3])
