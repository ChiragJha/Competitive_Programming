# Selection sort involves finding the min in each pass and placing it in the beginning. It is almost the opposite
# of bubble sort

# Time complexity = O(n2)
# Space complexity = O(1)
# Stability = unstable. How? When there are 2 identical values in the array and say they were ordered initially
# in lexicographic order although not sorted. So if arr = [90,10,90,0]. Here, the first 90 may represent marks of a
# student whose role number comes earlier. So after sorting we might want to keep the lexicographic order and the
# first 90 should come before the second one post sorting. This is if the algo were stable. However, with the
# selection sort the first 90 is swapped with 0 to the end of the array and hence the stability is broken. This
# would not happen with a bubble sort, which is stable, because adjacent elements are compared


def swap_places(array, index, index_outer):
    temp = array[index_outer]
    array[index_outer] = array[index]
    array[index] = temp


def selection_sort(array):
    for index_outer in range(len(array) - 1):
        minimum_index = index_outer
        for index_inner in range(index_outer + 1, len(array)):
            if array[index_inner] < array[minimum_index]:
                minimum_index = index_inner
        swap_places(array, minimum_index, index_outer)
    return array


# Define a test dataSet
array = [10, 2, 0, 9, 8]
print(selection_sort(array))
