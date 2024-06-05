
class CustomHashTable:

    #  Custom Hash table implementation
    ###  Runtime of all operations is O(1) constant time
    ### unless poor hash function, high collision rate etc.

    def __init__(self, size=10):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    # Hashing function using length of hash table

    def hashing_key(self, key):
        return int(key) % self.size

    #  Adds package ID to hash table
    #  Prints an error statement if package ID already exists

    def add(self, key, value):

        hash_key = self.hashing_key(key)
        kv_pair = [key, value]

        if not any(kvp[0] == key for kvp in self.table[hash_key]):
            self.table[hash_key].append(kv_pair)
            return True
        else:
            print('Sorry but that ID already exists')
            return False

    #  Searches hash table for for package ID using the key
    #  if found, will return package ID
    
    def search(self, key):

        hash_key = self.hashing_key(key)
        bucket = self.table[hash_key]
        for kvp in bucket:
            if kvp[0] == key:
                return kvp[1]
            print(kvp)
        return None
    
    #  Searches hash table and deletes package ID if it exists, returns True
    #  else it will just return False
    
    def delete(self, key):
        hash_key = self.hashing_key(key)
        bucket = self.table[hash_key]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return True
        return False

    def __iter__(self):
        for bucket in self.table:
            for key, value in bucket:
                yield value  

    #  get all keys for easy extraction to cli methods
    #  O(n) runtime since we have to iterate through hash table in full one time for all keys

    def get_all_keys(self):
        keys = []
        for bucket in self.table:
            for kvp in bucket:
                keys.append(kvp[0])
        return keys