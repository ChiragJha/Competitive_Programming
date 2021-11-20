"""
This algo. starts by picking up a pivot pivot element. The pivot element is one which has all elements less than in
towards its left and all the elements greater than it towards its right. The partition() function does this job. The
partition however does not implement sorting. Once, pivot is found, we need to sort the elements towards the right
and left side of it. We use recursion for this. Since, recursion will keep on going, we need a base case to exit the
recursive calls. This is = left>=right. Usually, while recursion continues you will reach a point where you only have
either one or two elements. And this would be sorted, because only one element exists. Similar to merge sort here.

Time complexity = Worst case, when array is already sorted or has duplicates so that pivot is at the end and we traverse
the array n2 times. = O(n2)
Average case - O(nlogn) this happens when pivot is near the middle. Almost like binary search/ merge sort
Stable = not stable
In-place = Yes
"""


def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(left, right, arr):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            swap(i, j, arr)
    swap(i + 1, right, arr)
    return i + 1


def quick_sort(left, right, arr):
    if left >= right:
        return
    pivot = partition(left, right, arr)
    quick_sort(left, pivot - 1, arr)
    quick_sort(pivot + 1, right, arr)


def quickSort(arr):
    quick_sort(0, len(arr) - 1, arr)


dummy_data = [2, 10, 20, 1, -1, 15]
quickSort(dummy_data)
print(dummy_data)
