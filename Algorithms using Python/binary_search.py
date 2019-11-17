
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low<=high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else :
            low =  mid + 1
    return None


list1 = [1,5,7,9,14]

print(binary_search(list1,7))

#### And if the item doesn't exist

print(binary_search(list1,2))