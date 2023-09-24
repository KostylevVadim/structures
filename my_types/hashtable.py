import hashlib

#Hashtable using python hash()
class Hashtable:
    def __init__(self, l: list) -> None:
        self.__dict = {}
        
        for elem in l:
            key = hash(str(elem))
            self.__dict[key] = elem
    
    def __str__(self) -> str:
        s = 'Dictionary:\n'
        for key, value in self.__dict.items():
            s+='key: '+ str(key)+' value: '+ str(value)+'\n'
        return s
    
    def in_hash(self, data):
        if data is None:
            return False
        x = hash(str(data))
        if x in self.__dict.keys():
            return True
        else:
            return False
        
    def add(self, data):
        if data is None:
            return
        x = hash(str(data))
        self.__dict[x] = data
        return
    
    def remove(self, data):
        if self.in_hash(data):
            self.__dict.pop(hash(str(data)))
            return 
        return
    
#Hashtable created hash()
class Hashtable_new:
    def _hash(self, data):
        return int(data)%(self.__reserved_length)
    
    
    def __init__(self,data, reserved_length) -> None:
        self.__list = []
        self.__reserved_length = reserved_length
        for i in range(reserved_length):
            self.__list.append([None]*reserved_length)
        #print(self.__list)
        for i in range(len(data)):
            key = self.__hash(data[i])
            j = 0
            flag = 0
            if j<self.__reserved_length:
                if self.__list[key][j] is None:
                    flag = 1
            while flag ==0 and j<self.__reserved_length:
                    j+=1
                    #print(i,j, self.__reserved_length)
                    if j<self.__reserved_length:
                        if self.__list[key][j] is None:
                            flag = 1
            #print(key, j, data[i], self.__list[key])
            if self.__list[key][-1] is None:
                self.__list[key][j] = data[i]
            
        #print(self.__list)

    def __str__(self):
        count = 0
        
        for i in range(len(self.__list)):
            count+=self.__list[i].count(None)
        fill = (self.__reserved_length * self.__reserved_length - count+0.0)/(self.__reserved_length * self.__reserved_length)
        s1 = 'Data:\n'
        s1+= ''
        for i in range(self.__reserved_length):
            if self.__list[i][0] is not None:
                
                s ='Key: '+str(i)+' Data: '
                s1+=s
                j = 0
                flag = 0
                while flag ==0 and j<self.__reserved_length:
                    s1+= str(self.__list[i][j]) +' '
                    j+=1
                    if j<self.__reserved_length:
                        if self.__list[i][j] is None:
                            flag = 1
                    
                    
                s1+='\n'
        s1+='Filled: '+ str(fill)+'\n'
        s1+='Reserved: '+ str(self.get_rezerved_size())
        return s1        

    def __rehash(self):
        count = 0
        for i in range(len(self.__list)):
            count+=self.__list[i].count(None)
        
        fill = (self.__reserved_length * self.__reserved_length - count+0.0)/(self.__reserved_length * self.__reserved_length)
        if fill> 0.65:
            list_of_data = []
            for i in range(len(self.__list)):
                for j in range(len(self.__list[i])):
                    if self.__list[i][j] is not None:
                        list_of_data.append(self.__list[i][j])
            self.__list = []
            self.__reserved_length  = self.__reserved_length **2
            for i in range(self.__reserved_length):
                self.__list.append([None]*self.__reserved_length)
        #print(self.__list)
            for i in range(len(list_of_data)):
                key = self.__hash(list_of_data[i])
                j = 0
                flag = 0
                if j<self.__reserved_length:
                    if self.__list[key][j] is None:
                        flag = 1
                while flag ==0 and j<self.__reserved_length:
                    j+=1
                    #print(i,j, self.__reserved_length)
                    if j<self.__reserved_length:
                        if self.__list[key][j] is None:
                            flag = 1
            #print(key, j, data[i], self.__list[key])
                if self.__list[key][-1] is None:
                    self.__list[key][j] = list_of_data[i]
        return 

    def add(self, data):
        key = self.__hash(int(data))
        
        if self.__list[key][-1] is None:
            j= 0
            while self.__list[key][j]!= None:
                j+=1
            self.__list[key][j] = data
        self.__rehash()
        
        return
    
    def remove(self, data):
        key = self.__hash(int(data))
        j = 0
        while j<self.__reserved_length:
            if self.__list[key][j]==data:
                self.__list[key][j]= None
                j+=self.__reserved_length
            j+=1
    
    def get_rezerved_size(self):
        return self.__reserved_length*self.__reserved_length

    # def content(self):
    #     return self.__list