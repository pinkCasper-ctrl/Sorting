def selectionSort(arr):
    n=len(arr)
    for item in range(n-1):
        min_index=item
        for j in range(item+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
                
            arr[item], arr[min_index]=arr[min_index], arr[item]
            
def printArray(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__=="__main__":
    arr=[64,25,12,22,11]
    
    print("Original array: ", end=" ")
    printArray(arr)
    selectionSort(arr)
    print("Sorted array: ", end=" ")
    printArray(arr)
  
