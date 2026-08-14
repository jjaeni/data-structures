class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value # Optional
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key) # print(v)하면 v.key 리턴

class DoublyLinkedList:
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
        if self.size == 0:
            print('h')

        else:
            print('h <->', end=' ')

            for v in self:
                print(v.key, '<->', end=' ')
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
        
        a_node = None
        b_node = None
        x_node = None

        # 조건4: 주어진 a, b, x가 리스트 안에 있는지 확인
        # 조건2: head 노드는 중간에 없어야 함
        for v in self:
            if v.key == a.key:
                a_node = v
            if v.key == b.key:
                b_node = v
            if v.key == x.key:
                x_node = v
            v = v.next


        if a_node == None:
            print('a_node가 없어요') #
            return
        if b_node == None:
            print('b_node가 없어요') #
            return
        if x_node == None:
            print('x_node가 없어요') #
            return


        # 조건1: b는 a보다 뒤에 있어야 한다.
        v = b_node.next
        while v != self.head:
            if v == a_node:
                print('b가 a보다 앞에 있어요 돌아가세요.') #
                return
            else:
                v = v.next


        # 조건3: a와 b 사이에 x가 존재하면 안 된다.
        v = a_node
        while v != b_node:
            if v == x_node:
                print('x node가 ab 사이에 존재') #
                return
            else:
                 v = v.next


        ap = a_node.prev
        xn = x_node.next
        # b.next가 존재할 때와, 존재하지 않을 때
        if b_node.next != x_node: # b_node의 next 존재
            bn = b_node.next

            # ap <-> bn  x <-> a b
            ap.next = bn
            bn.prev = ap
            x_node.next = a_node
            a_node.prev = x_node
            
        else:
            # ap <-> x <-> a b
            ap.next = x_node
            x_node.prev = ap
            x_node.next = a_node
            a_node.prev = x_node

        b_node.next = xn
        xn.prev = b_node

        self.print_list()


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
            print('a 노드가 없어요') #
            return
        if x_node == None:
            print('x 노드가 없어요') #
            return

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
            print('a 노드가 없어요') #
            return
        if x_node == None:
            print('x 노드가 없어요') #
            return

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
                    an = a_node.next
                else:
                    v = v.next

        if a_node == None:
            print('a node가 없어요. 다시 입력하세요') #
            return
        
        an = a_node.next
        a_node.next = new_node
        new_node.prev = a_node
        new_node.next = an
        an.prev = new_node

        self.size += 1
        self.print_list()


    def push_front(self, key):
        self.insert_after(None, key)


    def insert_before(self, a, key):
        '''
        a : Node
        key : key
        '''
        new_node = Node(key)

        if a == None:
            for v in self:
                if v.next == self.head:
                    a_node = v # 마지막꺼
                    an = v.next # 헤드

                    a_node.next = new_node
                    new_node.prev = a_node
                    new_node.next = an
                    an.prev = new_node
                else:
                    v = v.next
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
            print('a node가 없어요. 다시 입력하세요') #
            return

        self.size += 1
        self.print_list()


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
            print('x 노드가 없거나, head 원소입니다') #
            return

        xp = x_node.prev
        xn = x_node.next
        xp.next = xn
        xn.prev = xp

        self.size -= 1
        self.print_list()


    def pop_front(self):
        v = self.head.next
        vp = v.prev
        vn = v.next

        if vp == v:
            print('헤드밖에 업다') #
            return None

        key = v.key

        vp.next = vn
        vn.prev = vp

        self.size -= 1
        self.print_list()

        return key


    def pop_back(self):
        v_node = None
        
        for v in self:
            if v.next == self.head:
                v_node = v
                vp = v_node.prev
                vn = v_node.next
            else:
                v = v.next

        if v_node == None:
            print('헤드박에 업다') #
            return None

        vp.next = vn
        vn.prev = vp

        self.size -= 1
        self.print_list()