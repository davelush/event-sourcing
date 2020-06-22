from datetime import datetime

from org.davelush.eventsourcing.shipping.port import Port
from org.davelush.eventsourcing.shipping.ship import Ship


class Event(object):
    def __init__(self, ts: datetime, port: Port, ship: Ship):
        pass