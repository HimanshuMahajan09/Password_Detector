import hashlib
import math
import bitarray

class BloomFilter:
    def __init__(self, n_items, false_positive_prob):
        self.size = self.get_size(n_items, false_positive_prob)
        self.hash_count = self.get_hash_count(self.size, n_items)
        self.bit_array = bitarray.bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            digest = int(hashlib.sha256((item + str(i)).encode()).hexdigest(), 16)
            index = digest % self.size
            self.bit_array[index] = True

    def check(self, item):
        for i in range(self.hash_count):
            digest = int(hashlib.sha256((item + str(i)).encode()).hexdigest(), 16)
            index = digest % self.size
            if not self.bit_array[index]:
                return False
        return True

    @staticmethod
    def get_size(n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return max(1, int(m))

    @staticmethod
    def get_hash_count(m, n):
        k = (m / n) * math.log(2)
        return max(1, int(k))
