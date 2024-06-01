class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            self.start += 2
            if self.start >= self.end:
                raise StopIteration()
        return self.start


en = EvenNumbers(10, 25)
for i in en:
    print(i)

