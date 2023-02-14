"""
문제에서 주어진대로 300초 60초 10초로 경우를 나누어 divmod를 적용해서
버튼의 횟수를 나누었고 남은 시간에 따라
다르게 출력하도록 하였음
"""
time = int(input())

button_A, time = divmod(time, 300)
button_B, time = divmod(time, 60)
button_c, time = divmod(time, 10)

print(-1) if time else print(button_A, button_B, button_c)