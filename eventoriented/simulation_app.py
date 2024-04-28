from clock import Clock
from monitor import Monitor
from source_and_sink import Source, Sink
from events import EventNotice
from eventoriented.queue import Queue
from server import Server
from utilities.histogram import Histogram

import statistics as stats

class GeneratorFactory:
    def __init__(self, number_of_samples=1000, seed=None):
        self.number_of_samples = number_of_samples
        self.seed = seed

    def createArrivals(self):
        pass
    def createServices(self):
        pass

class SimulationApp:
    
    def __init__(self, title, generator_factory):
        self.title = title
        self.clock = Clock()
        self.monitor = Monitor(self.clock, generator_factory.number_of_samples)
        self.source = Source()
        self.sink = Sink()
        self.queue = Queue(self.clock)
        self.server = Server(self.clock)
        self.arrivals = generator_factory.createArrivals()
        self.services = generator_factory.createServices()
        self.arrivals.generate()
        self.services.generate()
        self.spent_time = []
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'arrival', None))
    
    def run(self):
        while self.monitor.moreSamples() and self.monitor.moreEvents():
            self.monitor.agenda.getNextEvent()
            self.execute()
            self.monitor.agenda.flushOutEvent()
        self.show()
    
    def execute(self):
        event_type = self.monitor.agenda.getEventType()
        if event_type == 'arrival':
            self.arrival()
        elif event_type == 'start':
            self.start()
        elif event_type == 'finish':
            self.finish(self.monitor.agenda.transaction())
        elif event_type == 'departure':
            self.departure(self.monitor.agenda.transaction())
        else:
            print('Unknown event type')

    def arrival(self):
        time = self.arrivals.next()
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, time, 'arrival', None))
        client = self.source.create(self.clock)
        self.queue.fileInto(client)
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'start', None))

    def start(self):
        time = self.services.next()
        if self.server.isAvailable() and self.queue.length > 0:
            self.server.seize()
            client = self.queue.takeFirst()
            self.monitor.agenda.scheduleEvent(EventNotice(self.clock, time, 'finish', client))

    def finish(self, client):
        self.server.release()
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'departure', client))
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'start', None))

    def departure(self, client):
        time = client.flowTime()
        print('Client spent time: ', time)
        self.spent_time.append(time)
        self.sink.remove(client)
        self.monitor.update()

    def show(self):
        print(self.title)
        self.monitor.show()
        self.source.show()
        self.sink.show()
        self.queue.show()
        self.server.show()
        self.sink.show()
        self.arrivals.plot_distribution()
        self.services.plot_distribution()
        Histogram(self.spent_time).plot()