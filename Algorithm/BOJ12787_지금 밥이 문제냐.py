"""
8비트의 값은 최대 255의 값을 갖기 때문에
IP 주소를 하나의 수로 이어 붙인다면 .을 기준으로 한 수는 256의 단위차가 발생하게 됨
해서 256을 곱해주거나 나누는 방식으로 구현하여 문제를 풀었음
"""
for _ in range(int(input())):
    M, N = input().split()
    if M == '1':
        IP_address = list(map(int, N.split('.')))
        output_int = []
        for i in range(8):
            output_int.append(IP_address[7 - i] * (256 ** i))
        print(sum(output_int))
    else:
        IP_address = []
        input_int = int(N)
        for _ in range(8):
            IP_address.append(input_int % 256)
            input_int //= 256
        print(*IP_address[::-1], sep='.')