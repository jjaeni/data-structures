class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value # Optional
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key) # print(v)하면 v.key 리턴

class DoublyLinkedList:
    '''
    모든 input은 Node로 주어지며,
    splice에 입력되는 매개변수들의 노드는 연결 리스트 내부에 있는 노드라는 가정하에 작성된 클래스입니다.
    '''
    def __init__(self):
        self.head = Node()
        self.size = 0


    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next


    def __len__(self):
        return self.size
    

    def print_list(self):
        v = self.head.next
        print('h -> ', end='')
        while v != self.head:
            print(str(v.key)+" -> ", end='')
            v = v.next
        print('h')

            
    def splice(self, a, b, x):
        '''
        a, b, x : Node
        a와 b 사이에는 x Node와 head Node는 있어서는 안됨.

        ------------------------

        a : splice 하고 싶은 Node의 시작점
        b : splice 하고 싶은 Node의 끝점
        x : splice한 노드들을 붙이고 싶은 위치 (x.next) 
        '''
        if a == None or b == None or x == None:
            return

        ap = a.prev
        xn = x.next
        if b.next != x:
            bn = b.next

            ap.next = bn
            bn.prev = ap
            x.next = a
            a.prev = x
        else:
            ap.next = x
            x.prev = ap
            x.next = a
            a.prev = x

        b.next = xn
        xn.prev = b


    def move_after(self, a, x):
        '''
        a, x : Node
        '''
        a_node = None
        x_node = None

        for v in self:
            if v.key == a.key:
                a_node = v
            if v.key == x.key:
                x_node = v

        if a_node == None:
            return None
        if x_node == None:
            return None

        self.splice(a_node, a_node, x_node)


    def move_before(self, a, x):
        '''
        a, x : Node
        '''
        a_node = None
        x_node = None
        
        for v in self:
            if v.key == a.key:
                a_node = v
            if v.key == x.key:
                x_node = v
        
        if a_node == None:
            return None
        if x_node == None:
            return None

        self.splice(a_node, a_node, x_node.prev)


    def insert_after(self, a, key):
        '''
        a : Node
        key : key
        '''
        new_node = Node(key)

        if a == None:
            a_node = self.head
        else:
            a_node = None

            for v in self:
                if v.key == a.key:
                    a_node = v
                else:
                    v = v.next

        if a_node == None:
            return
        
        an = a_node.next
        a_node.next = new_node
        new_node.prev = a_node
        new_node.next = an
        an.prev = new_node

        self.size += 1


    def push_front(self, key):
        self.insert_after(None, key)


    def insert_before(self, a, key):
        '''
        a : Node
        key : key
        '''
        new_node = Node(key)

        if a == None:
            hp = self.head.prev
            
            hp.next = new_node
            new_node.prev = hp
            new_node.next = self.head
            self.head.prev = new_node

        else:
            a_node = None
            for v in self:
                if v.key == a.key:
                    a_node = v
                    ap = a_node.prev

                    ap.next = new_node
                    new_node.prev = ap
                    new_node.next = a_node
                    a_node.prev = new_node
                else:
                    v = v.next

        if a_node == None:
            return None

        self.size += 1


    def push_back(self, key):
        self.insert_before(None, key)


    def delete_node(self, x):
        '''
        x : Node
        '''
        x_node = None

        for v in self:
            if v.key == x.key:
                x_node = v
            else:
                v = v.next

        if x_node == None or x == None:
            return None

        xp = x_node.prev
        xn = x_node.next
        xp.next = xn
        xn.prev = xp

        self.size -= 1


    def pop_front(self):
        v = self.head.next
        vp = v.prev
        vn = v.next

        if vp == v:
            return None

        key = v.key

        vp.next = vn
        vn.prev = vp

        self.size -= 1
        return key


    def pop_back(self):
        tail = self.head.prev
        tp = tail.prev

        if tail == self.head:
            return None
        
        key = tail.key

        tp.next = self.head
        self.head.prev = tp
        
        self.size -= 1
        return key


    def search(self, key):
        for v in self:
            if v.key == key:
                return v
            else:
                v = v.next
        return None


    def is_empty(self):
        return self.head.next == self.head


    def first(self):
        if self.head.next == self.head:
            return None
        return self.head.next


    def last(self):
        if self.head.next == self.head:
            return None
        return self.head.prev


    def join(self, list):
        if list.head.next == list.head:
            return None
        stail = self.head.prev
        lhead = list.head.next
        ltail = list.head.prev

        stail.next = lhead
        lhead.prev = stail

        ltail.next = self.head
        self.head.prev = ltail

        self.size += len(list)


    def split(self, x):
        new_list = DoublyLinkedList()
        tail = self.head.prev

        v = x
        cnt = 1

        while v != tail:
            v = v.next
            cnt += 1

        self.splice(x, tail, new_list.head)
        new_list.size = cnt
        self.size -= cnt

        return new_list