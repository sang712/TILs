'''
피보나치 함수를 문제에 작성된 대로 구현한 후 시간 절약을 위해서 딕셔너리를 사용함
그 후에 출력해야하는 0과 1의 호출 회수에 따라 해당 회수도 딕셔너리에 추가하였음
zip을 이용해서 간단하게 리스트간의 덧셈을 하였는데 
튜플 구조의 경우 결과물이 object형으로 나오기 때문에 list를 사용해야함
'''
import sys
input = sys.stdin.readline

memoFibonacci = {0: [0, 1, 0], 1: [1, 0, 1]}
def fibonacci(n):
    if n in memoFibonacci:
        return memoFibonacci[n]
    else:
        tempFibonacci = [x+y for x, y in zip(fibonacci(n-1), fibonacci(n-2))]
        memoFibonacci[n] = tempFibonacci
        return memoFibonacci[n]
    
T = int(input())
for tc in range(T):
    N = int(input())
    global zero, one
    zero, one = 0, 0
    print(*fibonacci(N)[1:])