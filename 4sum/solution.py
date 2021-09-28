"""
URL: https://leetcode.com/problems/4sum/

After submitting this solution:
Runtime: 92 ms, faster than 91.67% of Python3 online submissions.
Memory Usage: 13.9 MB, less than 99.39% of Python3 online submissions.
"""


class Solution:
  def fourSum(self, nums: list[int], target: int, how_many_elements_we_want: int = None) -> list[list[int]]:
    # Sort our numbers
    nums.sort()
    result_list = []

    # This is a "four sum" actually...
    if how_many_elements_we_want is None:
      how_many_elements_we_want = 4

    # Validation
    if len(nums) == 0 or nums[0] * how_many_elements_we_want > target or target > nums[-1] * how_many_elements_we_want:
      return result_list

    # In recursion way:
    if how_many_elements_we_want == 2:
      lowest_index = 0
      highest_index = len(nums) - 1

      while lowest_index < highest_index:
        current_sum = nums[lowest_index] + nums[highest_index]
        if current_sum < target or (lowest_index > 0 and nums[lowest_index] == nums[lowest_index - 1]):
          # Move and skip
          lowest_index += 1
          continue
        elif current_sum > target or (highest_index < len(nums) - 1 and nums[highest_index] == nums[highest_index + 1]):
          # Move and skip
          highest_index -= 1
          continue

        # Save
        result_list.append([nums[lowest_index], nums[highest_index]])

        # Move forward
        lowest_index += 1
        highest_index -= 1

      return result_list

    for index in range(len(nums)):
      if index == 0 or nums[index - 1] != nums[index]:
        for subset in self.fourSum(nums[index + 1:], target - nums[index], how_many_elements_we_want - 1):
          # Save
          result_list.append([nums[index]] + subset)

    return result_list


if __name__ == '__main__':
  solution_object = Solution()
  result = solution_object.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
  print(result, type(result))
