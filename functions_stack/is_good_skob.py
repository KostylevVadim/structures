from my_types.stack import Stack
def is_good_skob(str):
    x = Stack()
    l_fl = 0
    for el in str:
        if el in ['(', '[', '{']:
            l_fl = 0
            x.push(el)
        else:
            print('here', el, x.top())
            list_old = []
            flag = 0
            while x.isEmpty()==0 and flag ==0:
                if x.top() not in ['(', '[', '{']:
                    list_old.append(x.pop())
                else:
                    
                    if el == ')' and x.top() == '(':
                        flag = 1
                        print('here1')
                    elif el == ']' and x.top() == '[':
                        flag = 1
                    elif el == '}' and x.top() == '{':
                        flag = 1
                    else:
                        flag = 0
                        list_old.append(x.pop())
                        print('here2')
            if x.isEmpty()==1 and flag ==0:
                return 'NO'
            for i in list_old:
                x.push(i)
            l_fl = flag
    
    if l_fl == 1:
        return 'Yes'
    else:
        return 'No'

