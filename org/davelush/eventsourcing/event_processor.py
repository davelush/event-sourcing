from org.davelush.eventsourcing.arrival_event import ArrivalEvent
from org.davelush.eventsourcing.departure_event import DepartureEvent
from org.davelush.eventsourcing.event import Event


class EventProcessor(object):

    def process(self, ev: Event) -> None:
        pass
