import sys
sys.stdin = open('input.txt')

L = int(input())
S = input()
ACGT = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for s in S:
    ACGT[s] += 1

print((ACGT['A']*ACGT['C']*ACGT['G']*ACGT['T'])%1000000007)