# if hash table is full resize table automatically to increase length


def hash(string, tablesize):
    sum = 0
    for pos in range(len(string)):
        sum = sum + ord(string[pos])

    return sum % tablesize


class HashTable:
    def __init__(self, size=11, toIncreaseBy=1):
        self.size = size
        # to increase size of new table by factor of one
        self.toIncreaseBy = toIncreaseBy
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def reimplement(self, key, data):
        """
        reimplement slots and data array
        with  new size value
        """
        tempSlots = self.slots[:]  ## temp. values
        tempData = self.data[:]

        self.size += self.toIncreaseBy

        self.slots = [None] * self.size
        self.data = [None] * self.size

        for k, d in zip(tempSlots, tempData):
            if k is not None:  # if not checked can give error with self.hashfunction
                self.put(k, d)

        self.put(key, data)

    def put(self, key, data):
        # count none in table : if NoneCount is 0 means our table is full
        NoneCount = sum(x is None for x in self.slots)
        if NoneCount == 0:
            self.reimplement(key, data)

        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)
print(H.data)
H.reimplement(22, "vina")
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20] = "duck"
print(H[20])
print(H[99])
