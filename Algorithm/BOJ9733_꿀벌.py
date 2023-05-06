"""
EOFError를 검출하는 방식으로 입력을 받는 부분을 종료하려고 했는데 
except 분기로 넘어가지 않아서 그냥 try 안에 if라인을 추가하여 구현하였음
"""
import sys
input = sys.stdin.readline

num_work = 0
work = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
while True:
    try:
        works = input().split()
        num_work += len(works)
        for task in works:
            if task in work:
                work[task] += 1
        if len(works) == 0:
            break
    except EOFError:
        break
for task, times in work.items():
    print(f'{task} {times} {times/num_work:.2f}')
print(f'Total {num_work} 1.00')