'''
set() 다뤄 처음 입력한 사용자의 닉네임을 저장하고
ENTER가 입력될 때마다 set을 초기화 하는 방식으로 진행하도록 구현하였음
소요시간은 120ms
새로 초기화하는 대신 clear()를 사용했는데 시간이 더 오래걸림(150ms)
'''
import sys
input = sys.stdin.readline

N = int(input())

firstchat_list = set()
cnt = 0
for _ in range(N):
    record = input().strip()
    if record == 'ENTER':
        firstchat_list = set()
        # firstchat_list.clear()
    elif not record in firstchat_list:
        firstchat_list.add(record)
        cnt += 1
print(cnt)