# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    iA = 0
    iB = 0
    skip = False

    for i in range (0, len(merged_arr)):
        if skip:
          print("Skip")
          skip = False
          continue
        if iA == len(arrA):
            merged_arr[i] = arrB[iB]
            iB += 1
            continue
        elif iB == len(arrB):
            merged_arr[i] = arrA[iA]
            iA += 1
            continue
        
        if arrA[iA] == arrB[iB]:
            merged_arr[i] = arrA[iA]
            merged_arr[i+1] = arrB[iB]
            iA += 1
            iB += 1
            skip = True
        elif arrA[iA] < arrB[iB]:
            merged_arr[i] = arrA[iA]
            iA += 1
        elif arrB[iB] < arrA[iA]:
            merged_arr[i] = arrB[iB]
            iB += 1
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0:
        return arr
        
    split_list = []
    def split(list):
        if len(list) == 1:
            split_list.append(list)
        else:
            middle = len(list)//2
            split(list[:middle]), split(list[middle:])
    split(arr)

    def assemble(arr):
        half_arr_length = len(arr)//2
        combined_arr = []
        if len(arr)%2 == 0:
            combined_arr = [0] * half_arr_length
        else:
            half_arr_length += 1
            combined_arr = [0] * half_arr_length

        for i in range (0, len(arr)):
            if i == len(arr)-1 and len(arr)%2 == 1:
                combined_arr[len(combined_arr)-1] = arr[i]
            elif i%2 == 0:
                combined_arr[i//2] = merge(arr[i], arr[i+1])
            else:
                continue

        if len(combined_arr) == 1:
            return combined_arr
        else:
            return assemble(combined_arr)
    

    return assemble(split_list)[0]




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
