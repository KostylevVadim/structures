
from my_types.hashtable import Hashtable, Hashtable_new
from my_types.cache import Cache

x = Cache([1,2,3,4,5,6,1,1,2,3,4,], 8)
x.add(123)
for i in range(4):
    x.add(4)
x.add(54)
x.add(54)
x.add(1234)
x.add(1234)
x.add(5)
x.add(7)
print(x.get_least_requested())

