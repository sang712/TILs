N, M, K = map(int, input().split())

case = 0
if M < K:
    print(case)
else:
    for _ in range(N):
        seats = list(map(int, input()))
        temp = sum(seats[:K])
        if temp == 0:
            case += 1
        for i in range(M-K):
            temp -= seats[i]
            temp += seats[i+K]
            if temp == 0:
                case += 1
    print(case)