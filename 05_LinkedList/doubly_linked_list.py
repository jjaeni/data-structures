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


    def splice_test(self, key):
        new_node = Node(key)
        cnt = 0
        for v in self:
            if v.key == new_node.key:
                print(cnt, "번째 노드의 key값과 일치합니다")
                return
            else:
                cnt+=1
        print('당신이 입력한 노드는 연결리스트에 없습니다 돌아가!!!!')


    def splice(self, a, b, x):
        '''
        a, b, x : Node
        a와 b 사이에는 x Node와 head Node는 있어서는 안됨.

        ------------------------

        a : splice 하고 싶은 Node의 시작점
        b : splice 하고 싶은 Node의 끝점
        x : splice한 노드들을 붙이고 싶은 위치 (x.next) 
        '''
        if a == None or b == None or x == None: # (디버깅 완료)
            return
        
        a_node = None
        b_node = None
        x_node = None
        
        # 조건1: 리스트에서 노드 a 다음에 노드 b가 나와야 함.
        # 조건2: a와 b 사이에 head 노드가 있으면 안 됨.
        # 조건3: a와 b 사이에 x가 있으면 안 됨.
        # 조건4: 주어진 a, b, x가 리스트 안에 없을 수 있다.

        # 조건4: 주어진 a, b, x가 리스트 안에 있는지 확인
        for v in self:
            if v.key == a:
                a_node = v
            elif v.key == b:
                b_node == v
            elif v.key == x:
                x_node = v    

        if a_node == None or b_node == None or x_node == None:
            return

        # 조건3: 
                    
               

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