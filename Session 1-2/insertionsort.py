def insertionSort(arr):
    n = len(arr)
    #traversal
    for i in range (1, len(arr)):

        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

arr = [4, 2, 7, 1, 3, -2, 8]

insertionSort(arr) 

print("Insertion Sort - Sorted array")
for i in range (len(arr)):
    print("%d" % arr[i], end=" ")