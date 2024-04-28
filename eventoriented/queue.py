class Queue:
    def __init__(self, clock):
        self.clock = clock
        self.start_time = self.clock.time
        self.first = None
        self.last = None
        self.length = 0
        self.max_length = 0
        self.time_of_last_change = 0
        self.length_integral = 0
        self.num_of_entries = 0
        self.num_of_departures = 0

    def meanQueueLength(self):
        if self.clock.time > 0:
            return self.length_integral / (self.clock.time - self.start_time)
        else:
            return 0
        
    def meanQueueDelay(self):
        if self.clock.time > 0:
            return self.length_integral / self.num_of_departures
        else:
            return 0
    
    def fileInto(self, transaction):
        self.num_of_entries += 1
        self.length += 1
        self.length_integral += (self.length-1) * (self.clock.time - self.time_of_last_change)
        self.time_of_last_change = self.clock.time
        if self.length > self.max_length:
            self.max_length = self.length
        if (self.length - 1) == 0:
            self.first = transaction
        else:
            self.last.next_in_line = transaction
        transaction.next_in_line = None
        self.last = transaction
    
    def takeFirst(self):
        if self.length <= 0:
            print("Can't remove item from an empty queue!")
            return None
        else:
            self.num_of_departures += 1
            self.length -= 1
            self.length_integral += (self.length+1) * (self.clock.time - self.time_of_last_change)
            self.time_of_last_change = self.clock.time
            transaction = self.first
            self.first = transaction.next_in_line
            if self.length == 0:
                self.last = None
            return transaction
    
    def show(self):
        max = self.max_length
        mean = self.meanQueueLength()
        delay = self.meanQueueDelay()
        print('Queue report:')
        print('Items entered: ', self.num_of_entries)
        print('Items departed: ', self.num_of_departures)
        print('Queue current length: ', self.length)
        print('Queue max length: ', max)
        print('Queue mean length: ', round(mean, 2))
        print('Queue mean delay: ', round (delay, 2))