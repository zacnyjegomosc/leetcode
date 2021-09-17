"""
URL: https://leetcode.com/problems/valid-parentheses/

After submitting this solution:
Runtime: 24 ms, faster than 96.33% of Python3 online submissions.
Memory Usage: 14.2 MB, less than 86.44% of Python3 online submissions.
"""


class Solution:
  def isValid(self, string: str) -> bool:
    close_brackets = {
      '(': ')',
      '{': '}',
      '[': ']'
    }
    open_brackets = set(close_brackets.values())

    last_open_brackets: list = list()

    for char in string:
      if char in close_brackets:
        last_open_brackets.append(char)
        continue

      if char in open_brackets:
        if len(last_open_brackets) == 0:
          return False

        if char != close_brackets[last_open_brackets.pop()]:
          return False

    if len(last_open_brackets) > 0:
      return False

    return True


if __name__ == '__main__':
  solution_object = Solution()
  result = solution_object.isValid("{[]}")
  print(result, type(result))
