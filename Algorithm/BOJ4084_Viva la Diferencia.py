def transformation_steps(a, b, c, d):
    steps = 0
    # Continue until number sme
    while not (a == b == c == d):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        steps += 1
    return steps

# Read input until found jiro
while True:
    inputs = list(map(int, input().split()))
    
    #4 jiros, out 
    if inputs == [0, 0, 0, 0]:
        break
    
    # Unpack the input values into a, b, c, d
    a, b, c, d = inputs
    
    # Get the number of steps
    result = transformation_steps(a, b, c, d)
   
    print(result)
