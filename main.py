
def get_max_sub_array(arr):
    """
    Function to return the maximum sub array and its sum
    """
    if not all(isinstance(x, int) or isinstance(x, float) for x in arr):
        # If a char is contained in the array, raise a TypeError. 
        # The array must only contain numeric values.
        raise TypeError("Array must be of type int or float")
    elif len(arr) == 0:
        # if the array is empty, raise a ValueError.
        # The array needs to contain at least one element.
        raise ValueError("Array must not be empty")

    current_max, current_start, current_end = arr[0], 0, 0
    max_max, max_start, max_end = arr[0], 0, 0

    for i in range(len(arr)):

        current_max += arr[i]
        current_end = i

        if current_max > max_max:
            max_max = current_max
            max_start = current_start
            max_end = current_end

        elif current_max < 0:
            current_max = 0
            current_start = i + 1

    sub_array = arr[max_start:max_end + 1]
    return sub_array, sum(sub_array)