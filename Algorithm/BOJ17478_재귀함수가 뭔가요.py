"""
언더스코어가 아닌 하이픈으로 하여 문제를 틀렸었음
언더스코어로 수정하니 해결됨
"""
N = int(input())

recursive_ask = '"재귀함수가 뭔가요?"'
recursive_start = ['"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.', '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.', '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
recursive_answer = '"재귀함수는 자기 자신을 호출하는 함수라네"'
recursive_end = '라고 답변하였지.'
indent = '____'

def recursive(n):
    print(f'{indent*n}{recursive_ask}')
    if n < N:
        for sentence in recursive_start:
            print(f'{indent * n}{sentence}')
        recursive(n+1)
    elif n == N:
        print(f'{indent*n}{recursive_answer}')
    print(f'{indent*n}{recursive_end}')
    
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recursive(0)