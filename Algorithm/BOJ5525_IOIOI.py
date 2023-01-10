'''
처음에는 2N+1 길이의 IOI패턴을 만들어서 비교하려고 했는데 이렇게 되면
O(N*M)의 시간복잡도가 되어 50점밖에 얻지 못한다는 것을 알게 되었음
그래서 답을 찾아본 결과 패턴이 반복되기 때문에
패턴이 얼마큼 반복되는지 확인하면서 N번 만큼 반복되면 카운트를 하면 된다고 하여서
해당 방식으로 구현하였음

어떻게 보면 KMP 방법과 비슷하다는 느낌
KMP를 완벽히 학습한 것은 아니고 어떤 원리인지 파악했던 것을 기반으로 생각했을 때
KMP는 패턴상에서 반복되는 부분이 있다면 그것을 체크해두고 주어진 문자열과 비교할 때 건너뛰는 방식인데
다음 코드는 패턴을 찾았을 때 두 칸을 건너뛰기 때문에 비슷하다고 생각이 들었음

방법을 떠올리기 어려운 문제였음
'''
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input()

cnt = 0
num_of_serial_IOI = 0
i = 0
while i < M:
    if S[i:i+3] == 'IOI':
        num_of_serial_IOI += 1
        if num_of_serial_IOI == N:
            num_of_serial_IOI -= 1
            cnt += 1
        i += 1
    else:
        num_of_serial_IOI = 0    
    i += 1
print(cnt)