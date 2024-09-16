def count_vowels(S):
    vowels = "aeiou"  # Set of vowels
    count = 0
    
    for char in S:
        if char in vowels:
            count += 1
    
    return count

N = int(input())  
S = input().strip()

print(count_vowels(S))
