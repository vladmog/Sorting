# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code)
        for j in range(i+1, len(arr)):
          if arr[smallest_index] > arr[j]:
            smallest_index = j
        
        # TO-DO: swap
        smaller = arr[smallest_index]
        bigger = arr[cur_index]

        arr[i] = smaller
        arr[smallest_index] = bigger
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = False
    
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True
            
    if swapped:
        bubble_sort(arr)

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr