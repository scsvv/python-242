from random import randint

ll = [randint(0, 100) for i in range(12)]
print(ll)


def quicksort(arr):
    if arr: 
        pivot = arr[len(arr) // 2]

        below = [x for x in arr if x < pivot]
        eq = [x for x in arr if x == pivot] 
        above = [x for x in arr if x > pivot]

        return quicksort(below) + eq + quicksort(above)
           
    else:
        return arr

print(quicksort(ll))

