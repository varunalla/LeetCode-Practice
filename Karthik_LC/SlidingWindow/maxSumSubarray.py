import sys

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  wStart = 0
  wSum = 0
  maxSoFar = ~sys.maxsize

  arraySize = len(arr)

  for wEnd in range(arraySize):
    wSum += arr[wEnd]
    maxSoFar = max(wSum, maxSoFar)

    if(wEnd >= k - 1):
      wSum -= arr[wStart]
      wStart += 1
  
  return maxSoFar
