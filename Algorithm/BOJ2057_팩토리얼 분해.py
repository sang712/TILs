"""
이전 팩토리얼을 모두 합해도 다음 팩토리얼 값을 만들 수 없다는 점에서 착안해서
나올 수 있는 가장 큰 팩토리얼부터 그냥 적용해보는 방식으로 구현하였음
이렇게 되면 조합을 하지 않아도 바로 취사선택이 가능해서 시간을
560ms 에서 40ms로 줄일 수 있음
"""
N = int(input())
factorial = [1]
for i in range(1, 21):
    factorial.append(factorial[-1] * i)
    i += 1

for num in factorial[::-1]:
    if N > num:
        N -= num
    elif N == num:
        print('YES')
        break
else:
    print('NO')