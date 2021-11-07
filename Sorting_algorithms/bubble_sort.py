# Called bubble because it works as if the largest bubbles keep moving to the end based on their size and
# sort themselves accordingly. Then larger bubbles move to the end and they hold up the smaller ones in a sorted
# manner

# This algorithm compares adjacent elements and moves the largest element in each pass to the respective position.
# In the first pass, largest element is moved to the end. In the second pass, 2nd largest element is moved to the
# 2nd last position and so on. In n-1 passes, the array is sorted.

# Time complexity = O(n2)
# Space complexity = O(1)

def swap_places(array, index):
    temp = array[index + 1]
    array[index + 1] = array[index]
    array[index] = temp


def bubble_sort(array):
    for index_outer in range(len(array) - 1):
        # Since after each pass the last element is always sorted(largest), there is no need to compare.
        # optimising the second loop to neglect the last_index - current_pass
        # for index_inner in range(len(array)-1):
        is_swapped = False
        for index_inner in range(len(array) - index_outer - 1):
            if array[index_inner] > array[index_inner + 1]:
                # Further optimisation. If already sorted then stop the process and return array
                swap_places(array, index_inner)
                is_swapped = True
        # If no swapping happens, then it means that the array is sorted
        if not is_swapped:
            return array


# Define a test dataSet
array = [1, 10, 0, -1, 20]
print(bubble_sort(array))
