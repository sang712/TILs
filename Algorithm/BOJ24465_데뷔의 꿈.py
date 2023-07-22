"""
각각의 범위를 판단하여 해당 기간에 맞는 별자리를 반환하는 함수를 만들어서 풀이하였음
"""
import sys
input = sys.stdin.readline

def star_sign(m, d):
    if m == 1:
        if d <= 19:
            return 'Capricorn'
        if d >= 20:
            return 'Aquarius'
    elif m == 2:
        if d <= 18:
            return 'Aquarius'
        if d >= 19:
            return 'Pices'
    elif m == 3:
        if d <= 20:
            return 'Pices'
        if d >= 21:
            return 'Aries'
    elif m == 4:
        if d <= 19:
            return 'Aries'
        if d >= 20:
            return 'Taurus'
    elif m == 5:
        if d <= 20:
            return 'Taurus'
        if d >= 21:
            return 'Gemini'
    elif m == 6:
        if d <= 21:
            return 'Gemini'
        if d >= 22:
            return 'Cancer'
    elif m == 7:
        if d <= 22:
            return 'Cancer'
        if d >= 23:
            return 'Leo'
    elif m == 8:
        if d <= 22:
            return 'Leo'
        if d >= 23:
            return 'Virgo'
    elif m == 9:
        if d <= 22:
            return 'Virgo'
        if d >= 23:
            return 'Libra'
    elif m == 10:
        if d <= 22:
            return 'Libra'
        if d >= 23:
            return 'Scorpio'
    elif m == 11:
        if d <= 22:
            return 'Scorpio'
        if d >= 23:
            return 'Sagittarius'
    elif m == 12:
        if d <= 21:
            return 'Sagittarius'
        if d >= 22:
            return 'Capricorn'

aloha = set()
for _ in range(7):
    month, day = map(int, input().split())
    aloha.add(star_sign(month, day))
    
N = int(input())
candidates = []
for _ in range(N):
    m, d = map(int, input().split())
    if not star_sign(m, d) in aloha:
        candidates.append((m, d))
       
if candidates:
    candidates.sort(key=lambda x: (x[0], x[1])) 
    for candidate in candidates:
        print(*candidate)
else:
    print('ALL FAILED')