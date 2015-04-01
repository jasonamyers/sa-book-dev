import unittest

from decimal import Decimal

from db import dal, prep_db
from app import get_orders_by_customer


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')
        prep_db()

    @classmethod
    def tearDownClass(cls):
        dal.connection.close()

    def setUp(self):
        self.cookie_orders = [(u'wlk001', u'cookiemon', u'111-111-1111')]
        self.cookie_details = [
            (u'wlk001', u'cookiemon', u'111-111-1111',
                u'dark chocolate chip', 2, Decimal('1.00')),
            (u'wlk001', u'cookiemon', u'111-111-1111',
                u'oatmeal raisin', 12, Decimal('3.00'))]

    def test_orders_by_customer_bad_cust_name(self):
        results = get_orders_by_customer('bad name')
        assert results == []

    def test_orders_by_customer(self):
        results = get_orders_by_customer('cookiemon')
        assert results == self.cookie_orders

    def test_orders_by_customer_shipped_only(self):
        results = get_orders_by_customer('cookiemon', True)
        assert results == []

    def test_orders_by_customer_unshipped_only(self):
        results = get_orders_by_customer('cookiemon', False)
        assert results == self.cookie_orders

    def test_orders_by_customer_with_details(self):
        results = get_orders_by_customer('cookiemon', details=True)
        assert results == self.cookie_details

    def test_orders_by_customer_shipped_only_with_details(self):
        results = get_orders_by_customer('cookiemon', True, True)
        assert results == []

    def test_orders_by_customer_unshipped_only_details(self):
        results = get_orders_by_customer('cookiemon', False, True)
        assert results == self.cookie_details

    def test_orders_by_customer_without_details(self):
        results = get_orders_by_customer('cookiemon', details=False)
        assert results == self.cookie_orders

    def test_orders_by_customer_shipped_only_no_details(self):
        results = get_orders_by_customer('cookiemon', True, False)
        assert results == []

    def test_orders_by_customer_unshipped_only_no_details(self):
        results = get_orders_by_customer('cookiemon', False, False)
        assert results == self.cookie_orders
