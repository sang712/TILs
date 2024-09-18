def find_cheapest_pack(n, packs):
    # Required digits for 2021
    required_digits = ['2', '0', '2', '1']
    
    min_price = float('inf')  # min price
    best_pack_index = 0
    
    for i in range(n):
        price, digits = packs[i]
        
        # Check if contin digits 2, 0, 2, 1
        if all(digits.count(digit) >= required_digits.count(digit) for digit in required_digits):
            if price < min_price:
                min_price = price
                best_pack_index = i + 1  
    
    # If no valid pack is found go bck 0
    if best_pack_index == 0:
        return 0
    
    return best_pack_index

# Input parsing and function call
n = int(input())  # how much pcks
packs = []

for _ in range(n):
    p, d = input().split()
    p = int(p)  
    packs.append((p, d))  

print(find_cheapest_pack(n, packs))
