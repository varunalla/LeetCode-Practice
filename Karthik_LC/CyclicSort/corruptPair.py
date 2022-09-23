def find_corrupt_numbers(nums):
  # TODO: Write your code here

  size = len(nums)
  i = 0

  while i < size:
    j = nums[i] - 1

    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
    
  for i in range(size):
    if nums[i] != i + 1:
      return [nums[i], i + 1]
  
  return [-1,-1]
