class LinearSearch:
    """
    Linear Search Algorithm: 
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    def __init__(self, array, target):
        self.array = array
        self.target = target

    def search(self):
        if(len(self.array) == 0):
            raise Exception("Array is empty")
        for i in range(len(self.array)):
            if self.array[i] == self.target:
                return i
        return -1
    
    def __str__(self):
        try:
            index = self.search()
        except Exception as e:
            return f"LinearSearch: {e}"
        if index != -1:
            return f"LinearSearch: For array ={self.array} with target Value = {self.target}  Found at index {index}"
        return f"LinearSearch: For array ={self.array} with target Value = {self.target} Not Found" 
    


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    target = 5
    linear_search = LinearSearch(array, target)
    print(linear_search)
    