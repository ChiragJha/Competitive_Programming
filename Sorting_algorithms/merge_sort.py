# Merge sort divides the array in almost equal halves and then recursively does the same until 1 element remains on
# the right and left half, then it uses the merge_sorted_arrays function which takes O(n) time to merge to sorted
# arrays. The call stack takes O(n) space as well and not moore because stacks and deallocated when returning values
# There are log2(n) levels of calls made for the halving process which eventually leads to the merging of the two halves
# Time complexity = O(nlogn)
# Space complexity = O(n)
# Stability = If merging function is sorted, then the algo is stable as well
# Inplace = Usually not but the below implementation is a inplace implementation

def merge_sorted_arrays(low, mid, high, arr):
    a = arr[low:mid + 1]
    b = arr[mid + 1:high + 1]

    i = 0
    j = 0
    loop = low
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[loop] = a[i]
            i += 1
        else:
            arr[loop] = b[j]
            j += 1
        loop += 1

    while (i < len(a)):
        arr[loop] = a[i]
        i += 1
        loop += 1
    while (j < len(b)):
        arr[loop] = b[j]
        j += 1
        loop += 1

    return


def merge_sort(low, high, arr):
    if high > low:
        mid = (low + high) // 2
        merge_sort(low, mid, arr)
        merge_sort(mid + 1, high, arr)
        merge_sorted_arrays(low, mid, high, arr)
    return


a = [1, 9, 19]
b = [4, 14, 24]
low = 0
high = len(a) + len(b) - 1
mid = (low + high) // 2
arr = [10, 10, 5, 40, 15, 7, 1, -1, 0]
arr_merge_test = [*a, *b]
merge_sorted_arrays(0, mid, high, arr_merge_test)
print(arr_merge_test)
merge_sort(0, 8, arr)
print(arr)
