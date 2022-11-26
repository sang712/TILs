'''
분할 정복 방법으로 절반의 크기에 해당하는 부분으로 이동하여 판단하도록 하였음
분할 하다가 크기가 1일 때 해당 값을 바로 return하도록 하였고
return된 값들을 비교하여 모두 같으면 저장하는 방법으로 진행하였음
다 다른 경우여도 return 값은 있어야 된다고 생각해서 2를 추가해주었고
리스트에도 오류가 나지 않도록 2번 인덱스를 추가해주었음
'''
N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

# 하얀색, 파란색, 아무것도 아님 순
white_n_blue = [0, 0, 0]

def check_paper(size, r, c):
    if size == 1:
        return paper[r][c]
    
    half_size = size // 2
    
    left_up = check_paper(half_size, r, c)
    right_up = check_paper(half_size, r + half_size, c)
    left_down = check_paper(half_size, r, c + half_size)
    right_down = check_paper(half_size, r + half_size, c + half_size)
    
    if left_up == right_up == left_down == right_down:
        return left_up
    else:
        white_n_blue[left_up] += 1
        white_n_blue[right_up] += 1
        white_n_blue[left_down] += 1
        white_n_blue[right_down] += 1
        return 2
    
white_n_blue[check_paper(N, 0, 0)] += 1
for num in white_n_blue[:2]:
    print(num)
