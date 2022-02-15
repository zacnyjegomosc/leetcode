"""
URL: https://leetcode.com/problems/logger-rate-limiter/

After submitting this solution:
Runtime: 152 ms, faster than 72.67% of Python3 online submissions for Logger Rate Limiter.
Memory Usage: 20.7 MB, less than 26.96% of Python3 online submissions for Logger Rate Limiter.
"""

from collections import deque


class Logger(object):

  def __init__(self):
    self.log_messages_set = set()
    self.messages_queue = deque()

  def shouldPrintMessage(self, arriving_timestamp, arriving_message):
    while self.messages_queue:
      message_content, message_timestamp = self.messages_queue[0]
      if arriving_timestamp - message_timestamp < 10:
        break

      self.messages_queue.popleft()
      self.log_messages_set.remove(message_content)

    if arriving_message in self.log_messages_set:
      return False

    self.log_messages_set.add(arriving_message)
    self.messages_queue.append((arriving_message, arriving_timestamp))
    return True



if __name__ == '__main__':
  logger = Logger()
  print(logger.shouldPrintMessage(1, "foo"))
  print(logger.shouldPrintMessage(2, "bar"))
  print(logger.shouldPrintMessage(3, "foo"))
  print(logger.shouldPrintMessage(8, "bar"))
  print(logger.shouldPrintMessage(10, "foo"))
  print(logger.shouldPrintMessage(11, "foo"))
