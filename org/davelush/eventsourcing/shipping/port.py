from typing import List

from org.davelush.eventsourcing.shipping.ship import Ship


class Port(object):
    ships: List[Ship] = []
