class Stack:
    def __init__(self, **kwargs):
        

        if kwargs.get('list'):
            
            self.__list = kwargs['list']
        else:
            
            self.__list = []

    
    def pop(self):
        a = self.__list.pop()
        return a
    
    def push(self, a):
        self.__list.append(a)
    
    def isEmpty(self):
        if self.__list:
            return 0
        else:
            return 1
    
    def top(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None