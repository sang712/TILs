def calculate_prize_money(N):
    # Case 1: 22% tax on the total prize
    case1 = int(N * 0.78)
    
    # Case 2: 80% is necessary expenses, 22% tax on the remaining 20%
    case2 = int(N * (0.80 + (0.20 * 0.78)))
    
    # Output results
    print(case1, case2)
    
N = int(input())  # Input prize money
calculate_prize_money(N)
