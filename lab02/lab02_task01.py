def swap(list, i,j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
    
def isSorted(list):
    for i in range(len(list)):
        if(list[i][1] > list[i-1][1]): 
            break
    return (i == len(list))

def insertion_sort(list):
    n = len(list)
    value = None
    position = None
    
    for i in range(n):
        value = list[i][1]
        position = i
        if(isSorted(list)):
            break
        while (position > 0 and list[position - 1][1] < value):
            swap(list, position, position-1)
            position -= 1

n = int(input())
names = [item for item in input().split()]
scores = [int(item) for item in input().split()]

nameScore = list(zip(names, scores))

insertion_sort(nameScore)

sortedNames = []
sortedScores = []

for i in range(len(nameScore)):
    sortedNames.append(nameScore[i][0])
    sortedScores.append(nameScore[i][1])

print(sortedNames)
print(sortedScores)

for i in range(len(nameScore)):
    if (sortedScores[i] > 500) and i < 5:
        print(sortedNames[i])

# print(sortedNames)
# print(sortedScores)

# for i in range(len(brave)):
#     print(brave[i])

    
# print(n)
# print(names)
# print(scores)
# print(nameScore)
# print(sortedScoreList)