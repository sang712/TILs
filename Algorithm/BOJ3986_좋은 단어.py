'''
입력에서 \n을 포함하고 있어서 strip()함수를 사용해 잘라 주었고
전체 문자의 길이의 합이 100만을 넘지 않으므로 다음 코드의 반복이 50만이 되지 않으므로
다음과 같이 코드를 작성하였음

재채점으로 시간 초과가 났는데 생각해보니 
ABABABABABAABABABABABA 와 같은 경우는 시간이 엄청나게 소요됨
따라서 스택으로 한개씩 쌓고 비교하면서 제거하는 방향으로 
각 단어단 딱 길이 만큼 반복하도록 수정하기로 함
수정 후 통과 하였음
'''
import sys
input = sys.stdin.readline
N = int(input())
def check(string):
    stack = []
    for char in string: # 단어를 반복하면서
        # 스택이 비어 있다면 바로 채워주고
        # 비어있지 않을 때 마지막 값과 비교함
        # 비교했을 때 페어링이 되면 없애고 아니면 그냥 스택을 채움
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # 짝 맞추기가 끝났을 때 stack에 아직 값이 남아있다면 좋은 단어가 아님
    if stack:
        return 0
    return 1
        
cnt = 0    
for _ in range(N):
    cnt += check(input().strip())
print(cnt)