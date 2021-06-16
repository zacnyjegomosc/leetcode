class Solution:
  def makeCleanEmailAddress(self, email: str) -> str:
    # Remove substring between + and @
    clean_email = email
    if '+' in email:
      index_of_plus_sign = email.index('+')
      index_of_at_sign = email.index('@')
      clean_email = email[0:index_of_plus_sign] + email[index_of_at_sign:len(email)]

    index_of_at_sign_in_clean_email = clean_email.index('@')
    domain = clean_email[index_of_at_sign_in_clean_email:len(clean_email)]

    # Remove dots (".") from username and return it with domain
    return clean_email[0:index_of_at_sign_in_clean_email].replace('.', '') + domain

  def numUniqueEmails(self, emails: list[str]) -> int:
    # For each email - make it clean. List of clean emails cast to unique set and return the length of it.
    return len(set(map(self.makeCleanEmailAddress, emails)))


if __name__ == '__main__':
  solution_object = Solution()
  emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com",
            "a@google.com", "b@google.com"]
  resolution = solution_object.numUniqueEmails(emails)
  print(resolution, type(resolution))
