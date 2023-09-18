from my_types.stack import Stack

def evaluate(str):
    if str:
        stack=Stack()
        for elem in str:
            if elem.isdigit():
                stack.push(int(elem))
            else:
                
                b = stack.pop()
                a = stack.pop()
                if elem == '+':
                    stack.push(a+b)
                if elem == '-':
                    stack.push(a-b)
                if elem == '*':
                    stack.push(a*b)
                if elem == '/':
                    stack.push(a/b)
        return stack.top()