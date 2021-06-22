"""To slow, it's not good enough implementation. It works, but it's terrible."""

class Solution:
  def oddEvenJumps(self, arr: list[int]) -> int:
    result = 1

    # Allocate empty array (TODO: poor memory management)
    len_of_arr = len(arr)
    odd = [None] * len_of_arr
    even = [None] * len_of_arr

    # Allocate array of 0-pairs (TODO: poor memory management)
    array_of_pairs = [[0, 0] for _ in range(len_of_arr)]
    array_of_pairs[-1] = [1, 1]
    for i in range(len_of_arr - 2, -1, -1):
      # For each element in external loop
      min_value, min_index, max_value, max_index = max(arr[i + 1:]) + 1, -1, min(arr[i + 1:]) - 1, -1,
      for j in range(i + 1, len_of_arr):
        # Internal loop - get min and max
        if arr[i] <= arr[j] < min_value:
          min_index = j
          min_value = arr[j]

        if arr[i] >= arr[j] > max_value:
          max_index = j
          max_value = arr[j]

      odd[i] = min_index
      even[i] = max_index

    for step in range(len_of_arr - 2, -1, -1):
      if odd[step] != -1:
        # Jump here, direction: odd -> even
        array_of_pairs[step][1] = array_of_pairs[odd[step]][0]

      if even[step] != -1:
        # Jump here, direction: even -> odd
        array_of_pairs[step][0] = array_of_pairs[even[step]][1]

      result += array_of_pairs[step][1]

    return result


if __name__ == '__main__':
  solution_object = Solution()
  array_of_ints = [5,1,3,4,2]
  resolution = solution_object.oddEvenJumps(array_of_ints)
  print(resolution, type(resolution))
