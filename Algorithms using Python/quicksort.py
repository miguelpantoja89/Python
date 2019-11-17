def quicksort(L):
    if (len(L) < 2):
        return L
    else:
        first = L[0]  # pivot
        rest = L[1:] # see .txt to understand slice notation
        lo = [x for x in rest if x < first]
        hi = [x for x in rest if x >= first]
        return quicksort(lo) + [first] + quicksort(hi)


numbers = [0,4,5,3,2,1,6,8,7,9,10]

print(quicksort(numbers))