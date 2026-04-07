from collections import deque

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.buckets  = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        cur_freq = self.freq[val]

        if cur_freq not in self.buckets:
            self.buckets[cur_freq] = deque()
        self.buckets[cur_freq].append(val)

        if cur_freq > self.max_freq:
            self.max_freq = cur_freq

    def pop(self) -> int:
        bucket = self.buckets[self.max_freq]
        val = bucket.pop()

        self.freq[val] -= 1

        if len(bucket) == 0:
            self.max_freq -= 1

        return val
