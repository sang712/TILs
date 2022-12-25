'''
처음에는 숫자를 받아와서 정렬한 뒤에 중앙값을 찾도록 했지만, 정렬을 하게되면(O(nlogn)) 정렬을 하지 않은 것(O(n)) 보다 느려져서 
정렬을 하지 않는 풀이를 찾았고 적용해보도록 하겠음

정렬을 하지 않는 방식을 적용하였더니 584ms -> 240ms로 소요시간을 단축할 수 있었음

그리고 무엇보다 고민했던 round 함수(오사오입이 적용된 함수)의 사용에 관해선 고민할 필요가 없었음
주어진 수들은 모두 정수이고, 홀수 개가 주어지는데, 평균이 0.5가 딱 나오려면 짝수로 나누는 수 밖에는 없음
그렇기 때문에 round를 안심하고 써도 무방했음(대체재로 쓴 f-formatting도 오사오입이었고)
'''
# 정렬을 사용하지 않은 풀이, 240ms
import sys
input = sys.stdin.readline

N = int(input())

nums = [0] * 8001

for i in range(N):
    num = int(input())
    nums[num + 4000] += 1

cnt = 0
max_frequent = max(nums)
frequent_num = -8001
frequent_cnt = 0
median = -8001
max_num = -4001
min_num = 4001
sumation = 0
for i in range(len(nums)):
    if nums[i] == 0:
        continue
    
    cnt += nums[i]
    num = i - 4000
    if N // 2 + 1 <= cnt and median == -8001:
        median = num
    sumation += num * nums[i]
    
    if max_frequent == nums[i] and frequent_cnt < 2:
        frequent_num = num
        frequent_cnt += 1
    
    if min_num == 4001:
        min_num = min(min_num, num)
    max_num = max(max_num, num)
print(round(sumation / N), median, frequent_num, max_num - min_num)

# 정렬을 사용한 풀이, 584ms
'''
import sys
N = int(input())
count_numbers = {}
numbers = []
sumation = 0

for _ in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)
    
    count_numbers.setdefault(number, 0)
    count_numbers[number] += 1
    
    sumation += number

sorted_count_numbers = list(count_numbers.items())
sorted_count_numbers.sort(key=lambda x: (-x[1], x[0]))

numbers.sort()

mean = sumation/N
if -0.5 <= mean < 0.5:
    print(0)
else:
    print(f'{mean:.0f}')
print(numbers[N//2])
if N > 1:
    number1, count1 = sorted_count_numbers[0]
    number2, count2 = sorted_count_numbers[1]
    if count1 == count2:
        print(number2)
    else:
        print(sorted_count_numbers[0][0])
else:
    print(sorted_count_numbers[0][0])
print(numbers[N-1] - numbers[0])
'''