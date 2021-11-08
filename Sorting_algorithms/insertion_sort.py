# Insertion sort maintains a sorted and an unsorted array. And we insert the element from unsorted array O(n)
# into the correct position in sorted array O(n) in each iteration. Initially, the first element is the sorted array
# and the rest of the array is the unsorted array. Then we keep expanding

# Time complexity = O(n2)  -->Best case array already sorted - O(n),  Worst case - array reversed -- O(n2)
# Space complexity = O(1)
# Stability = Stable

def insertion_sort(array):
    for index in range(1, len(array)):
        insertion_element = array[index]
        index_sorted: int = index - 1
        while index_sorted >= 0 and insertion_element < array[index_sorted]:
            array[index_sorted + 1] = array[index_sorted]
            index_sorted -= 1
        # We avoid swapping elements in the while loop to avoid operations. We just want to shift greater elements
        # and find an index to insert the insertion element at the end
        array[index_sorted + 1] = insertion_element
    return array


# Define a test dataSet
array = [1, 10, 0, -1, 20]
print(insertion_sort(array))
