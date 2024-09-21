def determine_rulers():
    testCase = int(input())  
    for cnt in range(1, testCase + 1):
        s = input().strip()  
        lastChar = s[-1]  
        
        if lastChar == 'y' or lastChar == 'Y': #woho
            ruler = "nobody"
        elif lastChar in 'aeiouAEIOU':
            ruler = "a queen"
        else:
            ruler = "a king"
        
        print(f"Case #{cnt}: {s} is ruled by {ruler}.")

determine_rulers()
