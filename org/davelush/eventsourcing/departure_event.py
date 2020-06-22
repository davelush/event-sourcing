from datetime import datetime

from org.davelush.eventsourcing.event import Event
from org.davelush.eventsourcing.shipping.port import Port
from org.davelush.eventsourcing.shipping.ship import Ship


class DepartureEvent(Event):

    def __init__(self, ts: datetime, port: Port, ship: Ship):
        super(DepartureEvent, self).__init__(ts, port, ship)
