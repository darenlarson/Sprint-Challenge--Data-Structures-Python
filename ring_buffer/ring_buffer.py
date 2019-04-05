class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # Replace the item in storage that's at index of current.
    self.storage[self.current] = item

    # Use self.current as a counter.
    # If self.current isn't at the end of the capacity, increment it.
    if self.current < self.capacity - 1:
      self.current += 1
    # If self.current is at the end of capacity, reset it to 0 since the item at index 0 is now the oldest item.
    else:
      self.current = 0

  def get(self):
    result = []

    # Copy over values that are not None in order from self.storage to result. Return result.
    for i in range(len(self.storage)):
      if self.storage[i] is not None:
        result.append(self.storage[i])

    return result