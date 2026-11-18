
import time

class HashTable:
    def __init__(self, size=17):
        self.size = size
        self.table = [[] for _ in range(size)]

    def get_index(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key, value):
        index = self.get_index(key)
        bucket = self.table[index]

        for i, (old_key, _) in enumerate(bucket):
            if old_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def search(self, key):
        index = self.get_index(key)

        for old_key, value in self.table[index]:
            if old_key == key:
                return value

        return None


# Demonstrate collision
custom = HashTable()
custom.insert("AB", "SKU100")
custom.insert("BA", "SKU200")

print("COLLISION DEMONSTRATION")
print("Index of AB:", custom.get_index("AB"))
print("Index of BA:", custom.get_index("BA"))
print("Collision bucket:", custom.table[custom.get_index("AB")])

print("Search AB:", custom.search("AB"))
print("Search BA:", custom.search("BA"))

# Generate 100,000 SKUs
skus = [f"SKU{i:06d}" for i in range(100000)]

custom = HashTable(size=200003)
built_in = {}

for i, sku in enumerate(skus):
    custom.insert(sku, i)
    built_in[sku] = i

target = skus[-1]
repeats = 1000

start = time.perf_counter()
for _ in range(repeats):
    custom.search(target)
custom_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(repeats):
    built_in.get(target)
dict_time = time.perf_counter() - start

print("\nLOOKUP PERFORMANCE")
print("Total SKUs:", len(skus))
print("Lookup repetitions:", repeats)
print(f"Custom hash table: {custom_time:.6f} seconds")
print(f"Built-in dictionary: {dict_time:.6f} seconds")
