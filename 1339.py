import sys

size=int(sys.stdin.readline())
save=[]
sol=0

for _ in range(size):
    save.append(sys.stdin.readline())

alphabet=[0]*26

for i in range(size):
    for j in range(len(save[i])-1):
        tmp=save[i][len(save[i]) - 2 - j]
        alphabet[ord(tmp)-ord('A')] += 10**j

alphabet.sort(reverse=True)

for i in range(0,10):
    sol += (9-i)* alphabet[i]

print(sol)