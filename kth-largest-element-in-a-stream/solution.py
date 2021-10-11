"""
URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/

After submitting this solution:
Runtime: 92 ms, faster than 93.23% of Python3 online submissions.
Memory Usage: 18.3 MB, less than 75.71% of Python3 online submissions.
"""
import heapq


class KthLargest:
  def __init__(self, k: int, nums: list[int]):
    self.k = k
    self.nums = sorted(nums, reverse=True)[:k]
    heapq.heapify(self.nums)

    while len(self.nums) > k:
      heapq.heappop(self.nums)

  def add(self, val: int) -> int or None:
    heapq.heappush(self.nums, val)

    if len(self.nums) > self.k:
      heapq.heappop(self.nums)

    return self.nums[0]


if __name__ == '__main__':
  solution_object = KthLargest(2, [0])
  result = solution_object.add(-1)
  print(result, type(result))
  result = solution_object.add(1)
  print(result, type(result))
  result = solution_object.add(-2)
  print(result, type(result))
  result = solution_object.add(-4)
  print(result, type(result))
  result = solution_object.add(3)
  print(result, type(result))
