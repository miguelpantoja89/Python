

def findSmallest(aray):
    small_elem = aray[0]
    small_index = 0
    for i in range(1,len(aray)):
        if aray[i] < small_elem:
            small_elem = aray[i]
            small_index = i
    return small_index


def select_sort(aray):
    newArray = []
    for i in range(len(aray)):
        small = findSmallest(aray)
        newArray.append(aray.pop(small))
    return newArray


print(select_sort([1,2,3,6,5,4]))