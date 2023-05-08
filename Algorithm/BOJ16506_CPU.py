"""
문제를 풀면서 2진화를 하는 방법을 다시 알게 되었음
"""
import sys
input = sys.stdin.readline

def to_bin4(n: int) -> str:
    output = ''
    while n > 0:
        output = str(n % 2) + output
        n //= 2
    while len(output) < 4:
        output = '0' + output
    return output

def to_bin3(n: int) -> str:
    output = ''
    while n > 0:
        output = str(n % 2) + output
        n //= 2
    while len(output) < 3:
        output = '0' + output
    return output

operation = ['ADD', 'SUB', 'MOV', 'AND', 'OR', 'NOT','MULT', 'LSFTL', 'LSFTR', 'ASFTR', 'RL', 'RR']

op_to_opcode = {}
for i in range(len(operation)):
    op_to_opcode[operation[i]] = to_bin4(i) + '00'
    if operation[i] != 'NOT':
          op_to_opcode[operation[i] + 'C'] = to_bin4(i) + '10'

N = int(input())
for _ in range(N):
    mcode = []
    opcode, rD, rA, rB_C = input().split()
    mcode.append(op_to_opcode[opcode])
    mcode.append(to_bin3(int(rD)))
    mcode.append(to_bin3(int(rA)))
    mcode.append(to_bin4(int(rB_C))) if opcode.endswith('C') else mcode.append(to_bin3(int(rB_C)) + '0')
    print(''.join(mcode))