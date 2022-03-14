'''
연속된 값이 변하는지 판단하여 바뀌는 횟수를 체크하였고
바뀌는 횟수의 몫(대략)을 구하여 출력하였음
'''

S = input()

tmp = ''
relay = 0
for char in S:
    if tmp == '':
        tmp = char
        continue
    if char == tmp:
        continue
    else:
        relay += 1
        tmp = char

# round를 쓰면 오차가 발생할 수 있으므로 relay에 1을 더해서 몫을 취하는 것으로 하였음
print((relay+1)//2)