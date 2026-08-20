class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]


    def hash_function(self, key):
        return key % self.size


    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while self.keys[i] != None and self.keys[i] != key:
            i = (i+1)%self.size
            if (i == start):
                return 'FULL'
        return i


    def set(self, key, value = None):
        i = self.find_slot(key)

        if i == 'FULL':
            return None
        else:
            if self.keys[i] == key:
                self.values[i] = value

            elif self.keys[i] == None:
                self.keys[i] = key
                self.values[i] = value
        

    def remove(self, key):
        i = self.find_slot(key)
        j = i

        while True:
            self.keys[i] = None
            self.values[i] = None

            j = (j+1)%self.size
            if self.keys[j] == None:
                return key

            k = self.hash_function(self.keys[j])

            if not (i==k or i<k<=j or j<i<k or k<i<j):
                break

            self.keys[i] = self.keys[j]
            self.values[i] = self.values[j]
            i = j


    def search(self, key):
        i = self.find_slot(key)

        if self.keys[i] == key:
            return key
        else:
            return None