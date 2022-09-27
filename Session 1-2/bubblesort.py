def bubbleSort(arr):
    n = len(arr)

    #traversal
    for i in range(n-1):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] =arr[j+1], arr[j]


arr =  [4,2,7,1,3,-2,8]

bubbleSort(arr)

print("Bubble Sort - Sorted array")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")