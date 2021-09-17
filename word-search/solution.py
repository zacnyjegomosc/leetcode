"""
URL: https://leetcode.com/problems/word-search/

After submitting this solution:
Runtime: 6200 ms, faster than 64.02% of Python3 online submissions.
Memory Usage: 14.1 MB, less than 88.60% of Python3 online submissions.
"""


class Solution:
  def _dfs(self, board: list[list[str]], line_index: int, char_index: int, already_found_chars_count: int,
           word: str) -> bool:
    if already_found_chars_count == len(word):
      return True

    if line_index < 0 or line_index >= len(board) or char_index < 0 or char_index >= len(board[line_index]) or \
        board[line_index][char_index] != word[already_found_chars_count]:
      return False

    current_char = board[line_index][char_index]

    board[line_index][char_index] = None

    # Go to the bottom
    is_found: bool = self._dfs(board, line_index + 1, char_index, already_found_chars_count + 1, word)

    if not is_found:
      # Go to the top
      is_found = self._dfs(board, line_index - 1, char_index, already_found_chars_count + 1, word)

    if not is_found:
      # Go to the right
      is_found = self._dfs(board, line_index, char_index + 1, already_found_chars_count + 1, word)

    if not is_found:
      # Go to the left
      is_found = self._dfs(board, line_index, char_index - 1, already_found_chars_count + 1, word)

    board[line_index][char_index] = current_char
    return is_found

  def exist(self, board: list[list[str]], word: str) -> bool:
    for line_index, line in enumerate(board):
      for char_index, char in enumerate(line):
        if char == word[0] and self._dfs(board, line_index, char_index, 0, word):
          return True

    return False


if __name__ == '__main__':
  solution_object = Solution()
  result = solution_object.exist(board=[["A", "B", "C", "E"],
                                        ["S", "F", "C", "S"],
                                        ["A", "D", "E", "E"]],
                                 word="ABCCED")
  print(result, type(result))
