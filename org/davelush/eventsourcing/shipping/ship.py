from typing import List

from org.davelush.eventsourcing.shipping.cargo import Cargo


class Ship(object):
    cargo: List[Cargo] = []
