from typing import List

from org.davelush.eventsourcing.shipping.cargo import Cargo
from org.davelush.eventsourcing.shipping.port import Port


class Ship(object):
    cargo: List[Cargo] = []
    port: Port
    name: str

    def __init__(self, name: str):
        self.name = name
        self.port = Port.UNKNOWN
