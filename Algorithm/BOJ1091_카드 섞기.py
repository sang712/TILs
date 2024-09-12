def solve():
    N = int(input())  # Number of cards (multiple of 3)
    P = list(map(int, input().split()))  # Desired player for each card
    S = list(map(int, input().split()))  # Shuffle sequence

    # Initial configuration: cycle between player 0, 1, and 2
    current = [i % 3 for i in range(N)]

    # Check configuration matches configuration (P)
    if current == P:
        print(0)
        return

    for shuffle_count in range(1, N+1):
        # Apply shuffle pattern
        current = [current[S[i]] for i in range(N)]
        
        # Check reached the target configuration
        if current == P:
            print(shuffle_count)
            return
        
        # If the current configuration returns to the original, no P
        if current == [i % 3 for i in range(N)]:
            print(-1)
            return
    
    # If no solution, -1
    print(-1)

solve()
