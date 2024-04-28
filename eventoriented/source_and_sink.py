from transaction import Transaction

class SourceAndSink:
    def __init__(self):
        self.count = 0

class Source(SourceAndSink):
    def create(self, clock):
        self.count += 1
        this_client = Transaction(clock)
        this_client.next_in_line = None
        return this_client
    
    def show(self):
        print("Number of clients generated: ", self.count)

class Sink(SourceAndSink):

    def remove(self, client):
        client = None
        self.count += 1

    def show(self):
        print("Number of clients served: ", self.count)