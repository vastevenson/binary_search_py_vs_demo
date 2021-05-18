def binary_search(arr, target):
    # this method returns the index of the target (-1 if target DNE in arr)
    # assume the array is already sorted
    l_index = 0
    r_index = len(arr) - 1
    while l_index <= r_index:
        midpoint_index = l_index + r_index // 2
        try: midpoint_val = arr[midpoint_index]
        except IndexError:
            return -1
        if midpoint_val == target:
            return midpoint_index
        elif midpoint_val < target:
            l_index += 1
        else:
            r_index -= 1
    # if we make it through while loop, then elem is not in array, return -1
    return -1

arr = [0,1,2,3,4,5,6,7,8,9]
target = 10
print('The target: {} was at position {} in array'.format(target, binary_search(arr, target)))