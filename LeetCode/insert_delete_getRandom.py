class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.data_val = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        else:
            self.data_val.append(val)
            self.data[val] = len(self.data_val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            last_element_val = self.data_val[-1] # 6
            last_element_index = self.data[last_element_val]-1 # index 2
            
            change_index = self.data[val]-1 # index 0
            
            self.data[last_element_val] = change_index+1 # 3-> 1
            self.data_val[last_element_index], self.data_val[change_index] = val, last_element_val
            
            self.data.pop(val)
            self.data_val.pop()
            
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.sample(self.data_val, k= 1)[0]
