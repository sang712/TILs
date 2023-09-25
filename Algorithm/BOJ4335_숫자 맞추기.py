"""
문제의 요구사항대로 구현하였음
"""
import sys
input = sys.stdin.readline

ups = []
downs = []
lied = False
while True:
    num = int(input())
    if num == 0:
        break
    condition = input().strip()
    if condition == 'too high':
        ups.append(num)
    elif condition == 'too low':
        downs.append(num)
    elif condition == 'right on':
        for up in ups:
            if up <= num:
                lied = True
                break
        for down in downs:
            if down >= num:
                lied = True
                break
        print('Stan is dishonest' if lied else 'Stan may be honest')
        ups = []
        downs = []
        lied = False