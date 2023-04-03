"""
풀어보려는 문제중에 슬라이딩 윈도우 문제가 나와서 
어떻게 푸는지 감을 잡아보고자 쉬운 문제에 접근해보았음

머릿속에서 생각하는 것처럼 필터의 크기만큼 딱 값을 뽑아내 바로 연산을 처리하면 좋으련만
그렇지 못해 2중 for문을 돌렸고, 필터를 옮기기 위해 while문으로 바깥쪽을 감싸주었음
그 후에는 뽑아온 값을 정렬에 중앙값을 변환된 이미지에 저장하여 출력하였음

여기에서의 슬라이딩 윈도우는 내가 언급한 이미지 프로세싱에서 쓰는 필터라는 개념일테고 
필터의 크기는 W * W, 필터를 거친 결과물의 크기는 size_r * size_c
슬라이딩 윈도우는 특정 범위의 값을 추출해 해당 부분에서만 연산을 처리하는 것이라는 결론이 나옴

그럼에도 아까 본 A와 B로만 이루어진 연속된 문자열을 A가 모두 뭉치게끔 배열하는 문제에
어떻게 적용해야할지 감이 아직도 잡히지 않음
"""
import sys
input = sys.stdin.readline

M, N, K, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

size_r, size_c = M - W + 1, N - W + 1
B = [[0] * (size_c) for _ in range(size_r)]

cnt = 0
length = size_r * size_c
while cnt < length:
    br, bc = cnt // size_c, cnt % size_c
    temp = []
    for r in range(br, br + W):
        for c in range(bc, bc + W):
            temp.append(A[r][c]) 
    B[br][bc] = sorted(temp)[W ** 2//2]
    cnt += 1
    
for row in B:
    print(*row, sep=' ')