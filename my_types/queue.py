class Queue:
    def __init__(self, **kwargs):
        

        if kwargs.get('list'):
            
            self.__list = kwargs['list']
        else:
            
            self.__list = []
        #print(self.__list)

    
    def Dequeue(self):
        if self.__list:
            a = self.__list.pop(0)
            return a
    
    def Enqueue(self, a):
        self.__list.append(a)
    
    def isEmpty(self):
        if self.__list:
            return 0
        else:
            return 1
    
    def top(self):
        if self.__list:
            return self.__list[0]
        else:
            return None
        

