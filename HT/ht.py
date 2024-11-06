class HashTable():
    def __init__(self, size:int = 7) -> None:
        self.data_map = [None] * size
        
    def __hash(self, keys):
        my_hash = 0
        for letter in keys:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
            
    def set_value(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
            
ht = HashTable()
ht.set_value("Shimul", 30)
ht.set_value("Shimul", 50)
ht.set_value("Sohan", 50)
print(ht.get_item("Sohan"))
# ht.print_table()