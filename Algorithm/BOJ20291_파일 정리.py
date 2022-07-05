import sys

input = sys.stdin.readline
N = int(input())

extensions = dict()
for i in range(N):
    file = list(input().rstrip().split('.'))
    extension = file[1]
    extensions.setdefault(extension, 0)
    extensions[extension] += 1

extensions = list(extensions.items())
extensions.sort()

answer = ''
for extension, number in extensions:
    answer += extension + ' ' + str(number) + '\n'
print(answer)