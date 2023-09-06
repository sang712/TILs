M = int(input())
N = int(input())

square_number = []
for i in range(int(M ** 0.5), int(N ** 0.5) + 1):
    i_square = i ** 2
    if M <= i_square <= N:
        square_number.append(i ** 2)

if square_number:
    print(sum(square_number))
    print(square_number[0])
else:
    print(-1)