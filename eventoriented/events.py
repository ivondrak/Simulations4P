class EventNotice:
    def __init__(self, clock, time, event_type, transaction):
        self.clock = clock
        self.event_time = self.clock.time + time
        self.event_type = event_type
        self.transaction = transaction
        self.next_event = None

class EventList:

    def __init__(self):
        self.first_event = None
        self.length = 0

class Agenda:

    def __init__(self, clock):
        self.clock = clock
        self.agenda = EventList()

    def insert(self, event, before, after):
        before.next_event = event
        event.next_event = after

    def scheduleEvent(self, event):
        that = event
        that.next_event = None
        self.agenda.length += 1
        if self.agenda.first_event == None:
            self.agenda.first_event = that
        else:
            if that.event_time < self.agenda.first_event.event_time:
                that.next_event = self.agenda.first_event
                self.agenda.first_event = that
                self.clock.time_of_next_event = self.agenda.first_event.event_time
            else:
                next = self.agenda.first_event
                while that.event_time >= next.event_time and next.next_event:
                    prev = next
                    next = next.next_event
                if that.event_time >= next.event_time and next.next_event == None:
                    self.insert(that, next, None)
                else:
                    self.insert(that, prev, next)
        self.agenda.length += 1

    def getNextEvent(self):
        if self.agenda.first_event == None:
            print("Can't remove any item from empty event list!")
        else:
            current = self.agenda.first_event
            self.agenda.first_event = current.next_event
            self.agenda.length -= 1
            self.clock.time = current.event_time
            if self.agenda.first_event != None:
                self.clock.time_of_next_event = self.agenda.first_event.event_time
            else:
                self.clock.time_of_next_event = float('inf')
            self.current_event = current

    def flushOutEvent(self):
        self.current_event = None

    def transaction(self):
        return self.current_event.transaction
    
    def getEventType(self):
        return self.current_event.event_type
    
    def isEmpty(self):
        return self.agenda.length <= 0