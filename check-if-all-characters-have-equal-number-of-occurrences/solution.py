"""
URL: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

After submitting this solution:
Runtime: 36 ms, faster than 63.25% of Python3 online submissions.
Memory Usage: 14 MB, less than 96.34% of Python3 online submissions.
"""


class Solution:
  def areOccurrencesEqual(self, string: str) -> bool:
    discovered_chars = set()
    chars_db = dict()
    for char in string:
      if char in discovered_chars:
        chars_db[char] += 1
      else:
        chars_db[char] = 1
        discovered_chars.add(char)

    return min(chars_db.values()) == max(chars_db.values())


if __name__ == '__main__':
  solution_object = Solution()
  result = solution_object.areOccurrencesEqual('abcabc')
  print(result, type(result))
