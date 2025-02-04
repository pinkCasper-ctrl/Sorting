def insertionSort(arr):
    for item in range(1,len(arr)):
        key=arr[item]
        j=item-1
        
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1 
            arr[j+1]=key
            
def printArray(arr):
    for item in range(len(arr)):
        print(arr[item], end=" ")
    print()
    
if __name__=="__main__":
    arr=[22,27,16,2,18,6]
    insertionSort(arr)
    printArray(arr)
