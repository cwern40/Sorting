# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    if len(merged_arr) == 2:
        if arrA[0] < arrB[0]:
            merged_arr = [arrA[0], arrB[0]]
        else:
            merged_arr = [arrB[0], arrA[0]]
    else:
        merged_arr = []
        j = 0
        i = 0
        while j != len(arrB) and i != len(arrA):
            if arrA[i] < arrB[j]:
                merged_arr.append(arrA[i])
                i += 1
                if i == len(arrA):
                    merged_arr += arrB[j:]
            else:
                merged_arr.append(arrB[j])
                j += 1
                if j == len(arrB):
                    merged_arr += arrA[i:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
