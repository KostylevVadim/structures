
from collections_learner.named_tuple import named_tuple, c_map, c, or_dic

l1 = [1,2,3,4,5,6]
l2 = [9,9,8,7,6,5]
x = list(zip(l1,l2))
p = or_dic(x)

print(p[1])