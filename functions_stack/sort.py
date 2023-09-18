from my_types.stack import Stack
def stack_sort(x: Stack):
    temp = Stack()
    while x.isEmpty() == 0:
        l = x.pop()
        flag = 0
        while temp.isEmpty() == 0 and flag == 0:
            if temp.top() > l:
                m = temp.pop()
                x.push(m)
            else:
                flag = 1
        
        
        temp.push(l)
    
    


    return temp
