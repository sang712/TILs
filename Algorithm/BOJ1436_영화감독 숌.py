'''
앞에 1~5, 6, 7~9 를 붙이고
뒤에는 앞에 붙은 수에 따라 자리수를 늘려가는 방식으로 진행할 수 있을 거 같은데
다음에 해보는 것으로
'''
N = int(input())

numberOfEnd = []
length = 0
num = 666
while length < N:
    if '666' in str(num):
        numberOfEnd.append(num)
        length += 1
    num += 1

print(numberOfEnd[N-1])