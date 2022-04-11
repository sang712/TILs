vowels = ['a','e','i','o','u']

while True:
    password = input()
    acceptable = False
    if password == 'end':
        break

    vowel = 0
    consonant = 0

    for char in vowels:
        if char in password:
            acceptable = True
            break
        else:
            acceptable = False

    if not acceptable:
        print(f'<{password}> is not acceptable.')
        continue

    for i in range(len(password)):
        char = password[i]
        if char in vowels:
            vowel += 1
            consonant = 0
        else:
            consonant += 1
            vowel = 0
        if consonant >= 3 or vowel >= 3:
            acceptable = False
            break
        
        if i > 0 and char == password[i-1]:
            if char == 'e' or char == 'o':
                continue
            else:
                acceptable = False
                break

    if not acceptable:
        print(f'<{password}> is not acceptable.')
    else:
        print(f'<{password}> is acceptable.')