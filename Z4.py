class FlattenIterable:
    def __init__(self, n_list):
        self.n_list = n_list

    def __iter__(self):
        return FlattenIterator(self.n_list)

class FlattenIterator:
    def __init__(self, n_list):
        self.iter_stack = [iter(n_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.iter_stack:
            try:
                elem = next(self.iter_stack[-1])
                if isinstance(elem, list):
                    self.iter_stack.append(iter(elem))
                else:
                    return elem
            except StopIteration:
                self.iter_stack.pop()
        raise StopIteration

# Пример использования
n_list = [0, [1, [2, 3], 4], 5]
flattened = FlattenIterable(n_list)
for num in flattened:
    print(num, end=' ')
print()
for num in flattened:
    print(num, end=' ')
print()
