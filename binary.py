arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(arr, target):
  for i in range(0, len(arr)):
    if arr[i] ==target:
      return i
    return -1

print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


def binary_search(arr, target):
  low = 0
  high = len(arr)-1
  while low <= high:
    middle = (low+high)/2
    if target < arr[middle]:
      high = middle-1
    elif target > arr[middle]:
      low = middle+1
    else:
      return middle
  return -1

print(binary_search(arr, 3))