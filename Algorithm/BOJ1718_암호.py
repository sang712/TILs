# 메모리 127804KB, 시간 160ms
def solver():
    sentence = input()
    cipher_key = input()

    s_len = len(sentence)
    k_len = len(cipher_key)
    ans = ''
    for i in range(s_len):
        s_char = ord(sentence[i])
        k_char = ord(cipher_key[i%k_len])
        if s_char == 32:
            ans += ' '
        elif 97 <= s_char <= 122:
            ans_ord = s_char - (k_char-96) if s_char > k_char else s_char - (k_char-96) + 26
            ans += chr(ans_ord)
    print(ans)

solver()

# 메모리 129136KB, 시간 148ms
# def solver():
#     sentence = input()
#     cipher_key = input()
#
#     s_len = len(sentence)
#     k_len = len(cipher_key)
#     for i in range(s_len):
#         s_char = ord(sentence[i])
#         k_char = ord(cipher_key[i%k_len])
#         if s_char == 32:
#             print(sentence[i], end='')
#         elif 97 <= s_char <= 122:
#             ans = s_char - (k_char-96) if s_char > k_char else s_char - (k_char-96) + 26
#             print(chr(ans), end='')
#
# solver()