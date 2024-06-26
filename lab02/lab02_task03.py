import math

p, q = input().split()
p = int(p)
q = int(q)

l = [int(item) for item in input().split()] 
m = [int(item) for item in input().split()]

lcs = []
seq = []
match = 0


for i in range(p):
    for j in range(match, q):
        if (l[i] == m[j]):
            lcs.append(l[i])
            match = j + 1
            break
        elif not lcs:
            seq.append(lcs)
            lcs.clear()
            match = 0


# for i in range(match,min(p,q)):
#     for j in range(match, max(p,q)):
#         if l[i] == m[j]:
#             lcs.append(l[i])
#             match = j+1
#             if j != max(p,q) - 1:
#                 break
#         if j == max(p,q) - 1:
#             seq.append(lcs)
#             lcs = []
#             match = 0
            
        
    
for i in seq:
    print(i)