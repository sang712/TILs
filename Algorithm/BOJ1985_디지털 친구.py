def is_almost_friend(x, y):
    x = list(map(int, x))
    y = list(map(int, y))
    for i in range(len(x)-1):
        if not(i == 0 and x[i] == 1):
            x[i] -= 1
            x[i+1] += 1
            if is_friend(x, y):
                return True
            x[i] += 1
            x[i+1] -= 1
        
        x[i] += 1
        x[i+1] -= 1
        if is_friend(x, y):
            return True
        x[i] -= 1
        x[i+1] += 1
    
    for i in range(len(y)-1):
        if not(i == 0 and y[i] == 1):
            y[i] -= 1
            y[i+1] += 1
            if is_friend(x, y):
                return True
            y[i] += 1
            y[i+1] -= 1
        
        y[i] += 1
        y[i+1] -= 1
        if is_friend(x, y):
            return True
        y[i] -= 1
        y[i+1] += 1
    return False
        
def is_friend(x, y):
    if set(x) == set(y):
        return True
    return False

for _ in range(3):
    x, y = input().split()
    if is_friend(x, y):
        print('friends')
        continue
    if is_almost_friend(x, y):
        print('almost friends')
    else:
        print('nothing')