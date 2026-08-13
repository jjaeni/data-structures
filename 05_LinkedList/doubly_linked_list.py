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
            print('None')

        else:
            print('None <->', end=' ')

            for v in self:
                print(v.key, '<->', end=' ')
                v = v.next

            print('None')


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
            if v.key == a:
                a_node = v
            elif v.key == b:
                b_node = v
            elif v.key == x:
                x_node = v    

        if a_node == None or b_node == None or x_node == None:
            print('입력한 노드가 리스트에 존재 안하잖아여 구라쟁이')
            return

        # 조건1: b는 a보다 뒤에 있어야 한다.
        v = b_node.next
        while v != self.head:
            if v == a_node:
                print('b가 a보다 앞에 있어요 돌아가세요.')
                return
            else:
                v = v.next

        # 조건3: a와 b 사이에 x가 존재하면 안 된다.
        v = a_node.next
        while v != b_node:
            if v == x_node:
                print('x node가 ab 사이에 존재하잔아여 !!!')
                return
            else:
                v = v.next
        del v

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
            print('b_node의 next 없음')
            # ap <-> x <-> a b
            ap.next = x_node
            x_node.prev = ap
            x_node.next = a_node
            a_node.prev = x_node

        b_node.next = xn
        xn.prev = b_node


    def move_after(self, a, x):
        self.splice(a, a, x)


    def move_before(self, a, x):
        self.splice(a, a, x.prev)


    def insert_after(self, a, key):
        new_node = Node(key)
        self.move_after(new_node, a)


    def insert_before(self, a, key):
        new_node = Node(key)
        self.move_before(new_node, a)


    def push_front(self, key):
        new_node = Node(key)
        self.splice(new_node, new_node, self.head)


    def push_back(self, key):
        new_node = Node(key)

        for v in self:
            if v.next == self.head:
                self.splice(new_node, new_node, v)
            else:
                v = v.next
                                   

    def push_front(self, key):
        new_node = Node(key)

        if len(self) == 0:
            h = self.head
            h.next = new_node
            h.prev = new_node

            new_node.next = h
            new_node.prev = h

        else:
            x = self.head
            y = self.head.next

            new_node.prev = x
            new_node.next = y
            x.next = new_node
            y.prev = new_node

        self.size += 1


    def push_back(self, key):
        new_node = Node(key)

        if len(self) == 0:
            self.head.next = new_node
            self.head.prev = new_node

            new_node.next = self.head
            new_node.prev = self.head

        else:
            # x <- (new_node) <-> self.head
            x = self.head.prev
            y = self.head

            new_node.next = self.head
            new_node.prev = self.head.prev
            x.next = new_node
            self.head.prev = new_node

        self.size += 1


    def pop_front(self):
        x = self.head
        y = x.next # self.head.next
        z = y.next

        if len(self) == 0:
            return None
        else:
            x.next = z
            x.prev = z
            z.prev = x
            z.next = x
            self.size -= 1
            return y.key

            
    def pop_back(self):
        pass