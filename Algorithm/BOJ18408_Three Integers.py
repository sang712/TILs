def find_majority(A, B, C):

    count_1 = [A, B, C].count(1)
    count_2 = [A, B, C].count(2)
    
    if count_1 > count_2:
        return 1
    else:
        return 2

A, B, C = map(int, input().split())  

print(find_majority(A, B, C))
