def pair_with_targetsum(arr, target_sum):

  size = len(arr)
  left = 0
  right = size - 1

  while(left < right):
    if(arr[left] + arr[right] == target_sum):
      return [left,right]
    elif(arr[left] + arr[right] > target_sum):
      right -= 1
    else:
      left += 1

  return [-1, -1]
