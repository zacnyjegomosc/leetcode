class Solution:
  @staticmethod
  def shuffle(array_of_ints: list[int], len_of_arr) -> list[int]:
    """Make it shuffle"""
    result_arr = [None] * len_of_arr
    local_list = list()
    for key in array_of_ints:
      while local_list and key > local_list[-1]:
        result_arr[local_list.pop()] = key
      local_list.append(key)
    return result_arr

  def oddEvenJumps(self, arr: list[int]) -> int:
    len_of_arr = len(arr)

    sorted_arr = sorted(range(len_of_arr), key=lambda key: arr[key])
    next_odd_item = Solution.shuffle(sorted_arr, len_of_arr)

    # sort * (-1)
    sorted_arr.sort(key=lambda key: -arr[key])
    next_even_item = Solution.shuffle(sorted_arr, len_of_arr)

    # Allocate False arrays (TODO: poor memory management)
    odd_steps = [False] * len_of_arr
    even_steps = [False] * len_of_arr

    # Mark end of arrays
    odd_steps[len_of_arr - 1] = True
    even_steps[len_of_arr - 1] = True

    for element in range(len_of_arr - 2, -1, -1):
      # Mark steps (increment and decrement)
      if next_odd_item[element] is not None:
        odd_steps[element] = even_steps[next_odd_item[element]]
      if next_even_item[element] is not None:
        even_steps[element] = odd_steps[next_even_item[element]]

    # Sum our "good indices", odd steps
    return sum(odd_steps)


if __name__ == '__main__':
  solution_object = Solution()
  array_of_ints = [5, 1, 3, 4, 2]
  resolution = solution_object.oddEvenJumps(array_of_ints)
  print(resolution, type(resolution))
