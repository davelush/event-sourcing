import datetime
import unittest
import pycountry
import pytest

from org.davelush.eventsourcing.arrival_event import ArrivalEvent
from org.davelush.eventsourcing.departure_event import DepartureEvent
from org.davelush.eventsourcing.event_processor import EventProcessor
from org.davelush.eventsourcing.shipping.cargo import Cargo
from org.davelush.eventsourcing.shipping.port import Port
from org.davelush.eventsourcing.shipping.ship import Ship


sfo = Port("San Francisco", pycountry.countries.get(alpha_3='USA'))
la = Port("Los Angeles", pycountry.countries.get(alpha_3='USA'))
yyv = Port("Vancouver", pycountry.countries.get(alpha_3='CAN'))


class TestEventProcessor(unittest.TestCase):

    def setUp(self) -> None:
        self.eproc = EventProcessor()
        self.refact = Cargo("refactoring")
        self.kr = Ship("King Roy")

    def test_arrival_set_ships_location(self):
        self.eproc.process(ArrivalEvent(datetime.datetime(2005, 1, 11), sfo, self.kr))
        self.assertEqual(sfo, self.kr.port)

    def test_departure_puts_ship_out_to_sea(self):
        self.eproc.process(ArrivalEvent(datetime.datetime(2005, 10, 1), la, self.kr))
        self.eproc.process(ArrivalEvent(datetime.datetime(2005, 11, 1), sfo, self.kr))
        self.eproc.process(DepartureEvent(datetime.datetime(2005, 11, 1), sfo, self.kr))
        self.assertEqual(Port.AT_SEA, self.kr.port)
