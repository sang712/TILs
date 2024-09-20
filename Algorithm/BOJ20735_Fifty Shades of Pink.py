N = int(input())
count = 0

for _ in range(N):
    package_name = input().strip().lower()
    
    if "pink" in package_name or "rose" in package_name:
        count += 1

if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
