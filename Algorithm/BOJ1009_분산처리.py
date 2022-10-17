'''
딱 10대의 컴퓨터가 존재하기 때문에 원하는 답은 마지막 자리수임을 도출해낼 수 있었음
1부터 9까지 자리수의 제곱수의 1의 자리는 최대 길이가 4이므로 
거침없이 while문을 사용해서 해당 수의 제곱수의 1의 자리를 를 순서대로 갖는 리스트를 만들었고
지수를 해당 리스트의 길이로 나눈 나머지를 인덱스로 사용하여 결과를 냄

+) 10을 고려를 하지 않아서 틀렸음..
'''
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
        continue
    units = [a%10]
    num = a
    while True:
        num = num * a % 10
        if not num in units:
            units.append(num)
        else:
            break
    length = len(units)
    print(units[(b-1)%length])