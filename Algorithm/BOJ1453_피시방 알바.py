N = int(input())
people = list(map(int, input().split()))
seated = set()

ans = 0
for person in people:
    if person in seated:
        ans += 1
    else:
        seated.add(person)
        
print(ans)