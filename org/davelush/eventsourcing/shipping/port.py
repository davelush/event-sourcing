from typing import List
import pycountry

# from org.davelush.eventsourcing.shipping.ship import Ship


class Port(object):
    UNKNOWN = -2
    AT_SEA = -1
    # ships: List[Ship] = []
    name: str

    def __init__(self, name: str, country):
        self.name = name
