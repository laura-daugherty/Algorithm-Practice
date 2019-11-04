# middle = len(arr) / 2 = 20 / 2 = 10
# arr[10] = 15? # nope, check if greater than or less than
# arr[10] > 15? # nope, eliminate LHS of array, continue searching RHS
# middle = len(arr[11: ]) / 2 = 9 / 2 = 4 .  # integer division
# arr[11 + 4] = 15? # yes! we can return the index where the target value can be found


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]