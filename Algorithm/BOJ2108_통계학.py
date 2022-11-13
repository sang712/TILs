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
