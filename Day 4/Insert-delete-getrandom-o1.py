# Problem URL: https://leetcode.com/problems/insert-delete-getrandom-o1

import random
class RandomizedSet:

    def __init__(self):
        self.s = {}

    def insert(self, val: int) -> bool:
        if self.s.get(val):
            return False
        else:
            self.s[val] = 1
            return True
        

    def remove(self, val: int) -> bool:
        if self.s.get(val):
            del self.s[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.s)
        return list(self.s.items())[random.randint(0, n-1)][0]