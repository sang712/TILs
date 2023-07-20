"""
정렬을 할 때 두번째 기준을 안 정하면 입력 순서대로 그대로 유지됨 유의할 것

문제를 풀기전에 생각한 방법이
하나는 셋을 둬서 없앨 때 편하게 없애고 출력할 때 
테이블 번호만 리스트로 출력하는 것이었고
다른 하나는 지금 풀이처럼 리스트를 둬서 시간 복잡도는 증가하겠지만
맘 편하게 코딩하는 것이었는데

돌이켜보면 삭제하는 과정에서 어차피 하나하나 for문을 돌면서 찾아야 하는 거였어서
맘 편하게 코딩하는 것을 선택하는 것이 맞았음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
order_list = []
for _ in range(N):
    command, *num = input().split()
    if command == 'order':
        order_list.append(list(map(int, num)))
    elif command == 'sort':
        order_list.sort(key=lambda x: (x[1], x[0]))
    elif command == 'complete':
        for i in range(len(order_list)):
            if order_list[i][0] == int(num[0]):
                order_list.pop(i)
                break
        
    output = []
    for table, time in order_list:
        output.append(table)
    print(*output) if output else print('sleep')