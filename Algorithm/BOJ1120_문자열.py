A, B = input().split()

len_A, len_B = len(A), len(B)

if len_A == len_B:
    diff = 0
    for i in range(len_A):
        if A[i] != B[i]:
            diff += 1
elif len_A < len_B:
    diff = 51
    for j in range(len_B - len_A + 1):
        temp_diff = 0
        for i in range(len_A):
            if A[i] != B[i + j]:
                temp_diff += 1
        diff = min(diff, temp_diff)
elif len_A > len_B:
    diff = 51
    for j in range(len_A - len_B + 1):
        temp_diff = 0
        for i in range(len_B):
            if A[i + j] != B[i]:
                diff += 1
        diff = min(diff, temp_diff)
print(diff)