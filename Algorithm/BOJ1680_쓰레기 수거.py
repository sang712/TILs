"""
문제에서 요구하는대로 구현하였음
쓰레기 차를 출발시켜 직전 위치와 현재 위치의 차를 이동거리에 포함시키고
쓰레기를 싣도록 함
쓰레기를 실을 때 가득 차면 돌아갔다 오고
딱 맞으면 돌아오고
남으면 그대로 둔 뒤에
다음 for문에 진입해서 쓰레기 차의 위치에 따라 직전 위치의 거리를 더해주는 방식으로 풀이하였음
"""
import sys
input = sys.stdin.readline

ans = []
for tc in range(int(input())):
    W, N = map(int, input().split())
    trash_spot = [tuple(map(int, input().split())) for _ in range(N)]
    
    travel, trash, prev_dist = 0, 0, 0
    is_at_dump = True
    for x, w in trash_spot:
        if is_at_dump:
            travel += prev_dist
            is_at_dump = False
        
        travel += x - prev_dist
        
        if trash + w < W:
            trash += w
        
        else:
            travel += x
            if trash + w > W:
                travel += x
                trash = w
                is_at_dump = False
            else:
                trash = 0
                is_at_dump = True
        
        prev_dist = x
    
    if not is_at_dump:
        travel += prev_dist
    
    ans.append(travel)
print(*ans, sep='\n')
    