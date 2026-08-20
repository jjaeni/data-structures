from hash_table import HashTable

H = HashTable()

H.set(1)
H.set(11)
H.set(21)
H.set(2)

print(H)

H.remove(1)
print(H)

print(H.search(1))

H.set(3)
H.set(31)
H.set(13)

print(H)

H.remove(11)
print(H)

print(H.search(33))