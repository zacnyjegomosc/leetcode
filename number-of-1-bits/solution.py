"""
URL: https://leetcode.com/problems/number-of-1-bits/

After submitting this solution:
Runtime: 28 ms, faster than 88.82% of Python3 online submissions.
Memory Usage: 13.9 MB, less than 99.81% of Python3 online submissions.
"""


class Solution:
  def hammingWeight(self, n: int) -> int:
    weight = 0
    for index in range(32):
      if n & (1 << index):
        weight += 1

    return weight


if __name__ == '__main__':
  solution_object = Solution()
  result = solution_object.hammingWeight(0o0000000000000000000000000001011)
  print(result, type(result))
