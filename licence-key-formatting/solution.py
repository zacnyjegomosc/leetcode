"""This is the most optimal way, in my opinion. It works."""


class Solution:
  def licenseKeyFormatting(self, licence_key: str, how_many_groups: int) -> str:
    # 'upper' is calling here because a 'licence_key' string is shortest at this point, and it is the fastest way.
    licence_key_without_dashes = licence_key.replace('-', '').upper()
    len_of_licence_key_without_dashes = len(licence_key_without_dashes)
    modulo_after_grouping = len_of_licence_key_without_dashes % how_many_groups

    # Allocate two variables for starting and ending key (for slicing).
    starting_key = 0
    ending_key = 0

    formatted_key = str()
    if modulo_after_grouping > 0:
      # 'modulo_after_grouping' is our 'ending_key', but I want to save some memory operations, and I don't reassign
      # this variable here.
      formatted_key += licence_key_without_dashes[starting_key:modulo_after_grouping]
      starting_key += modulo_after_grouping

    last_starting_key_position = len_of_licence_key_without_dashes - how_many_groups
    while starting_key <= last_starting_key_position:
      ending_key = starting_key + how_many_groups
      formatted_key += '-' + licence_key_without_dashes[starting_key:ending_key]
      starting_key = ending_key

    # In some edge cases, we have a dash at the beginning of our formatted_key. I can write 'if' in 'while' loop,
    # but I don't want it (for micro-optimization reasons).
    if formatted_key.startswith('-'):
      formatted_key = formatted_key[1:]  # Remove the first character from 'formatted_key'.

    return formatted_key


if __name__ == '__main__':
  solution_object = Solution()
  resolution = solution_object.licenseKeyFormatting("2-5g-3-J", 2)
  print(resolution, type(resolution))
