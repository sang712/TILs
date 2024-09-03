import sys

for i in range(int(sys.stdin.readline())):
    startC = 100001  # Initialize to a value higher than any possible cost/weight ratio
    ans = 0
    exb = 0

    for j in range(int(sys.stdin.readline())):
        a, b = map(int, sys.stdin.readline().split())
        
        cost_per_weight = b / a
        
        if startC > cost_per_weight:
            startC = cost_per_weight
            exb = b
        elif startC == cost_per_weight:
            if exb > b:  
                exb = b

    # Output the best price found
    print(exb)
