"""
출력의 대소문자를 틀려서 여러번 틀린 문제로
문제를 풀어서 생각해보면 호 대신 변으로 생각하고
m개의 변으로 m각형을 만드는데, 이 때 다른 변들의 합 == 가장 큰 변 인 경우도 포함해라 임
그래서 작은 값부터 더해가면서 그 다음 값과 비교해서
더한 값이 크거나 같으면 YES를 아니면 NO를 출력하도록함

잠깐 삼각형만 검사하면 되지 않나 생각했었는데 
이러면 삼각형은 안되는데 사각형은 되는 경우가 있을 수 있기 때문에 안 됨

정렬 한 뒤, 해당 호보다 작은 모든 호의 지름을 다 더했을 때 해당 호보다 큰거나 같은지 확인하면 끝
"""
import sys
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    N = int(input())
    arcs = list(map(float, input().split()))
    arcs.sort()
    sumation = arcs[0]
    for i in range(1, N):
        if sumation >= arcs[i]:
            print('YES')
            break
        sumation += arcs[i]
    else:
        print('NO')