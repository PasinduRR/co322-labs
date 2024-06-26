def swap(list, i,j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
    
def isSorted(list):
    for i in range(len(list)):
        if(list[i] > list[i-1]): 
            break
    return (i == len(list))

def insertion_sort(list):
    n = len(list)
    value = None
    position = None
    
    for i in range(n):
        value = list[i]
        position = i
        if(isSorted(list)):
            break
        while (position > 0 and list[position - 1] > value):
            swap(list, position, position-1)
            position -= 1
            
def binarySearch(list, value):
    low = 0
    high = len(list) - 1
    for i in range(len(list)):
        mid = low + (high - low) // 2
        # print("low",low,"\nhigh",high,"\nmid",mid)
        if(list[mid] == value):
            return mid
        elif(list[mid] > value):
            high = mid - 1
        else:
            low = mid + 1
    return -1

S = int(input())
N = int(input())
strength_arr = [int(item) for item in input().split()]

insertion_sort(strength_arr)
# print(strength_arr)
result = binarySearch(strength_arr, S)
if(result != -1):
    print("Bicorn Horn is present at index", result)
else:
    print("Bicorn Horn is not found!")
