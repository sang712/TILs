def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

while True:
    line = input()
    if line == "#":
        break
    print(count_vowels(line))
