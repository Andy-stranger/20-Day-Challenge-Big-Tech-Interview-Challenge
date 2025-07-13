from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.sorted_list = SortedList([]) #unique rates
        self.current_rate = (0,0) #(time,rate)
        self.hash_map = {} #time -> rate
        self.seen = {} #rate -> count

    def update(self, timestamp: int, price: int) -> None:
        cur_time , cur_rate = self.current_rate
        if timestamp > cur_time or (timestamp == cur_time and price != cur_rate):
            self.current_rate = (timestamp,price)
        if timestamp in self.hash_map:
            old = self.hash_map[timestamp]
            self.seen[old] = self.seen.get(old)-1
            if self.seen[old] == 0:
                del self.seen[old]
                self.sorted_list.remove(old)
        self.seen[price] = self.seen.get(price,0) + 1
        if self.seen[price] == 1:
            self.sorted_list.add(price)
        self.hash_map[timestamp] = price


    def current(self) -> int:
        cur_time , cur_rate = self.current_rate
        return cur_rate

    def maximum(self) -> int:
        return self.sorted_list[-1]
        

    def minimum(self) -> int:
        return self.sorted_list[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()