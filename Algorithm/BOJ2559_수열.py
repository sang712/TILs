"""
슬라이딩 윈도우를 학습하기 위한 두번째 문제로
어느정도의 대략적인 감은 잡은 것 같음

K 길이 만큼 온도를 모두 더하여 새로운 리스트에 넣도록 하였고
한 칸씩 이동하면서 이전 것은 빼고 다음 것은 더하는 방식으로
굳이 한 번 참조했던 곳을 다시 보지 않도록 하였음

마지막에는 새로운 리스트에서 가장 큰 값을 출력하도록 하였음
"""
N, K = map(int, input().split())

temperatures = list(map(int, input().split()))

i, j = 0, K
serial_temperature = sum(temperatures[i:j])
serial_temperatures = [serial_temperature]
while j < N:
    serial_temperature += temperatures[j] - temperatures[i]
    serial_temperatures.append(serial_temperature)
    i += 1
    j += 1
print(max(serial_temperatures))