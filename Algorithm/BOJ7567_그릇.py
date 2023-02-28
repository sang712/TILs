bowls = input()

prev = ''
height = 0
for bowl in bowls:
    if bowl != prev:
        height += 10
    else:
        height += 5
    prev = bowl
    
print(height)