"""
처음에는 조합 문제라고 생각해서 앞자리 수가 뒷자리 수보다 작거나 같다는 조건으로 4자리 수를 만들었었음
근데 이 경우 반례로 1324가 있기 때문에 위의 전제는 틀렸음을 알 수 있었음
그래서 그냥 확인해 볼 숫자도 9000개밖에 안 되기 때문에 그냥 브루트 포스로 다 확인했고
혹시나 시간을 줄일 수 있을까 해서 방문처리도 하였음
"""
card = input().split()

clock_num = sorted([''.join(card[i:] + card[:i]) for i in range(4)])
checked = set()
clock_nums = []
for num in range(1111, 10000):
    check_num = str(num)
    if '0' in check_num:
        continue

    if not check_num in checked:
        candidates = sorted([''.join(check_num[i:] + check_num[:i]) for i in range(4)])
        checked.update(candidates)
        clock_nums.append(candidates[0])
        
clock_nums.sort()
print(clock_nums.index(clock_num[0]) + 1)