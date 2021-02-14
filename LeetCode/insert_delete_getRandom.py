import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.structure = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.structure:
            return False
        else:
            self.structure.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.structure:
            self.structure.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.structure:
            temp = random.sample(self.structure,k=1)
            return temp[0]