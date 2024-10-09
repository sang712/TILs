import math

# Function calculate the time required to destroy the wall
def calculate_destruction_time(n, s, p, points):
    total_length = 0
    
    # Calculate  total length of the wall
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        
        # Add  length of the segment hor or ver
        if x1 == x2:
            total_length += abs(y2 - y1)
        else:
            total_length += abs(x2 - x1)
    
    # Calculate the total hours 
    total_hours = math.ceil((total_length * s) / p)
    
    return total_hours

def main():
    K = int(input())  # no of datasets
    
    for data_set_num in range(1, K + 1):
        n, s, p = map(int, input().split())
        points = []
        
        for _ in range(n + 1):
            x, y = map(int, input().split())
            points.append((x, y))
        
        result = calculate_destruction_time(n, s, p, points)
        
        print(f"Data Set {data_set_num}:")
        print(result)
        print() 

if __name__ == "__main__":
    main()
