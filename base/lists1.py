heap = [2.2, -6, 'cde', [0.1, 0.2], '']

print(heap)
print(type(heap))
print(id(heap), end='\n\n')

print(heap[0], type(heap[0]), sep='\t\t')
print(heap[2], type(heap[2]), sep='\t\t')
print(heap[3], type(heap[3]), sep='\t', end='\n\n')

print(repr(heap[2][1]), end='\n\n')
# heap[2][1]
# 'cde'[1]
# 'd'

heap[-1] = 'last element'
print(heap)
print(id(heap), end='\n\n')

heap = heap + [1]
# heap += [1]
print(heap)
print(id(heap), end='\n\n')

heap.append(2)
print(heap)
print(id(heap), end='\n\n')

heap_copy = heap.copy()
print(heap_copy)
print(id(heap_copy), end='\n\n')

heap_copy.extend(['a', 'b'])
print(heap_copy)
print(id(heap_copy), end='\n\n')

