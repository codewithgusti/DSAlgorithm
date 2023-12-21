
# binary search 

def binary_search(arr,start,end,key):
    while start <= end:
        mid = start + (end - start)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid -1
    return -1 


array = [2,5,7,8,12,23,34,47,52,69]
number = 8
result = binary_search(array,0,len(array) -1 , number)
print(result)