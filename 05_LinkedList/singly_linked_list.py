class Node:
    def __init__(self, key, value = None):
        self.key = key # 노드에 저장되는 key 값으로 이 값으로 노드를 구분
        self.value = value # 추가 정보가 있다면 value에 저장 (optional)
        self.next = None # 다음에 연결될 노드(의 주소 또는 reference): 초기값은 None


    def __str__(self): # print 함수를 이용해 출력할 때의 문자열 리턴
        return str(self.key) # ex) print(v) -> key값인 3을 print



class SinglyLinkedList:
    def __init__(self):
        self.head = None # head node 지정
        self.size = 0 # list의 크기


    def __len__(self):
        return self.size
    

    def print_list(self):
        v = self.head
        while v:
            print(v.key, "->", end=" ")
            v = v.next
        print("None")


    def push_front(self, key, value=None):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def push_back(self, key, value=None):
        new_node = Node(key)

        if len(self) == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        
        self.size += 1


    def pop_front(self):
        # 사이즈 감소, head 변경
        if len(self) == 0:
            return None
        
        else:
            x = self.head
            key = x.key
            self.head = self.next
            self.size -= 1
            del x
            return key


    def pop_back(self):
        # 사이즈 감소, tail이 변경
        if len(self) == 0:
            return None
        
        else:
            prev = None
            tail = self.head

            while tail.next != None:
                prev = tail
                tail = tail.next

            if len(self) == 1:
                x = self.head
                key = x.key
                self.head = None
                self.size -= 1
                del x
                return key

            else:
                x = tail
                key = x.key
                prev.next = tail.next
                self.size -= 1
                del x
                return key


    def search(self, key):
        for v in self:
            if v.key == key:
                return v
        return None


    def __iter__(self):
        v = self.head
        while v != None:
            yield v # yield = return
            v = v.next


    def remove(self, node):
        if node == None: # key 값을 찾은 노드 v를 node라고 칭함
            return False
        else: # key 값 갖는 노드가 존재할 때
            if node == self.head:
                self.head = self.next
                self.size -= 1
                return True
            else:
                for v in self:
                    if node == v:
                        v = v.next
                        self.size -= 1
                        return True