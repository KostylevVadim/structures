class Node:
    def __init__(self, data, left, right, head):
        
        self.__data = data
        self.left = left
        self.right = right
        self.head = head
        
    def __str__(self) -> str:
        s1 = str(self.__data)
        if self.head:
            s1 += ' Head is: '+str(self.head.get_data())
        return 'Data in node: ' + s1
        
    def get_data(self):
        return self.__data
    


class BinaryTree:
    
    def __init__(self):
        self.__root = None

    def __str__(self):

        return 'Root is '+ str(self.__root) + ' List of data: ' + str(self.__data_list)
    
    
    
    def root(self):
        return self.__root
    
    def _tree_shower(self, node: Node):
        if node is None:
            return
        str1 =''
        str1+=str(node.get_data())
        #print(node)
        str1+='('
        if node.left is not None:
            
            str1+=self._tree_shower(node.left)
        if node.right is not None:
            str1+=' '+self._tree_shower(node.right)
        str1+=')'
        return str1

    def show_tree(self):
        str1 = ''
        if self.__root is None:
            print('NO data')
        else:
            
            str1+=str(self.__root)+'\n('
            if self.__root.left is not None:
                str1+=self._tree_shower(self.__root.left)
            if self.__root.right is not None:
                str1+=' '+self._tree_shower(self.__root.right)
            str1+=')'
        return str1
    
    def __find_place(self, cura: Node, a):
        
        if cura.get_data() == a:
            return [cura, 'NOWAY', 'NO']
        if cura.get_data() > a and cura.left is None:
            return [cura, 'LEFT', 'YES']
        elif cura.get_data() > a and cura.left is not None:
            return self.__find_place(cura.left, a)
        elif cura.get_data() < a and cura.right is None:
            return [cura, 'RIGHT', 'YES']
        elif cura.get_data() < a and cura.right is not None:
            return self.__find_place(cura.right, a)
            


    def add(self, data):
        if self.__root is None:
            self.__root = Node(data, None, None, None)
        elif self.__root.get_data() == data:
            return
        elif self.__root.get_data()> data:
            print('goleft')
            if self.__root.left is None:
                self.__root.left = Node(data, None, None, self.__root)
            else:
                x = self.__find_place(self.__root.left, data)
                print(str(x[0]))
                if x[2] == 'YES':
                    if x[1] == 'LEFT':
                        x[0].left = Node(data, None, None, x[0])
                    else:
                        x[0].right = Node(data, None, None, x[0])
        elif self.__root.get_data()<data:
            print('goright')
            if self.__root.right is None:
                self.__root.right = Node(data, None, None, self.__root)
            else:
                x = self.__find_place(self.__root.right, data)
                if x[2] == 'YES':
                    if x[1] == 'LEFT':
                        x[0].left = Node(data, None, None, x[0])
                    else:
                        x[0].right = Node(data, None, None, x[0])

    def go_with_width(self):
        x= self.__root
        v = [x]
        c = 3
        j = 0
        while len(v)>0 and j<c:
            vn = []
            for i in v:
                if i.left is not None:
                    vn.append(i.left)
                if i.right is not None:
                    vn.append(i.right)
            if vn:
                for i in vn:
                    print(i)
            v = vn[:]
            j+=1
    
    def __goer(self, node: Node):
        if node is None:
            return
        self.__goer(node.left)
        print(node.get_data())
        self.__goer(node.right)

    def go_with_high(self):
        self.__goer(self.__root)



            

    
        

        

            


        
    