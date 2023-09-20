from collections import namedtuple, ChainMap, Counter, OrderedDict

def named_tuple():
    Point = namedtuple('Point','x1, x2, x3')
    x = Point(1,2, 3)
    z = []
    for i in range(5):
        s = ''
        for j in range(1,i+1):
            s+='x'+str(j)+' '
        P = namedtuple('PointV'+str(i), s)
        print(s)
        z.append(P)
    try:
        y = z[1](1)
        print(y)
        y = z[2](1,2)
        print(y)
        y = z[3](1,2,3)
        print(y)
        y = z[4](1,2,3,4)
        print(y)
    except Exception as e:
        print(e)
    finally:
        print('конец')

def c_map(d1: dict, d2: dict):
    d_sum = ChainMap(d1,d2)
    x =d_sum.new_child({5:6, 7:8})
    return x


def c(list: list):
    return Counter(list)

def or_dic(tup: list):
    return OrderedDict(tup)


    


