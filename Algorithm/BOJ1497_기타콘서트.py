import sys
input = sys.stdin.readline
N, M = map(int, input().split())

guitar_info = [input().split() for _ in range(N)]

def check_guitar(guitar_comb, idx_guitar, cnt_guitar):
    if idx_guitar >= N:
        return
    the_guitar = guitar_info[idx_guitar][1]
    
    check_guitar(guitar_comb.copy(), idx_guitar + 1, cnt_guitar)
    
    for i in range(M):
        if the_guitar[i] == 'Y':
            guitar_comb[i] += 1
              
    check_guitar(guitar_comb.copy(), idx_guitar + 1, cnt_guitar + 1)
    cnt_song = 0
    for comb in guitar_comb:
        if comb:
            cnt_song += 1
    
    max_song, min_guitar = max_song_min_guitar
    if cnt_song:
        if cnt_song > max_song or (cnt_song == max_song and cnt_guitar + 1 < min_guitar):
            max_song_min_guitar[0] = cnt_song
            max_song_min_guitar[1] = cnt_guitar + 1
    
max_song_min_guitar = [0, N + 1]
check_guitar([0] * M, 0, 0)
max_song, min_guitar = max_song_min_guitar
print(min_guitar if max_song else -1)