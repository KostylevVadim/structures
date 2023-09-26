
from my_types.hashtable import Hashtable, Hashtable_new
from my_types.cache import Cache
from my_types.binary_tree import BinaryTree

x = Cache([1,2,2,3,3,3,4,4,4,4,3,3,3,3,3],3)

x.load_from_json()
print(x)



