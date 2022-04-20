n = int(input())
a = list(map(int, input().split()))
sumation = sum(a)
a.sort()
count = 0
for i in range(n-1):
    piece = a[i]
    sumation -= piece
    count += piece * sumation
print(count)