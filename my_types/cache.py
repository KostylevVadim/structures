from collections import Counter
class Cache():
    def __init__(self, data: list, limit :int):
        x = {data.count(data[i]): data[i] for i in range(len(data))}
        print(x)
