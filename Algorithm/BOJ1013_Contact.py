"""
정규식을 사용하지 않고 그냥 구현하여 풀이하였음
우선 01로 시작하는 부분은 없애고
10으로 시작할 때 0이 적어도 한 번 등장하면서 반복되는 0을 체크하고
1이 적어도 한 번 등장하면서 반복되는 1을 체크한 뒤에
만약 뒤에 00으로 시작되고, 앞에는 11로 끝났었다면 
이전에 반복된다고 체크했던 1을 다시 사용할 수 있도록 index를 하나 물리도록 하는 방식으로 구현하였음
"""
import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    radio_wave = input().strip()
    length = len(radio_wave)
    i = 0
    while i < length:
        if i+1 < length and radio_wave[i] =='0' and radio_wave[i+1] == '1':
            i += 2
        elif i+1 < length and radio_wave[i] == '1' and radio_wave[i+1] == '0':
            i += 2
            if i < len(radio_wave) and radio_wave[i] == '0':
                    i += 1
            else:
                ans.append('NO')
                break
            while i < len(radio_wave):
                if radio_wave[i] == '0':
                    i += 1
                else:
                    break
                
            if i < len(radio_wave) and radio_wave[i] == '1':
                    i += 1
            else:
                ans.append('NO')
                break
            while i < len(radio_wave):
                if radio_wave[i] == '1':
                    i += 1
                else:
                    break
            if radio_wave[:i].endswith('11') and radio_wave[i:].startswith('00'):
                i -= 1
        else:
            ans.append('NO')
            break
    else:
        ans.append('YES')
print(*ans, sep='\n')