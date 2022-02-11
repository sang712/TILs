while True:
    num = int(input())
    if num == 0:
        break

    temp = num
    palindrome = 0
    while temp:
        palindrome = palindrome * 10 + (temp % 10)
        temp //= 10
    if palindrome == num:
        print('yes')
    else:
        print('no')