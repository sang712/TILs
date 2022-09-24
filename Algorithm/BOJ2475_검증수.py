unique_number = list(map(int, input().split()))

ans = 0
for num in unique_number:
    ans += num ** 2
    
print(ans%10)