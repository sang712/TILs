'''
행과 열을 나눠서 길을 찾도록 하였고 경사로를 세우는 것은 다른 함수를 새로 정의하여 사용하였음
높이가 차이가 나는 칸을 마주하였을 때 어느 칸이 더 작냐에 따라 방향이 결정되므로
해당 내용을 함수의 인자에 넣어 delta를 대신하였음
골드3 문제라고 하기엔 실수없이 잘 풀렸음
'''
N, L = map(int, input().split())

mapa = [list(map(int, input().split())) for _ in range(N)]

ROW, COL = 1, 2
def checking_a_line(RorC, r, c, d, h, installed):
    if RorC == ROW:
        for i in range(L):
            c += d
            if 0 <= c < N and not installed[c]:
                if mapa[r][c] == h:
                    installed[c] = 1
                    continue
            return False
        else:
            return True
    elif RorC == COL:
        for i in range(L):
            r += d
            if 0 <= r < N and not installed[r]:
                if mapa[r][c] == h:
                    installed[r] = 1
                    continue
            return False
        else:
            return True
    return False

cnt = 0
def moving():
    global cnt
    for i, row in enumerate(mapa):
        installed = [0] * N
        prevh = -1
        for j, h in enumerate(row):
            if j > 0:
                if prevh == h:
                    continue
                elif prevh+1 == h:
                    if not checking_a_line(ROW, i, j, -1, prevh, installed):
                        break
                elif prevh-1 == h:
                    if not checking_a_line(ROW, i, j-1, 1, h, installed):
                        break
                else:
                    break
            prevh = h
        else:
            # print(f'row{i}:', installed)
            cnt += 1
    for j, col in enumerate(zip(*mapa)):
        installed = [0] * N
        prevh = -1
        for i, h in enumerate(col):
            if i > 0:
                if prevh == h:
                    continue
                elif prevh+1 == h:
                    if not checking_a_line(COL, i, j, -1, prevh, installed):
                        break
                elif prevh-1 == h:
                    if not checking_a_line(COL, i-1, j, 1, h, installed):
                        break
                else:
                    break
            prevh = h
        else:
            # print(f'col{j}', installed)
            cnt += 1
moving()
print(cnt)