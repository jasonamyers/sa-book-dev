import os
import unittest

from app import get_orders_by_customer


class TestApp(unittest.TestCase):

    def setUp(self):
        self.db_url = os.environ.get('DATABASE_URL')
        os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

    def tearDown(self):
        os.environ['DATABASE_URL'] = self.db_url
        pass

    def test_get_order_by_customer_bad_cust_name(self):
        results = get_orders_by_customer('bad name')
        assert results == []
