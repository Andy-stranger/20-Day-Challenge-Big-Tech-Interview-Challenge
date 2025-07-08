class LinkedList:
    def __init__(self,key: int, value:int):
        self.val = (key,value)
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_map = {}
        self.cap = capacity
        self.cache_list_head = LinkedList(-1,-1)
        self.cache_list_tail = LinkedList(-1,-1)
        self.cache_list_head.next = self.cache_list_tail
        self.cache_list_tail.prev = self.cache_list_head


    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1
        node = self.cache_map[key]
        k,val = node.val
        self.__update_key(key,node)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.__delete_node(key,self.cache_map[key])
        new_node = LinkedList(key,value)
        self.__insert_first(key,new_node)
        if len(self.cache_map) > self.cap:
            self.__delete_last()

    def __update_key(self,key: int, node: LinkedList) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = self.cache_list_head
        node.next = self.cache_list_head.next
        self.cache_list_head.next.prev = node
        self.cache_list_head.next = node
        self.cache_map[key] = self.cache_list_head.next
    
    def __insert_first(self, key: int, node: LinkedList) -> None:
        node.prev = self.cache_list_head
        node.next = self.cache_list_head.next
        self.cache_list_head.next.prev = node
        self.cache_list_head.next = node
        self.cache_map[key] = self.cache_list_head.next
    
    def __delete_last(self) -> None:
        del_node = self.cache_list_tail.prev
        if del_node != self.cache_list_head:
            key,val = del_node.val
            prev = del_node.prev
            self.cache_list_tail.prev = prev
            if prev:
                prev.next = self.cache_list_tail
            del self.cache_map[key]
    
    def __delete_node(self, key: int, node: LinkedList) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        del self.cache_map[key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)